import inspect
from dataclasses import asdict
from typing import Type, Annotated
from nestipy.common import Module
from nestipy.dynamic_module import NestipyModule
from nestipy.ioc import Inject
from nestipy.metadata import Reflect
from peewee import Model, Database, SqliteDatabase, MySQLDatabase, PostgresqlDatabase

from .peewee_builder import ConfigurableModuleClass, PEEWEE_DB_CONFIG, PeeweeConfig
from .peewee_meta import PeeweeMetadata


@Module()
class PeeweeModule(ConfigurableModuleClass, NestipyModule):
    _db: Database
    _config: Annotated[PeeweeConfig, Inject(PEEWEE_DB_CONFIG)]
    _models: list = []
    _peewee_models: list = []

    async def on_startup(self):
        config_dict = asdict(self._config)
        del config_dict['driver']
        match self._config.driver:
            case 'sqlite':
                self._db = SqliteDatabase(**config_dict)
            case 'postgres':
                self._db = PostgresqlDatabase(**config_dict)
            case _:
                self._db = MySQLDatabase(**config_dict)
        self._setup_model()
        await self.on_shutdown()
        self._db.connect()
        self._db.create_tables(self._peewee_models)

    async def on_shutdown(self):
        if not self._db.is_closed():
            self._db.close()

    @classmethod
    def for_feature(cls, *models: Model):
        for m in models:
            if Reflect.get_metadata(m, PeeweeMetadata.ModelMeta, False) and m not in cls._models:
                cls._models.append(m)
        return cls

    def _setup_model(self):
        db = self._db

        class BaseModel(Model):
            class Meta:
                database = db

        self._setup_base_class(BaseModel)

    def _setup_base_class(self, base: Type):
        for model in self._models:
            properties = {"__module__": model.__module__, }
            for name, value in inspect.getmembers(model):
                if not name.startswith('__'):
                    properties[name] = value
            peewee_model = type(model.__name__, (base,), properties)
            new_class_member = inspect.getmembers(peewee_model)
            for name, value in new_class_member:
                if not name.startswith('__'):
                    setattr(model, name, value)
            globals()[model.__name__] = peewee_model
            self._peewee_models.append(peewee_model)
