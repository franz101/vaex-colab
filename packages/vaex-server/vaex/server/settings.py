
from typing import Dict
from pydantic import Field
import pydantic
import vaex.config
from ..minisettings import BaseSettings, Field


class Settings(BaseSettings):
    '''Configuration options for the FastAPI server'''
    # vaex_config_file: str = "vaex-server.json"
    add_example: bool = Field(True, title="Add example dataset")
    # vaex_config: dict = None
    graphql: bool = Field(False, title="Add graphql endpoint")
    files: Dict[str, str] = Field(default_factory=dict, title="Mapping of name to path")
    # TODO[pydantic]: The `Config` class inherits from another class, please create the `model_config` manually.
    # Check https://docs.pydantic.dev/dev-v2/migration/#changes-to-config for more information.
    class Config(vaex.config.ConfigDefault):
        env_file = '.env'
        env_file_encoding = 'utf-8'
        env_prefix = 'vaex_server_'
        # secrets_dir = '/run/secrets'
