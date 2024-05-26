from datetime import date, datetime
from logging import Logger
from typing import Any, Final
from .datetime_pomes import TIMEZONE_LOCAL
from .env_pomes import APP_PREFIX, env_get_str
from .str_pomes import str_sanitize, str_find_whitespace

VALIDATION_MSG_LANGUAGE: Final[str] = env_get_str(f"{APP_PREFIX}_VALIDATION_MSG_LANGUAGE", "en")
VALIDATION_MSG_PREFIX: Final[str] = env_get_str(f"{APP_PREFIX}_VALIDATION_MSG_PREFIX", APP_PREFIX)


def validate_value(attr: str,
                   val: str | int | float,
                   min_val: int = None,
                   max_val: int = None,
                   default: bool | list[Any] = None) -> str:
    """
    Validate *val* according to value, range, or membership in values list, as specified.

    :param attr: the name of the attribute
    :param val: the value to be validated
    :param min_val: if val is a string, specifies its minimum length; otherwise, specifies its minimum value
    :param max_val: if val is a string, specifies its maximum length; otherwise, specifies its maximum value
    :param default: if boolean, requires val to be specified; if list, requires val to be in it
    :return: None if val passes validation, or the corresponding error message otherwise
    """
    # initialize the return variable
    result: str | None = None

    # 'val' can be None, and None can be in 'default'
    if isinstance(default, list):
        if val not in default:
            if not val:
                # 112: Required attribute
                result = validate_format_error(112, f"@{attr}")
            else:
                length: int = len(default)
                if length == 1:
                    # 125: Invalid value {}: must be {}
                    result = validate_format_error(125, val, default[0], f"@{attr}")
                else:
                    # is 'None' or '' the last element in list ?
                    if default[-1] in ("", None):
                        # yes, omit it from the message
                        length -= 1
                    # again, is 'None' or '' the last element in list ?
                    if default[-1] in ("", None):
                        # yes, omit it from the message
                        length -= 1
                    # 126: Invalid value {}: must be one of {}
                    result = validate_format_error(126, val, default[:length], f"@{attr}")
    elif not val:
        if isinstance(default, bool) and default:
            # 112: Required attribute
            result = validate_format_error(112, f"@{attr}")
    elif isinstance(val, str):
        length: int = len(val)
        if min_val is not None and max_val == min_val and length != min_val:
            # 124: Invalid value {}: length must be {}
            result = validate_format_error(124, val, min_val, f"@{attr}")
        elif max_val is not None and max_val < length:
            # 123: Invalid value {}: length longer than {}
            result = validate_format_error(123, val, max_val, f"@{attr}")
        elif min_val is not None and length < min_val:
            # 122: Invalid value {}: length shorter than {}
            result = validate_format_error(122, val, min_val, f"@{attr}")
    elif (min_val is not None and val < min_val) or \
         (max_val is not None and val > max_val):
        if min_val is not None and max_val is not None:
            # 127: Invalid value {}: must be in the range {}
            result = validate_format_error(127, val, [min_val, max_val], f"@{attr}")
        elif min_val is not None:
            # 118: Invalid value {}: must be greater than {}
            result = validate_format_error(118, val, min_val, f"@{attr}")
        else:
            # 117: Invalid value {}: must be less than {}
            result = validate_format_error(117, val, max_val, f"@{attr}")

    return result


def validate_bool(errors: list[str] | None,
                  scheme: dict,
                  attr: str,
                  default: bool = None,
                  mandatory: bool = False,
                  logger: Logger = None) -> bool:
    """
    Validate the boolean value associated with *attr* in *scheme*.

    If provided, this value must be a *bool*, or the string *t*, *true*, *f*, or *false*.

    :param errors: incidental error messages
    :param scheme: dictionary containing the value to be validated
    :param attr: the name of the attribute whose value is being validated
    :param default: default value, if not found
    :param mandatory: specifies whether the value must be provided
    :param logger: optional logger
    :return: the validated value, or None if validation failed
    """
    stat: str | None = None
    pos: int = attr.rfind(".") + 1
    suffix: str = attr[pos:]

    # retrieve the value
    result = scheme.get(suffix)

    # validate it
    if result is None or result == "":
        if default is not None:
            result = default
        elif mandatory:
            # 112: Required attribute
            stat = validate_format_error(112, f"@{attr}")
    elif isinstance(result, str):
        if result.lower() in ["t", "true"]:
            result = True
        elif result.lower() in ["f", "false"]:
            result = False
    elif not isinstance(result, bool):
        # 128: Invalid value {}: must be type {}
        stat = validate_format_error(128, result, "bool", f"@{attr}")

    if stat:
        __validate_log(errors, stat, logger)

    return result


