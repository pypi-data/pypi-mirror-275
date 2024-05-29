from . import api
from .api.instance import Instance
from .api import paths
from .api import logger
from .api import net
from .api import versions
from .api import config
from typing import Optional
import sys
import click
from click_aliases import ClickAliasedGroup
import os
import send2trash
import shutil


@click.group(cls=ClickAliasedGroup)
@click.option("--work-dir", "-w", type=str, default=paths.WORK_DIR, help="Set a working directory for Cosmix.")
def cosmix(work_dir: str):
    if work_dir != paths.WORK_DIR:
        paths.update_work_dir(os.path.abspath(work_dir))
        # We clear config caches here just in case the config was cached before the
        # working directory was updated
        config._CACHED_CONFIG = None
        logger._sanatization_mode = None
        logger._sanatized_username = None
        logger._colored_logs = None
        logger.info("Set working directory to " + work_dir)


@cosmix.command()
def version():
    """Shows the current cosmix version."""
    logger.info("Cosmix " + api.VERSION)


@cosmix.command()
@click.option("--no-versions", "-V", is_flag=True, default=False, help="Disables latest version checks.")
def debug(no_versions: bool):
    """Shows debug information."""
    logger.info("Cosmix " + api.VERSION)
    logger.info("Paths:")
    logger.info("  Local Path: " + paths.LOCAL_PATH)
    logger.info("  Work Dir:   " + paths.WORK_DIR)
    logger.info("  Instances:  " + paths.INSTANCES)
    logger.info("  Deps:       " + paths.DEPS)
    if not no_versions:
        logger.info("Latest Available Versions: (these may take a second)")
        logger.info("  Cosmic Reach: " + versions.get_latest_of("reach"))
        logger.info("  Cosmic Quilt: " + versions.get_latest_of("quilt"))


@cosmix.command(aliases = ["new"])
@click.option("--version", "-v", default="latest", type=str, help="The version of Cosmic Reach to use. Use 'auto' for auto-updating. Defaults to 'latest'")
@click.option("--quilt-version", "-q", default=None, type=str, help="The Cosmic Quilt version to use. Use 'auto' for auto-updating.")
@click.option("--display-name", "-n", default=None, type=str, help="An optional display name to use for the instance.")
@click.argument("name")
def add(version: str, quilt_version: str, display_name: Optional[str], name: str):
    """Adds a new instance."""
    if Instance.exists(name):
        logger.error("Instance already exists.")
        exit(1)
    instance = Instance.make_instance(name, version, quilt_version, display_name)
    instance.download()
    logger.info("Made instance " + name)


@cosmix.command()
@click.option("--version", "-v", default="none", type=str, help="The version of Cosmic Reach to update to. Use 'auto' for auto-updating. Defaults to 'none'")
@click.option("--quilt-version", "-q", default="none", type=str, help="The Cosmic Quilt version to update to. Use 'auto' for auto-updating. Defaults to 'none'")
@click.argument("name")
def update(version: str, quilt_version: str, name: str):
    """Updates an existing instance."""
    instance = Instance.get_or_throw(name)

    if version != "none":
        if version == "auto":
            instance.version = versions.get_latest_of("reach")
            instance.auto_update_reach = True
        else:
            instance.version = versions.get_version_or_latest_of("reach", version)

    if quilt_version != "none":
        if quilt_version == "auto":
            instance.quilt_version = versions.get_latest_of("quilt")
            instance.auto_update_quilt = True
        else:
            instance.quilt_version = versions.get_version_or_latest_of("quilt", quilt_version)

    instance.save()
    instance.download(is_updating = True)

    logger.info("Updated instance " + name)


@cosmix.command()
@click.option("--args", "-a", default="none", type=str, help="A list of JVM args to pass to Cosmic Reach when launched.")
@click.argument("name")
def launch(args: str, name: str):
    """Launches an instance."""
    Instance.from_config_file(name).launch(args.split())


