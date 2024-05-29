from pathlib import Path


def _split_protocol(url: str) -> tuple[set[str], str]:
    if "://" in url:
        parts = str(url).split("://")
        protocol = parts[0]
        path = parts[1]
        if not protocol:
            protocol = "file"
    else:
        protocol = "file"
        path = url
    return set(protocol.split("::")), path


def _is_s3_url(url: str) -> bool:
    protocols, path = _split_protocol(url)
    return "s3" in protocols


def fix_url(url: str) -> str:
    protocols, url = _split_protocol(url)
    is_zip = "zip" in protocols or Path(str(url)).suffix == ".zip"
    if is_zip:
        protocols.add("zip")
    valid_protocols = []
    for p in ["zip", "s3"]:
        if p in protocols:
            valid_protocols.append(p)
            protocols.remove(p)
    protocol = "::".join(valid_protocols + list(protocols))
    return f"{protocol}://{url}"
