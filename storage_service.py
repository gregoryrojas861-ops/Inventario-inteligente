from pathlib import Path

def save_local_file(content: bytes, filename: str, directory="storage"):
    path = Path(directory)
    path.mkdir(parents=True, exist_ok=True)
    target = path / Path(filename).name
    target.write_bytes(content)
    return target
