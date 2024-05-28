from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional

T = TypeVar("T") # openapi client instance
C = TypeVar("C") # Config type

class PineconePlugin(ABC, Generic[T, C]):
    """
    The optional openapi_client parameter passed if the PluginMetadata passed
    to the plugin constructor has an openapi_client_class attribute.
    """
    @abstractmethod
    def __init__(self, config: C, openapi_client: Optional[T] = None):
        pass
