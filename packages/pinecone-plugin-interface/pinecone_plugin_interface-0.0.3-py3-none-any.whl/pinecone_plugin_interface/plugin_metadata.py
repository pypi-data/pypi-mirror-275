from collections import namedtuple
from typing import NamedTuple
from .pinecone_plugin import PineconePlugin

class PluginMetadata(NamedTuple):
    """
    What object are you trying to extend with a plugin? For initial use cases, this
    will always be 'Pinecone', which refers to the Pinecone class in the python sdk.
    """
    target_object: str

    """
    This is the attribute of the target object that will hold a reference to the 
    instantiated plugin implementation.

    For example, you could have this plugin implementation:

    ```
    # pinecone_plugin/my_plugin/__init__.py
    class MyPlugin(PineconePlugin):
        def __init__(self, client_builder, config):
            pass

        def feature(self):
            return "feature-response"
    
    __installables__ = [PluginMetadata('Pinecone', 'foo', MyPlugin)]
    ```

    After installation in the python sdk, this plugin would be accessible like so:

    ```
    from pinecone import Pinecone

    pc = Pinecone(api_key='key')
    pc.foo.feature()  # returns 'feature-response'
    ```
    """
    namespace: str

    """
    This should be a class extending the PineconePlugin abstract base class. This class should expose
    various feature methods with UX in mind, since it's the surface end-users will
    interact with. Often it will be a wrapper around a generated OpenAPI client object.
    """
    implementation_class: PineconePlugin

    """
    This value will be used to set an appropriate X-Pinecone-API-Version header on
    the plugin's requests. It will only be used when installing plugins that 
    include the openapi_client_class attribute. 
    
    If you are not building around an OpenAPI generated client class, you can leave this as an 
    empty string and it will be your responsibility to make sure an appropriate 
    version header is sent with every request.
    """
    api_version: str

    """
    If the plugin is built on top of a generated OpenAPI client class, this should be the
    OpenAPI client class that the plugin uses. If you are not using an OpenAPI client,
    you can leave this as None.

    Providing this value allows us to automatically instantiate and configure all openapi client
    objects in a consistent way across the entire SDK so that you get the benefit of features like
    proxy configuration for free in your plugin.
    """
    openapi_client_class: type