from dataclasses import dataclass, field
from typing import Literal
from peewee import Model as BaseModel

from nestipy.dynamic_module import ConfigurableModuleBuilder, DynamicModule


@dataclass
class PeeweeConfig:
    driver: Literal['sqlite', 'mysql', 'postgres']
    host: str = ''
    port: int = 0
    user: str = ''
    password: str = 3306
    database: str = ''
    models: list[BaseModel] = field(default_factory=lambda: [])
    # options: dict = field(default_factory=lambda: {})


def extra_callback(dynamic_module: DynamicModule, extras: dict):
    if extras.get('is_global') is not None:
        dynamic_module.is_global = extras.get('is_global')


ConfigurableModuleClass, PEEWEE_DB_CONFIG = ConfigurableModuleBuilder[PeeweeConfig]() \
    .set_method('for_root') \
    .set_extras({'is_global': True}, extra_callback) \
    .build()
