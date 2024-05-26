import unittest
from dinamic_py_loader.dinamic_py_loader import PackageController, ModuleController, DinamicLoader
from pathlib import Path


TEST_ROOT = Path(__file__).parent


class LoadingTests(unittest.TestCase):
    def test_module_controller(self):
        mod_name = 'direct_module.py'
        mod_path = TEST_ROOT / mod_name
        MOD_CONTR = ModuleController(mod_path)

        # Name and path check:
        self.assertEqual(MOD_CONTR.name, mod_name[:-3])
        self.assertEqual(MOD_CONTR.path, str(mod_path))     # str because of test can be run on windows

        # Elements access check:
        self.assertEqual(MOD_CONTR.DIRECT_MODULE_GLOBAL['key'], 'value')

        # Same tests with non-ascii path and after reload:
        mod_name = 'cat_module.py'
        mod_path = TEST_ROOT / 'коська'/ mod_name

        MOD_CONTR.load_self(mod_path)
        self.assertEqual(MOD_CONTR.name, 'cat_module')
        self.assertEqual(MOD_CONTR.path, str(mod_path))

        self.assertEqual(MOD_CONTR.CAT_MODULE_GLOBAL['key'], 'value')

    def test_package_controller(self):
        pkg_name = 'pkg1'
        pack_path = TEST_ROOT / pkg_name

        PACK_CONTR = PackageController(pack_path)

        # Name and path check:
        self.assertEqual(PACK_CONTR.name, pkg_name)
        self.assertEqual(PACK_CONTR.path, str(pack_path))

        # Checking subpackage existence and its name and path:
        sub_pack_name = 'pkg1_sub_pkg'
        sub_pack_path = pack_path / sub_pack_name

        self.assertTrue(sub_pack_name in PACK_CONTR.packages)
        sub_pack = PACK_CONTR.packages[sub_pack_name]
        self.assertEqual(sub_pack.name, sub_pack_name)
        self.assertEqual(sub_pack.path, str(sub_pack_path))
        self.assertEqual(PACK_CONTR.pkg1_sub_pkg, sub_pack)

        # Checking parsed elements list and iterator:
        self.assertTrue(
            ['source_1', 'pkg1_sub_pkg'],
            [elem.name for elem in PACK_CONTR]
        )

        # Checking access to child elements:
        # Subpackage module:
        self.assertEqual(
            PACK_CONTR.pkg1_sub_pkg.source_1_1.SOURCE_1_1_GLOBAL['key'],
            'value'
        )

        # Inner module:
        self.assertEqual(
            PACK_CONTR.source_1.SOURCE_1_GLOBAL['key'],
            'value'
        )

        # Checking __init__py direct access:
        self.assertEqual(
            PACK_CONTR.INIT_GLOBAL['key'],
            'value'
        )

        # Checking some points with non-ascii path and after reload:
        pkg_name = 'коська'
        pack_path = TEST_ROOT / pkg_name

        PACK_CONTR.load_self(pack_path)
        self.assertEqual(PACK_CONTR.name, pkg_name)
        self.assertEqual(PACK_CONTR.path, str(pack_path))

        # Checking access:
        # Subpackage module:
        self.assertEqual(
            PACK_CONTR.подкоська.sub_cat_module.SUB_CAT_MODULE_GLOBAL['key'],
            'value'
        )

        # Inner module:
        self.assertEqual(
            PACK_CONTR.cat_module.CAT_MODULE_GLOBAL['key'],
            'value'
        )

    def test_dinamic_loader(self):
        first_pack_path = TEST_ROOT / 'коська'
        second_pack_path = TEST_ROOT / 'pkg1'
        mod_path = TEST_ROOT / 'direct_module.py'

        loader = DinamicLoader([first_pack_path, mod_path], second_pack_path)

        # Checking all elements in (there is no need to test other because its based on PackageController class):
        self.assertTrue(
            ['коська', 'pkg1', 'direct_module'],
            [elem.name for elem in loader]
        )


if __name__ == '__main__':
    unittest.main()
