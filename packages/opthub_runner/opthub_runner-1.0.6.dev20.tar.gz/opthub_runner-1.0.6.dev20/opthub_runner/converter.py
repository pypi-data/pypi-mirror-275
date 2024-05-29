"""This module contains the functions to convert."""

import logging
import math
import sys

LOGGER = logging.getLogger(__name__)


def float_to_json_float(value: object) -> object:  # noqa: PLR0911
    """Convert float values to JSON float values.

    Args:
        value (object): The object consists of float values.

    Returns:
        object: The object consists of json float values.
    """
    if isinstance(value, list):
        return [float_to_json_float(v) for v in value]
    if isinstance(value, dict):
        return {k: float_to_json_float(v) for k, v in value.items()}
    if not isinstance(value, float):
        return value
    if value == math.inf:
        LOGGER.warning("math.inf is converted to sys.float_info.max")
        return sys.float_info.max
    if value == -math.inf:
        LOGGER.warning("-math.inf is converted to -sys.float_info.max")
        return -sys.float_info.max
    if math.isnan(value):
        LOGGER.warning("math.nan is converted to None")
        return None
    return value
