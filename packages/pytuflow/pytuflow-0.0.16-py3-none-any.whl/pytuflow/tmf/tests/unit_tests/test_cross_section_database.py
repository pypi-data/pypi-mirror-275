from tmf.tuflow_model_files.db.xs import CrossSectionDatabase


def test_cross_section_database_tuflow():
    p = './tests/unit_tests/test_datasets/1d_xs_EG14_001_L.shp'
    db = CrossSectionDatabase(p)
    assert db.db().shape == (240, 111)


def test_cross_section_database_tuflow_wildcard():
    p = './tests/unit_tests/test_datasets/1d_xs_EG14_002_L.shp'
    db = CrossSectionDatabase(p)
    assert db.db().shape == (240, 109)
    assert len(db._driver.unresolved_xs) == 1
    assert len([x for x in db._index_to_file.values() if x]) == 55