def validate_int(errors: list[str] | None,
                 scheme: dict,
                 attr: str,
                 min_val: int = None,
                 max_val: int = None,
                 default: bool | int | list[int] = None,
                 logger: Logger = None) -> int:
    """
    Validate the *int* value associated with *attr* in *scheme*.

    If provided, this value must be a *int*, or a valid string representation of a *int*.

    :param errors: incidental error messages
    :param scheme: dictionary containing the value to be validated
    :param attr: the attribute associated with the value to be validated
    :param min_val: the minimum value accepted
    :param max_val:  the maximum value accepted
    :param default: if int, specifies the default value;
                    if bool, requires the value to be specified;
                    if list, requires the value to be in it
    :param logger: optional logger
    :return: the validated value, or None if validation failed
    """
    stat: str | None = None
    pos: int = attr.rfind(".") + 1
    suffix: str = attr[pos:]

    # retrieve the value
    result: int | None = scheme.get(suffix)

    # handle the empty string
    if result == "":
        result = None

    # validate it
    if isinstance(result, str) and result.isnumeric():
        result = int(result)
    # bool is subtype of int
    elif result is not None and \
            (isinstance(result, bool) or not isinstance(result, int)):
        # 128: Invalid value {}: must be type {}
        stat = validate_format_error(128, result, "int", f"@{attr}")
    elif isinstance(default, int) and not isinstance(default, bool):
        if result is None:
            result = default
        else:
            stat = validate_value(attr, result, min_val, max_val)
    else:
        stat = validate_value(attr, result, min_val, max_val, default)

    if not stat:
        stat = validate_value(attr, result, min_val, max_val, default)

    if stat:
        __validate_log(errors, stat, logger)

    return result


def validate_float(errors: list[str] | None,
                   scheme: dict,
                   attr: str,
                   min_val: float = None,
                   max_val: float = None,
                   default: bool | int | float | list[float | int] = None,
                   logger: Logger = None) -> float:
    """
    Validate the *float* value associated with *attr* in *scheme*.

    If provided, this value must be a *float*, or a valid string representation of a *float*.

    :param errors: incidental error messages
    :param scheme: dictionary containing the value to be validated
    :param attr: the attribute associated with the value to be validated
    :param min_val: the minimum value accepted
    :param max_val:  the maximum value accepted
    :param default: if float, specifies the default value;
                    if bool, requires the value to be specified;
                    if list, requires the value to be in it
    :param logger: optional logger
    :return: the validated value, or None if validation failed
    """
    stat: str | None = None
    pos: int = attr.rfind(".") + 1
    suffix: str = attr[pos:]

    # retrieve the value
    result: float | None = scheme.get(suffix)

    # handle the empty string
    if result == "":
        result = None

    # validate it
    if isinstance(result, str) and result.replace(".", "", 1).isnumeric():
        result = float(result)
    elif result is not None and not isinstance(result, int) and not isinstance(result, float):
        # 128: Invalid value {}: must be type {}
        stat = validate_format_error(128, result, "float", f"@{attr}")
    else:
        # bool é subtipo de int
        if isinstance(result, int) and not isinstance(result, bool):
            result = float(result)
        if isinstance(default, float):
            if result is None:
                result = default
            else:
                stat = validate_value(attr, result, min_val, max_val)
        else:
            stat = validate_value(attr, result, min_val, max_val, default)

    if not stat:
        stat = validate_value(attr, result, min_val, max_val, default)

    if stat:
        __validate_log(errors, stat, logger)

    return result


