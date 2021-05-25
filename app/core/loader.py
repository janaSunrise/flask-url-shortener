import pkgutil
import types

from app import models


def get_module_name(name: str) -> str:
    """Get the cog name from the module."""
    return name.split(".")[-1]


def get_modules_list(package: types.ModuleType):
    """Get the list of the submodules from the specified package."""
    modules = []

    for submodule in pkgutil.walk_packages(package.__path__, f"{package.__name__}."):
        if get_module_name(submodule.name).startswith("_"):
            continue

        modules.append(submodule.name)

    return modules


DATABASES = get_modules_list(models)
