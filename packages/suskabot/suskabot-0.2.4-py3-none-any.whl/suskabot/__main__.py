import logging
import sys

from typing import Optional
from contextlib import suppress

from suskabot.config import config

from suskabot.app import app


logger = logging.getLogger()


# somehow pydantic raises an attribute error when I'm trying to access config.Config for the type hint
# removing the type hint solves the issue, but I'd rather just suppress the pydantic error
with suppress(AttributeError):
    config: Optional[config.Config] = config.load_config()
if not config:
    logger.error("Couldn't load config file")
    sys.exit(1)

app = app.App(config)

app.run()
