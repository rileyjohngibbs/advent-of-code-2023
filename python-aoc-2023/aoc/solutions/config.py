import os

from pydantic_settings import BaseSettings, SettingsConfigDict

here = os.path.dirname(__file__)


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=os.path.join(here, "..", ".env"))
    puzzle_input_dir: str = os.path.join(here, "..", "..", "..", "inputs")
    example_input_dir: str = os.path.join(here, "..", "..", "..", "examples")
    test: bool = False
    time_execution: bool = False

    @property
    def input_dir(self) -> str:
        return self.example_input_dir if self.test else self.puzzle_input_dir


config = Config()
