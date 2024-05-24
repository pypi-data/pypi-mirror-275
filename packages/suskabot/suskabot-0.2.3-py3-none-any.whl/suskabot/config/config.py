import logging
import os
import enum
from typing import Self, Dict, Optional

import telegram.constants
import pydantic
import dotenv

from suskabot.utils import utils


logger = logging.getLogger()


class VideoResolution(enum.Enum):
    RES_144 = 144
    RES_240 = 240
    RES_360 = 360
    RES_480 = 480
    RES_720 = 720
    RES_1080 = 1080
    RES_1440 = 1440
    RES_2160 = 2160


def get_lowest_resolution_value() -> int:
    return VideoResolution.RES_144.value


def get_highest_resolution_value() -> int:
    return VideoResolution.RES_2160.value


# it is assumed that every valid configuration is type annotated
# I tried really hard, but there's no easier way to achieve the same functionality without repeating config names
def get_config_attributes() -> set[str]:
    return vars(Config)['__annotations__'].keys()


# every configuration must be type annotated, else it won't be loaded!!!
class Config(pydantic.BaseModel):
    tg_bot_api_token: str

    comma_separated_translation_services: str
    user_language: str
    default_language_to_translate_to: str

    minimum_video_resolution: int
    maximum_video_resolution: int
    file_size_limit_mb: int
    save_to_drive: bool

    tg_bot_api_token = pydantic.Field(
        pattern=r"^[0-9]+:[a-zA-Z0-9_-]+$"
    )

    comma_separated_translation_services = pydantic.Field(
        default="google,yandex,bing,argos",
        pattern=r"^([a-zA-Z]+,?)+"
    )
    user_language = pydantic.Field(
        default="ru",
        pattern=r"^[^-]{2,3}(-[^-]{2,3})?(-[^-]{2,3})?$"
    )
    default_language_to_translate_to = pydantic.Field(
        default="en",
        pattern=r"^[^-]{2,3}(-[^-]{2,3})?(-[^-]{2,3})?$",
    )

    # right now only progressive videos are supported, so video quality is 720p max.
    # it also looks like 360p and 720p are the only available options
    minimum_video_resolution = pydantic.Field(
        default=get_lowest_resolution_value(),
    )
    maximum_video_resolution = pydantic.Field(
        default=get_highest_resolution_value(),
    )

    @pydantic.field_validator("maximum_video_resolution", "minimum_video_resolution")
    def validate_resolution(cls, v):
        valid_video_resolutions = [res.value for res in VideoResolution]
        assert v in valid_video_resolutions, ("this does not look like a valid resolution. "
                                              f"supported resolutions: {valid_video_resolutions}")
        return v

    @pydantic.model_validator(mode='after')
    def check_if_valid_video_resolution_preferences(self) -> Self:
        if self.minimum_video_resolution > self.maximum_video_resolution:
            raise ValueError("minimum video resolution can't be higher than maximum video resolution")
        if self.minimum_video_resolution > 720:
            logger.warning("Since only progressive videos are supported right now,"
                           " 720p is the maximum possible resolution")
        return self

    # setting the limit higher than the default will break telegram api controller!
    file_size_limit_mb = pydantic.Field(
        default=utils.bytes_to_megabytes(
            telegram.constants.FileSizeLimit.FILESIZE_UPLOAD.value
        ),
        gt=0,
        validate_default=True
    )

    save_to_drive = pydantic.Field(
        default=True
    )

    # TODO: having a config for yt video downloads directory seems like a nice idea


def load_config() -> Optional[Config]:
    """
    Loads configurations from os.environ first and /project_name/config/.env file second,
    then validates them using pydantic

    :return: Config instance or None

    :raises pydantic.ValidationError: If some configurations are invalid
    """
    env_file_config: Dict[str, str | None] = dotenv.dotenv_values("./suskabot/config/.env")

    config_data: Dict[str, str | None] = {}

    configurations: set[str] = get_config_attributes()
    configuration: str
    for configuration in configurations:
        configuration_value: str | None
        configuration_upper: str = configuration.upper()

        logger.debug(f"Getting {configuration}..")

        if configuration_upper in os.environ and os.environ.get(configuration_upper) is not None:
            configuration_value = os.environ[configuration_upper]
            logger.debug(f"Got {configuration} from environ")

        elif configuration_upper in env_file_config and env_file_config.get(configuration_upper) != "":
            configuration_value = env_file_config[configuration_upper]
            logger.debug(f"Got {configuration} from .env")

        else:
            logger.debug(f"Couldn't find {configuration} anywhere, will try to use the default value")
            continue

        config_data[configuration] = configuration_value
        logger.info(f"{configuration} set to {configuration_value}")

    config: Config = Config(**config_data)

    return config
