from typing import Type, cast, Callable

from nestipy.metadata import SetMetadata
from peewee import Model as BaseModel

from .peewee_meta import PeeweeMetadata


def Model() -> Callable[[Type], BaseModel]:
    decorator = SetMetadata(PeeweeMetadata.ModelMeta, True)

    def class_decorator(cls: Type) -> BaseModel:
        cls = decorator(cls)
        return cast(BaseModel, cls)

    return class_decorator
