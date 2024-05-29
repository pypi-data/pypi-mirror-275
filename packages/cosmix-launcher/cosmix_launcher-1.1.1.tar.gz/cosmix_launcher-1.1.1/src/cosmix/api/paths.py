import os
from os.path import join


__all__ = (
    "LOCAL_PATH",
    "CR_DIR"
    "WORK_DIR",
    "DEPS",
    "INSTANCES",
    "path_to_cr",
    "path_to_cq_deps",
    "update_work_dir",
)


LOCAL_PATH = (
    os.environ.get("APPDATA") or
    os.environ.get("XDG_DATA_HOME") or
    join(os.environ["HOME"], ".local", "share")
)

CR_DIR     = join(LOCAL_PATH, "cosmic-reach")
WORK_DIR   = join(LOCAL_PATH, "cosmix")
DEPS       = join(WORK_DIR, "deps")
INSTANCES  = join(WORK_DIR, "instances")


def path_to_cr(version: str) -> str:
    return join(DEPS, "cosmic-reach", version + ".jar")


def path_to_cq_deps(version: str) -> str:
    return join(DEPS, "cosmic-quilt", version)


def update_work_dir(path: str):
    global WORK_DIR, DEPS, INSTANCES
    WORK_DIR   = path
    DEPS       = join(WORK_DIR, "deps")
    INSTANCES  = join(WORK_DIR, "instances")
