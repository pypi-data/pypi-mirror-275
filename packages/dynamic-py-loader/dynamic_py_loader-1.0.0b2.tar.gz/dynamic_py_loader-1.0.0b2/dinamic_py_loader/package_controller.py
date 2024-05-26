from os import path, walk, listdir
from .module_controller import ModuleController
from pathlib import Path


def _path_exists(path: Path | str):
    if not path:
        raise ImportError("Path wasn't specified.")


def _check_is_package(path: Path | str):
        for root, _, files in walk(path):   # It can work with Path
            for file in files:
                if file.endswith('.py'):
                    return True
        return False


class PackageController():
    '''
    Stores dynamically loaded package, can be empty and reloaded.
    ! Warning: relative path doesn't work properly because of realpath problem.
    '''

    def __init__(self, pack_path: Path | str | None = None, strict_load=False):
        '''
        :param pack_path: *Path* object from *pathlib* or str path, should be absolute, can be None;
        :param strict_load: if is True only __init__py imported elements will be proceeded;
        '''

        self.name = None
        self.path = None
        self.modules = {}
        self.packages = {}
        self.init = None

        if pack_path:
            pack_path = str(Path(pack_path).resolve())

            if not path.exists(pack_path):
                raise ImportError(f"Given package path doesn't exist: {pack_path}.")
            if not path.isdir(pack_path):
                raise ImportError(f"Given package path isn't a dir: {pack_path}.")

            self.name = path.basename(pack_path)
            self.path = pack_path

            init_path = path.join(pack_path, '__init__.py')
            if path.isfile(init_path):
                self.load_module(init_path, True)

            if not strict_load:
                for item in listdir(pack_path):
                    item_path = path.join(pack_path, item)
                    if path.isfile(item_path) and item.endswith('.py') and item != '__init__.py':
                        self.load_module(item_path)
                    elif path.isdir(item_path) and item != '__pycache__' and _check_is_package(item_path):
                        self.load_sub_package(item_path)

    def load_self(self, pack_path: Path | str) -> None:
        '''
        Reinits the object.
        '''
        self.__init__(pack_path)

    def load_sub_package(self, path: Path | str) -> None:
        _path_exists(path)
        package = PackageController(path)
        self.packages[package.name] = package

    def load_module(self, path: Path | str, is_init=False) -> None:
        _path_exists(path)
        module = ModuleController(path)
        if is_init:
            self.init = module
        else:
            self.modules[module.name] = module

    def get_sub_package(self, name: str) -> "PackageController" or None:
        return self.packages.get(name)

    def get_module(self, name: str) -> ModuleController or None:
        return self.modules.get(name)

    def get_all_elements(self) -> list["PackageController" or ModuleController]:
        '''
        Returns list of package and subpackage elements of inner level.
        '''

        elements = []
        elements.extend(self.modules.values())
        elements.extend(self.packages.values())
        return elements

    def __getattr__(self, item):
        if hasattr(self.init, item):
            return getattr(self.init, item)
        elif item in self.modules:
            return self.modules[item]
        elif item in self.packages:
            return self.packages[item]
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{item}'")

    def __iter__(self):
        return iter(self.get_all_elements())
