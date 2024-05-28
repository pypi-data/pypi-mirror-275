from nestipy.common import Module

from .config_builder import ConfigurableModuleClass
from .config_service import ConfigService


@Module(
    providers=[
        ConfigService
    ],
    exports=[
        ConfigService
    ],
)
class ConfigModule(ConfigurableModuleClass):
    ...
