import decalmlutils
from decalmlutils.testing import _import_submodules


def test_all_modules_importable():
    """
    A test which checks that all modules in a package can be imported.
    """
    _import_submodules(decalmlutils)
