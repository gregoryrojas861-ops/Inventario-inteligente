from pathlib import Path
import shutil
from config import BASE_DIR

def backup_sqlite(destination):
    source = BASE_DIR / "inventory.db"
    if not source.exists():
        raise FileNotFoundError("La base SQLite todavía no existe.")
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    return destination
