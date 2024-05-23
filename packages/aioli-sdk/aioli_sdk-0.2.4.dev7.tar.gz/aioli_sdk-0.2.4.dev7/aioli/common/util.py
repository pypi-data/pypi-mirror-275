# © Copyright 2023-2024 Hewlett Packard Enterprise Development LP
import functools
import os
import pathlib
import platform
import random
import warnings
from argparse import Namespace
from typing import (
    Any,
    Callable,
    Dict,
    Iterator,
    List,
    Optional,
    Sequence,
    TypeVar,
    Union,
    cast,
    overload,
)

T = TypeVar("T")


def sizeof_fmt(val: Union[int, float]) -> str:
    val = float(val)
    for unit in ("", "K", "M", "G", "T", "P", "E", "Z"):
        if abs(val) < 1024.0:
            return "%3.1f%sB" % (val, unit)
        val /= 1024.0
    return "%.1f%sB" % (val, "Y")


def get_default_controller_address() -> str:
    return os.environ.get(
        "AIOLI_CONTROLLER", os.environ.get("AIOLI_CONTROLLER_ADDR", "localhost:8080")
    )


def get_aioli_username_from_env() -> Optional[str]:
    return os.environ.get("AIOLI_USER")


def get_aioli_user_token_from_env() -> Optional[str]:
    return os.environ.get("AIOLI_USER_TOKEN")


def get_aioli_password_from_env() -> Optional[str]:
    return os.environ.get("AIOLI_PASS")


def debug_mode() -> bool:
    return os.getenv("AIOLI_DEBUG", "").lower() in ("true", "1", "yes")


def preserve_random_state(fn: Callable) -> Callable:
    """A decorator to run a function with a fork of the random state."""

    @functools.wraps(fn)
    def wrapped(*arg: Any, **kwarg: Any) -> Any:
        state = random.getstate()
        try:
            return fn(*arg, **kwarg)
        finally:
            random.setstate(state)

    return wrapped


def get_config_path() -> pathlib.Path:
    if os.environ.get("AIOLI_DEBUG_CONFIG_PATH"):
        return pathlib.Path(os.environ["AIOLI_DEBUG_CONFIG_PATH"])

    system = platform.system()
    if "Linux" in system and "XDG_CONFIG_HOME" in os.environ:
        config_path = pathlib.Path(os.environ["XDG_CONFIG_HOME"])
    elif "Darwin" in system:
        config_path = pathlib.Path.home().joinpath("Library").joinpath("Application Support")
    elif "Windows" in system and "LOCALAPPDATA" in os.environ:
        config_path = pathlib.Path(os.environ["LOCALAPPDATA"])
    else:
        config_path = pathlib.Path.home().joinpath(".config")

    return config_path.joinpath("aioli")


U = TypeVar("U", bound=Callable[..., Any])


def deprecated(message: Optional[str] = None) -> Callable[[U], U]:
    def decorator(func: U) -> U:
        @functools.wraps(func)
        def wrapper_deprecated(*args: Any, **kwargs: Any) -> Any:
            warning_message = (
                f"{func.__name__} is deprecated and will be removed in a future version."
            )
            if message:
                warning_message += f" {message}."
            warnings.warn(warning_message, category=DeprecationWarning, stacklevel=2)
            return func(*args, **kwargs)

        return cast(U, wrapper_deprecated)

    return decorator


def prepend_protocol(host: str) -> str:
    host = only_prepend_protocol(host)
    return f"{host}/api/v1"


def only_prepend_protocol(host: str) -> str:
    # If neither http nor https is specified, supply the default of http.
    if not (host.startswith("http://") or host.startswith("https://")):
        host = f"http://{host}"
    return host


@overload
def chunks(lst: str, chunk_size: int) -> Iterator[str]:
    ...


@overload
def chunks(lst: Sequence[T], chunk_size: int) -> Iterator[Sequence[T]]:
    ...


def chunks(
    lst: Union[str, Sequence[T]], chunk_size: int
) -> Union[Iterator[str], Iterator[Sequence[T]]]:
    """
    Collect data into fixed-length chunks or blocks.  Adapted from the
    itertools documentation recipes.

    e.g. chunks('ABCDEFG', 3) --> ABC DEF G
    """
    for i in range(0, len(lst), chunk_size):
        yield lst[i : i + chunk_size]


def launch_dashboard(args: Namespace, dashboard_uri: Optional[str]) -> None:
    import webbrowser

    url = f"{only_prepend_protocol(args.controller)}{dashboard_uri}"
    if not webbrowser.open(url):
        print(f"Failed to open a browser window. Manually open the dashboard using: {url}")


def construct_environment(args: Namespace) -> Dict[str, str]:
    environment: Dict[str, str] = {}
    if args.env is None:
        return environment

    for entry in args.env:
        # split to name & value
        the_split = entry.split("=", maxsplit=1)
        name: str = the_split[0]
        value: str = ""
        if len(the_split) > 1:
            value = the_split[1]
        environment[name] = value
    return environment


def construct_arguments(args: Namespace) -> List[str]:
    arguments: List[str] = []
    if args.arg is None:
        return arguments

    for entry in args.arg:
        arguments.append(entry.strip())
    return arguments
