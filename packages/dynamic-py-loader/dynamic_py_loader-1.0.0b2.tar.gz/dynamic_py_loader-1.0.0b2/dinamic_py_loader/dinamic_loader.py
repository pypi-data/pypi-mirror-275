from .package_controller import PackageController
from .module_controller import ModuleController
from pathlib import Path
from os import path


class DinamicLoader(PackageController):
    '''
    Can load packages dynamically.
    ! Warning: relative path doesn't work properly because of realpath problem.
    '''

    def __init__(self, *args, loaders=None):
        '''
        :param args: Indefinite number of path objects from pathlib/path strings or list with them.
        :param loaders: Other objects of that class. Used to copy their data in current object.
        '''

        super().__init__()
        self.paths_pool = self._process_args(args)
        self.loaders = loaders or []

        for path in self.paths_pool:
            self.load_element(path)

        for loader in self.loaders:
            for package_path in loader.paths_pool:
                self.load_element(package_path)

    def _process_args(self, args: Path | str | list[Path|str]):
        paths = []
        for arg in args:
            match arg:
                case str() | Path():
                    paths.append(arg)
                case list():
                    paths.extend(arg)
                case type:
                    print(type)
                    raise ValueError(f'{type} is invalid argument type, list or str expected.')
        return paths

    def load_element(self, elem_path: Path | str) -> None: # add possibility to get lists
        '''
        :param elem_path: path object from pathlib or path str
        '''

        elem_path = str(Path(elem_path).resolve())
        if not path.exists(elem_path):
            raise ImportError(f"Given path doesn't exist: {elem_path}.")
        if path.isdir(elem_path):
            package = PackageController(elem_path)
            self.packages[package.name] = package
        else:
            module = ModuleController(elem_path)
            self.packages[module.name] = module
