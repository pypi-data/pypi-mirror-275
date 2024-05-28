from tmf.tuflow_model_files.db.drivers.xstf import TuflowCrossSectionDatabaseDriver


def test_tuflow_cross_section_driver_test():
    p = './tests/unit_tests/test_datasets/1d_xs_EG14_001_L.shp'
    driver = TuflowCrossSectionDatabaseDriver(p)
    assert driver.test_is_self(p) == True


def test_tuflow_cross_section_driver():
    p = './tests/unit_tests/test_datasets/1d_xs_EG14_001_L.shp'
    driver = TuflowCrossSectionDatabaseDriver(p)
    df = driver.load(p)
    assert df.shape == (240, 111)
