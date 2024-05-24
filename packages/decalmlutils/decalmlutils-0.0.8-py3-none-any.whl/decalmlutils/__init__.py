# ruff: noqa: E402, F403
# make sure warnings are imported
import warnings

from .io.misc import *  # noqa: F401, F403
from .logging_utils import setup_default_logging

# always show deprecation warnings
warnings.simplefilter("always", DeprecationWarning)


__version__ = "0.0.8"


setup_default_logging()
