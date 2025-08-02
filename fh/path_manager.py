from pathlib import Path


class PathManager:
    def __init__(self):
        self.root_dir = Path(__file__).parent.parent.resolve()
        self.data_dir = self.root_dir / "data"
        self.storage_dir = self.root_dir / "storage"

        self._create_dirs()

    def _create_dirs(self):
        self.data_dir.mkdir(exist_ok=True)
        self.storage_dir.mkdir(exist_ok=True)

    def get_data_path(self, filename: str) -> Path:
        return self.data_dir / filename

    def get_storage_path(self, filename: str) -> Path:
        return self.storage_dir / filename
