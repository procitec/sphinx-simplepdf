import sys
import pkgutil
import platform
try:
    from importlib.metadata import version
except ImportError:
    from importlib_metadata import version


class DebugPython:

    @property
    def py_exec(self):
        return sys.executable

    def get_packages(self):
        packages = list(pkgutil.iter_modules())

        names = [x[1] for x in packages]

        final = {}
        for name in names:
            try:
                __version__ = version(name)
            except (Exception):
                final[name] = 'unknown'
            else:
                final[name] = __version__

        return final

    @property
    def os(self):
        return platform.system(), platform.release()
