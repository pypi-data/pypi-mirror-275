from importlib import util
from os import path
from pathlib import Path


class ModuleController():
    '''
    Stores dynamically loaded module, can be empty and reloaded.
    ! Warning: relative path doesn't work properly because of realpath problem.
    '''

    def __init__(self, mod_path: Path | str | None = None):
        '''
         :param mod_path: *Path* object from *pathlib* or str path, should be absolute, can be None;
        '''

        self.spec = None
        self.module = None

        if mod_path:
            mod_path = str(Path(mod_path).resolve())

            if not path.exists(mod_path):
                raise ImportError(f"Given module path doesn't exist: {mod_path}.")
            if not (path.isfile(mod_path) and mod_path.endswith('.py')):
                raise ImportError(f"Given module path isn't a Python module: {mod_path}.")

            spec = util.spec_from_file_location(path.basename(mod_path), mod_path)
            if spec is None:
                raise ImportError(f"Could not create a module spec for {mod_path}.")

            self.spec = spec
            self.module = util.module_from_spec(spec)
            spec.loader.exec_module(self.module)

    @property
    def name(self):
        return self.spec.name[:-3]  # Not to take .py

    @property
    def path(self):
        return self.spec.origin

    def load_self(self, mod_path: Path | str) -> None:
        '''
        Reinits the object.
        '''
        self.__init__(mod_path)

    def get(self, elem: str, default=None) -> any:
        '''
        :param elem: string name of any global namespace ement
        :param default: default specified walue
        '''

        try:
            return getattr(self.module, elem)   # Getattr for module even with specified default raises error!
        except ModuleNotFoundError:
            return default

    def __getattr__(self, item):
        return getattr(self.module, item)