def validate_str(errors: list[str] | None,
                 scheme: dict,
                 attr: str,
                 min_length: int = None,
                 max_length: int = None,
                 default: bool | str | list[str] = None,
                 logger: Logger = None) -> str:
    """
    Validate the *str* value associated with *attr* in *scheme*.

    If provided, this value must be a *str*.

    :param errors: incidental error messages
    :param scheme: dictionary containing the value to be validated
    :param attr: the attribute associated with the value to be validated
    :param min_length: the minimum length accepted
    :param max_length:  the maximum length accepted
    :param default: if str, specifies the default value;
                    if bool, requires the value to be specified;
                    if list, requires the value to be in it
    :param logger: optional logger
    :return: the validated value, or None if validation failed
    """
    stat: str | None = None
    pos: int = attr.rfind(".") + 1
    suffix: str = attr[pos:]

    # obtain and validate the value
    result: str | None = scheme.get(suffix)
    if result and not isinstance(result, str):
        # 128: Invalid value {}: must be type {}
        stat = validate_format_error(128, result, "str", f"@{attr}")
    elif isinstance(default, str):
        if result is None:
            result = default
        else:
            stat = validate_value(attr, result, min_length, max_length)
    else:
        stat = validate_value(attr, result, min_length, max_length, default)

    if stat:
        result = None
        __validate_log(errors, stat, logger)

    return result


def validate_date(errors: list[str] | None,
                  scheme: dict,
                  attr: str,
                  day_first: bool = False,
                  default: bool | date = None,
                  logger: Logger = None) -> date:
    """
    Validate the *date* value associated with *attr* in *scheme*.

    If provided, this value must be a *date*, or a valid string representation of a *date*.

    :param errors: incidental error messages
    :param scheme: dictionary containing the value to be validated
    :param attr: the attribute associated with the value to be validated
    :param day_first: indicates that the day precedes the month in the string representing the date
    :param default: if date, specifies the default value;
                    if bool, requires the value to be specified
    :param logger: optional logger
    :return: the validated value, or None if validation failed
    """
    # import needed module
    from .datetime_pomes import date_parse

    # initialize the return variable
    result: date | None = None

    stat: str | None = None
    pos: int = attr.rfind(".") + 1
    suffix: str = attr[pos:]

    # obtain and validate the value
    date_str: str = scheme.get(suffix)
    if date_str:
        result = date_parse(date_str, dayfirst=day_first)
        if not result:
            # 121: Invalid value {}
            stat = validate_format_error(121, date_str, f"@{attr}")
        elif result > datetime.now(TIMEZONE_LOCAL).date():
            # 129: Invalid value {}: date is later than the current date
            stat = validate_format_error(129, date_str, f"@{attr}")
    elif isinstance(default, bool) and default:
        # 112: Required attribute
        stat = validate_format_error(112, f"@{attr}")
    elif isinstance(default, date):
        result = default

    if stat:
        __validate_log(errors, stat, logger)

    return result


def validate_datetime(errors: list[str] | None,
                      scheme: dict,
                      attr: str,
                      day_first: bool = True,
                      default: bool | datetime = None,
                      logger: Logger = None) -> datetime:
    """
    Validate the *datetime* value associated with *attr* in *scheme*.

    If provided, this value must be a *date*, or a valid string representation of a *date*.

    :param errors: incidental error messages
    :param scheme: dictionary containing the value to be validated
    :param attr: the attribute associated with the value to be validated
    :param day_first: indicates that the day precedes the month in the string representing the date
    :param default: if datetime, specifies the default value;
                    if bool, requires the value to be specified
    :param logger: optional logger
    :return: the validated value, or None if validation failed
    """
    # import needed module
    from .datetime_pomes import datetime_parse

    # initialize the return variable
    result: datetime | None = None

    stat: str | None = None
    pos: int = attr.rfind(".") + 1
    suffix: str = attr[pos:]

    # obtain and validate the value
    date_str: str = scheme[suffix]
    if date_str:
        result = datetime_parse(date_str, dayfirst=day_first)
        if not result:
            # 121: Invalid value {}
            stat = validate_format_error(121, date_str, f"@{attr}")
        elif result > datetime.now(TIMEZONE_LOCAL):
            # 129: Invalid value {}: date is later than the current date
            stat = validate_format_error(129, date_str, f"@{attr}")
    elif isinstance(default, bool) and default:
        # 112: Required attribute
        stat = validate_format_error(112, f"@{attr}")
    elif isinstance(default, datetime):
            result = default

    if stat:
        __validate_log(errors, stat, logger)

    return result


