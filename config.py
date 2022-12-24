import json
from pathlib import Path

import data
from models.configs import ConfigsModel


class Config:

    default_config_file_path = Path("./config.json").resolve()
    configs = ConfigsModel()

    @classmethod
    def __load_configs(cls, config_file_path: Path | None = None):
        with open(file=config_file_path, mode="r") as config_file:
            config_data = json.load(fp=config_file)
        cls.configs = ConfigsModel(**config_data)

    @classmethod
    def configure(cls, config_file_path: Path | None = None):
        if config_file_path is None:
            config_file_path = cls.default_config_file_path
        cls.__load_configs(config_file_path=config_file_path)
        data.populate_with_n_random_books(
            n_books=cls.configs.n_books)
