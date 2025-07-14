import json, pathlib

from .settings import params


def from_local_config(path: pathlib.Path) -> params:
    config_path = path / "clic_config.json"
    with config_path.open("r") as f:
        data = json.load(f)

    s = params(
        comment_symbol=data["comment_symbol"],
        file_extension=data["file_extension"],
        count_comments=data["count_comments"],
        count_whitespaces=data["count_whitespaces"],
    )
    return s


def write_base_config(path: pathlib.Path) -> None:
    # FIXME: possible to serialize params class to automatically adapt defaults?
    config = {
        "comment_symbol": "",
        "file_extension": "",
        "count_comments": False,
        "count_whitespaces": False,
    }
    with path.open("w") as f:
        json.dump(config, f)
    pass