def validate_ints(errors: list[str] | None,
                  scheme: dict,
                  attr: str,
                  min_val: int = None,
                  max_val: int = None,
                  mandatory: bool = False,
                  logger: Logger = None) -> list[int]:
    """
    Validate the list of *int* values associated with *attr* in *scheme*.

    If provided, this list must contain *ints*, or valid string representations of *ints*.

    :param errors: incidental error messages
    :param scheme: dictionary containing the list of values to be validated
    :param attr: the attribute associated with the list of values to be validated
    :param min_val: the minimum value accepted
    :param max_val:  the maximum value accepted
    :param mandatory: whether the list of values must be provided
    :param logger: optional logger
    :return: the list of validated values, or None if validation failed
    """
    # initialize the return variable
    result: list[Any] | None = None

    stat: str | None = None
    pos: int = attr.rfind(".") + 1
    suffix: str = attr[pos:]
    try:
        values: list[Any] = scheme[suffix]
        if isinstance(values, list):
            result = []
            if len(values) > 0:
                for inx, value in enumerate(values):
                    result.append(value)
                    if isinstance(value, int):
                        stat = validate_value(f"@{attr}[{inx+1}]", value, min_val, max_val)
                    else:
                        # 128: Invalid value {}: must be type {}
                        stat = validate_format_error(128, value, "int", f"@{attr}[{inx+1}]")
            elif mandatory:
                # 112: Required attribute
                stat = validate_format_error(112, f"@{attr}")
        else:
            # 128: Invalid value {}: must be type {}
            stat = validate_format_error(128, result, "list", f"@{attr}")
    except (KeyError, TypeError):
        if mandatory:
            # 112: Required attribute
            stat = validate_format_error(112, f"@{attr}")

    if stat:
        __validate_log(errors, stat, logger)

    return result


def validate_strs(errors: list[str] | None,
                  scheme: dict,
                  attr: str,
                  min_length: int,
                  max_length: int,
                  mandatory: bool = False,
                  logger: Logger = None) -> list[str]:
    """
    Validate the list of *str* values associated with *attr* in *scheme*.

    If provided, this list must contain *strs*.

    :param errors: incidental error messages
    :param scheme: dictionary containing the list of values to be validated
    :param attr: the attribute associated with the list of values to be validated
    :param min_length: the minimum length accepted
    :param max_length:  the maximum length accepted
    :param mandatory: whether the list of values must be provided
    :param logger: optional logger
    :return: the list of validated values, or None if validation failed
    """
    # initialize the return variable
    result: list[Any] | None = None

    stat: str | None = None
    pos: int = attr.rfind(".") + 1
    suffix: str = attr[pos:]
    try:
        values: list[Any] = scheme[suffix]
        if isinstance(values, list):
            result = []
            if len(values) > 0:
                for inx, value in enumerate(values):
                    result.append(value)
                    if isinstance(value, str):
                        stat = validate_value(f"@{attr}[{inx+1}]", value, min_length, max_length)
                    else:
                        # 128: Invalid value {}: must be type {}
                        stat = validate_format_error(128, value, "str", f"@{attr}[{inx+1}]")
            elif mandatory:
                # 112: Required attribute
                stat = validate_format_error(112, f"@{attr}")
        else:
            # 128: Invalid value {}: must be type {}
            stat = validate_format_error(128, result, "list", f"@{attr}")
    except (KeyError, TypeError):
        if mandatory:
            # 112: Required attribute
            stat = validate_format_error(112, f"@{attr}")

    if stat:
        __validate_log(errors, stat, logger)

    return result


