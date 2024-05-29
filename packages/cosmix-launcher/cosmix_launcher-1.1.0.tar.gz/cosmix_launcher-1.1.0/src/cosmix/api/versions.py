from . import net


__all__ = (
    "LATEST_REACH_URL",
    "LATEST_QUILT_URL",
    "SOURCES",
    "get_latest_of",
    "get_version_or_latest_of",
)


LATEST_REACH_URL = "https://raw.githubusercontent.com/CRModders/CosmicArchive/main/versions.json"
LATEST_QUILT_URL = "https://codeberg.org/api/v1/repos/CRModders/cosmic-quilt/releases/latest"
SOURCES = {
    # TODO: Use `alpha`, `beta`, `release`, or whatever once CR changes latest versions
    "reach": lambda: net.get_json(LATEST_REACH_URL)["latest"]["pre_alpha"],
    "quilt": lambda: net.get_json(LATEST_QUILT_URL)["tag_name"],
}


def get_latest_of(source: str) -> str:
    return SOURCES[source]()

def get_version_or_latest_of(source: str, version: str) -> str:
    return version if version != "latest" else get_latest_of(source)