@cosmix.command()
def instances():
    """Shows all instances."""
    if not os.path.exists(paths.INSTANCES) or len(os.listdir(paths.INSTANCES)) <= 0:
        logger.error("No instances found.")
        exit(1)

    for instance_name in os.listdir(paths.INSTANCES):
        instance = Instance.get_or_throw(instance_name)
        s = f" - \u001b[1m{instance.display_name}\u001b[0m"
        if instance.display_name != instance.name:
            s += f" ({instance.name})"
        s += f" \u001b[33m(Version: {instance.version})\u001b[0m"
        if instance.quilt_version is not None:
            s += f" \u001b[34m(Quilt: {instance.quilt_version})\u001b[0m"
        print(s)


@cosmix.command()
@click.argument("name")
def trash(name: str):
    """Trashes an instance."""
    instance = Instance.get_or_throw(name)
    i = input('Are you sure? (y/n) ').lower()
    while True:
        if i == 'n':
            logger.info('Aborted.')
            break
        elif i == 'y':
            send2trash.send2trash(instance.path)
            logger.info("Moved " + name + " to trash.")
            break
        else:
            i = input('Are you sure? (y/n) ').lower()


@cosmix.command()
@click.argument("name")
def info(name: str):
    """Gets info about an instance."""
    i = Instance.get_or_throw(name)
    print(i.display_name + ":")
    print("Instance: " + i.name + (" (modded)" if i.is_modded() else ""))
    print("Path:     " + i.path.replace(os.path.expanduser("~"), "~", 1))
    print("Version:  " + i.version)
    if i.is_modded():
        print("Quilt:    " + i.quilt_version)
        mods = i.get_mods()
        if (l := len(mods)) > 0:
            print(f"{l} Mods:")
            for mod in mods:
                print(f"  - {mod}")


@cosmix.command("add-mod")
@click.argument("name")
@click.argument("mod", type=click.Path(exists = True))
def add_mod(name: str, mod):
    """Adds a jar mod."""
    i = Instance.get_or_throw(name)
    if not i.is_modded():
        logger.error("Instance is not modded")
        exit(1)

    path = os.path.join(i.path, "mods")
    os.makedirs(path, exist_ok = True)
    shutil.copyfile(mod, os.path.join(path, os.path.split(mod)[-1]))

    logger.info("Done.")


@cosmix.command("add-crm1-mod")
@click.option("--repo", "-r", default=None, type=str, help="Provide a CRM-1 repo to use to resolve the mod. Dependencies may still be found using default_repos.")
@click.argument("name")
@click.argument("mod")
def add_crm1_mod(repo: Optional[str], name: str, mod: str):
    """Adds a jar mod via CRM-1."""
    i = Instance.get_or_throw(name)

    if not i.is_modded():
        logger.error("Instance is not modded")
        exit(1)

    path = os.path.join(i.path, "mods")
    os.makedirs(path, exist_ok = True)

    repos = config.get_config()["crm1"]["default_repos"]
    if repo is not None:
        repos.append(repo)

    net.download_crm1_mod(mod, path, repos)
    logger.info("Done.")


@cosmix.command("add-data-mod")
@click.option("--ignore-global-warning", "-I", is_flag = True, default = False, help = "Ignores the global path warning.")
@click.argument("name")
@click.argument("mod", type=click.Path(exists = True))
def add_data_mod(ignore_global_warning: bool, name: str, mod):
    """Adds a data mod."""
    i = Instance.get_or_throw(name)

    if not i.is_modded() and not ignore_global_warning:
        logger.warn("Instance is not modded, this means the data mod will be installed to the GLOBAL Cosmic Reach directory (~/.local/share/cosmic-reach/)")
        logger.warn("Use --ignore-global-warning or -I to ignore this warning.")
        exit(1)

    if i.is_modded():
        path = os.path.join(i.path_to("mods"), "assets")
        os.makedirs(path, exist_ok = True)
        shutil.copytree(mod, path, dirs_exist_ok = True)
    elif ignore_global_warning:
        if not os.path.exists(paths.CR_DIR):
            logger.error("Global Cosmic Reach path does not exist. This should not happen.")
            exit(1)
        path = os.path.join(paths.CR_DIR, "mods", "assets")
        shutil.copytree(mod, path, dirs_exist_ok = True)

    logger.info("Done.")


@cosmix.command("whereis")
@click.argument("name")
def whereis(name: str):
    """Shows the path to an instance."""
    i = Instance.get_or_throw(name)
    logger.info(i.path)


if __name__ == "__main__":
    cosmix()