def validate_format_error(error_id: int,
                          *args: Any) -> str:
    """
    Format and return the error message identified by *err_id* in the standard messages list.

    The message is built from the message element in the standard messages list, identified by *err_id*.
    The occurrences of '{}' in the element are sequentially replaced by the given *args*.

    :param error_id: the identification of the message element
    :param args: optional arguments to format the error message with
    :return: the formatted error message
    """
    # retrieve the standard validation messages list
    match VALIDATION_MSG_LANGUAGE:
        case "en":
            from .validation_msgs import _ERR_MSGS_EN
            err_msgs = _ERR_MSGS_EN
        case "pt":
            from .validation_msgs import _ERR_MSGS_PT
            err_msgs = _ERR_MSGS_PT
        case _:
            err_msgs = {}

    # initialize the return variable
    result: str = ""
    if VALIDATION_MSG_PREFIX:
        result += VALIDATION_MSG_PREFIX + str(error_id) + ": "
    result += err_msgs.get(error_id) or ""

    # apply the provided arguments
    for arg in args:
        if arg is None:
            result = result.replace(" {}", "", 1)
        elif not result or (isinstance(arg, str) and arg.startswith("@")):
            result += " " + arg
        elif isinstance(arg, str) and arg.find(" ") > 0:
            result = result.replace("{}", arg, 1)
        else:
            result = result.replace("{}", f"'{arg}'", 1)

    return result


def validate_format_errors(errors: list[str]) -> list[dict]:
    """
    Build and return a list of dicts from the list of errors *errors*.

    Each element in *errors* is encoded as a *dict*.
    This list is tipically used in a returning *JSON* string.

    :param errors: the list of errors to build the list of dicts with
    :return: the built list
    """
    # initialize the return variable
    result: list[dict] = []

    # extract error code, description, and attribute from text
    for error in errors:

        # locate the last indicator for the attribute
        pos = error.rfind("@")

        # is there a whitespace in the attribute's name ?
        if pos > 0 and str_find_whitespace(error[pos:]) > 0:
            # yes, disregard the attribute
            pos = -1

        # was the attribute's name found ?
        if pos == -1:
            # no
            out_error: dict = {}
            desc: str = error
        else:
            # yes
            term: str = "attribute" if VALIDATION_MSG_LANGUAGE == "en" else "atributo"
            out_error: dict = {term: error[pos + 1:]}
            desc: str = error[:pos - 1]

        # does the text contain an error code ?
        if VALIDATION_MSG_PREFIX and desc.startswith(VALIDATION_MSG_PREFIX):
            # yes
            term: str = "code" if VALIDATION_MSG_LANGUAGE == "en" else "codigo"
            pos: int = desc.find(":")
            out_error[term] = desc[0:pos]
            desc = desc[pos+2:]

        term: str = "description" if VALIDATION_MSG_LANGUAGE == "en" else "descricao"
        out_error[term] = desc
        result.append(out_error)

    return result


def validate_unformat_errors(errors: list[dict | str]) -> list[str]:
    """
    Extract and return the list of errors used to build the list of dicts *errors*.

    :param errors: the list of dicts to extract the errors from
    :return: the built list
    """
    # initialize the return variable
    result: list[str] = []

    # define the dictionary keys
    name: str = "code" if VALIDATION_MSG_LANGUAGE == "en" else "codigo"
    desc: str = "description" if VALIDATION_MSG_LANGUAGE == "en" else "descricao"

    # traverse the list of dicts
    for error in errors:
        if isinstance(error, dict):
            desc: str = str_sanitize(error.get(desc) or "''")
            result.append(f"{error.get(name)}: {desc}")
        else:
            result.append(error)

    return result


def __validate_log(errors: list[str],
                   err_msg: str,
                   logger: Logger) -> None:
    """
    LOg *err_msg* using *logger*, and add it to the error messages list *errors*.

    :param errors: the error messages list
    :param err_msg: the message to log
    :param logger: the logger
    """
    if logger:
        logger.error(err_msg)
    if isinstance(errors, list):
        errors.append(err_msg)
