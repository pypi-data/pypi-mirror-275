import unittest
from pathlib import Path
from .test_function import TestFunction


TCF = Path(__file__).parent / r'./mif/TUFLOW/runs/EG00_001.tcf'
TEMPLATE_FOLDER = TCF.parent.parent.parent / r'./templates'


class TestMif(unittest.TestCase):

    def test_mif_to_gpkg_separate(self):
        test_folder_name = 'gpkg'
        out_folder = TCF.parent / test_folder_name
        template_dir = TEMPLATE_FOLDER / test_folder_name
        gis = 'gpkg'
        grid = 'tif'
        op = 'separate'
        args = ['-tcf', str(TCF), '-o', str(out_folder), '-gis', gis, '-grid', grid, '-op', op, '-verbose', 'off',
                '-always-use-root-dir']
        test = TestFunction()
        test.conversion_test(args, template_dir)

    def test_mif_to_shp_separate(self):
        test_folder_name = 'shp'
        out_folder = TCF.parent / test_folder_name
        template_dir = TEMPLATE_FOLDER / test_folder_name
        gis = 'shp'
        grid = 'tif'
        op = 'separate'
        args = ['-tcf', str(TCF), '-o', str(out_folder), '-gis', gis, '-grid', grid, '-op', op, '-verbose', 'off',
                '-always-use-root-dir']
        test = TestFunction()
        test.conversion_test(args, template_dir)
