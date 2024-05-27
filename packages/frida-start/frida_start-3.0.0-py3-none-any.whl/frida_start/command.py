#!/usr/bin/env python3

"""This script aims to automate the process of starting frida-server
on an Android device (for now). The script is a part of AndroidTamer
project and is based on this issue:
https://github.com/AndroidTamer/Tools_Repository/issues/234.

This script performs following things:
1. Try to determine the device architecture
2. Download the frida-server and extract it
3. Push it to the device and execute it
4. Save the PID of the process and write it to 'frida.pid' file.

#Todo:
* Better exception handling.
* Implement better/robust architecture detection code
* Implement for more devices
* Implement the feature to kill frida-server afterwards
"""

import argparse
import logging
import os
import subprocess
import sys
import lzma
import pathlib

import requests

from frida_start import __version__

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format="[%(asctime)s] [%(name)s: %(levelname)s]: %(message)s",
)
log = logging.getLogger("frida-start")

try:
    from frida import __version__ as FRIDA_VERSION
except ImportError:
    log.error("Frida not found. Please run `pip install frida` to proceed.")
    sys.exit(1)

# Just put "adb" below, if adb exists in your system path.
ADB_PATH = "adb"
DOWNLOAD_PATH = pathlib.Path.home() / ".frida-start"


def list_devices():
    """
    Return devices conected to adb
    :return: list
    """
    cmd = f"{ADB_PATH} devices -l"
    output = (
        subprocess.check_output(cmd, shell=True)
        .strip()
        .decode("utf-8")
        .replace("\r", "")
        .split("\n")
    )

    devices = set()
    for device in output[1:]:
        device = device.strip()
        if device != "":
            devices.add(tuple(device.split()))

    return {d[0]: {t.split(":")[0]: t.split(":")[1] for t in d[2:]} for d in devices}


def get_device_arch(transport_id=None):
    """This function tries to determine the architecture of the device, so that
    the correct version of Frida-server can be downloaded.

    :returns either "arch" that Frida release page understands or None.
    """
    arch = None

    getprop_cmd = f"{ADB_PATH} -t {transport_id} shell getprop ro.product.cpu.abi"
    getprop_archs = ["armeabi", "armeabi-v7a", "arm64-v8a", "x86", "x86_64"]
    # We know shell=True is bad, but should be fine here.
    output = (
        subprocess.check_output(getprop_cmd, shell=True).lower().strip().decode("utf-8")
    )

    if output in getprop_archs:
        if output in ["armeabi", "armeabi-v7a"]:
            arch = "arm"
        elif output == "arm64-v8a":
            arch = "arm64"
        else:
            arch = output

    return arch


def prepare_download_url(arch):
    """Depending upon the arch provided, the function returns the download URL."""
    return f"https://github.com/frida/frida/releases/download/{FRIDA_VERSION}/frida-server-{FRIDA_VERSION}-android-{arch}.xz"


def download_and_extract(url, fpath, force_download=False):
    """This function downloads the given URL, extracts .xz archive
    as given file name.

    :returns True if successful, else False.
    """
    data = None
    DOWNLOAD_PATH.mkdir(exist_ok=True)

    fpath = DOWNLOAD_PATH / fpath

    if fpath.is_file() and not force_download:
        log.info(f"Using {fpath.name} from downloaded cache")
        return True

    log.warning(f"Downloading: {url}")
    req = requests.get(url, stream=True)
    if req.status_code == 200:
        # Downloading and writing the archive.
        archive_name = fpath.with_suffix(".xz")

        req.raw.decode_content = True
        with open(archive_name, "wb") as fh:
            for chunk in req.iter_content(1024):
                fh.write(chunk)

        with lzma.open(archive_name) as fh:
            data = fh.read()

        os.unlink(archive_name)
    else:
        log.error(
            f"ERROR: downloading frida-server. Got HTTP status code {req.status_code} from server."
        )

    if data:
        log.info(f"Writing file as: {fpath}")
        fpath.write_bytes(data)
        return True
    return False


def push_and_execute(fname, transport_id=None):
    """This function pushes the file to device, makes it executable,
    and then finally runs the binary. The function also saves the PID
    of process in 'frida.pid' file.
    """

    fname = DOWNLOAD_PATH / fname

    push_cmd = [
        ADB_PATH,
        "-t",
        transport_id,
        "push",
        str(fname),
        "/data/local/tmp/frida-server",
    ]
    chmod_cmd = [
        ADB_PATH,
        "-t",
        transport_id,
        "shell",
        "chmod 0755 /data/local/tmp/frida-server",
    ]
    kill_cmd = [
        ADB_PATH,
        "-t",
        transport_id,
        "shell",
        "su",
        "0",
        "killall",
        "frida-server",
    ]
    execute_cmd = [
        ADB_PATH,
        "-t",
        transport_id,
        "shell",
        "su",
        "0",
        "/data/local/tmp/frida-server",
    ]

    res = subprocess.Popen(push_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    res.wait()

    if res.returncode != 0:
        log.error(
            f"Could not push the binary to device. {res.stdout.read().decode()}{res.stderr.read().decode()}"
        )
        return

    log.info("File pushed to device successfully.")
    subprocess.Popen(chmod_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).wait()

    log.info("Killing all frida-server on device.")
    subprocess.Popen(kill_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).wait()

    log.info("Executing frida-server on device.")
    res = subprocess.Popen(execute_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ret_code = None
    try:
        ret_code = res.wait(3)
    except:
        pass

    if ret_code is not None and ret_code != 0:
        decoded = res.stderr.readline().decode("utf-8")
        log.error(f"Error executing frida-server. {decoded}")


def main():
    """This function is where the magic happens."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--device-name", required=False)
    parser.add_argument(
        "-f", "--force", help="force download", action="store_true", default=False
    )
    parser.add_argument("--version", action="version", version=__version__)
    ops = parser.parse_args()

    devices = list_devices()
    if len(devices) == 0:
        log.error("No device found. Exiting.")
        sys.exit(1)

    log.info("Devices: {}".format(", ".join([dname for dname, _ in devices.items()])))

    if len(devices) != 1 and ops.device_name is None:
        parser.exit(2, "Multiple devices conected select one with -d\n")
    elif ops.device_name is not None and ops.device_name not in devices:
        parser.exit(2, f"Device {ops.device_name} not found\n")

    if ops.device_name is None:
        ops.device_name, _ = next(iter(devices.items()), None)

    log.info(f"Current installed Frida version: {FRIDA_VERSION}")

    transport_id = devices[ops.device_name]["transport_id"]
    arch = get_device_arch(transport_id=transport_id)

    if arch:
        log.info(f"Found arch: {arch}")
        url = prepare_download_url(arch)
        fname = f"frida-server-{FRIDA_VERSION}-android-{arch}"
        if download_and_extract(url, fname, ops.force):
            push_and_execute(fname, transport_id=transport_id)
    else:
        log.info("Could not determine device's arch. Exiting.")


if __name__ == "__main__":
    main()
