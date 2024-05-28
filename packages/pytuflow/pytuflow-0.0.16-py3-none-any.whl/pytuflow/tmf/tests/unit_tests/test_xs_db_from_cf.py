from tmf.tuflow_model_files.cf._cf_build_state import ControlFileBuildState


def test_xs_db_from_cf():
    p = './tests/unit_tests/test_datasets/example_tuflow_cross_sections.ecf'
    cf = ControlFileBuildState(p)
    inp = cf.find_input('read gis table links')[0]
    db = cf.input_to_loaded_value(inp)[0]
    assert db.db().shape == (240, 109)


def test_xs_db_ctx():
    p = './tests/unit_tests/test_datasets/example_tuflow_cross_sections.ecf'
    cf = ControlFileBuildState(p)
    ctx = cf.context()
    inp = ctx.find_input('read gis table links')[0]
    db = ctx.input_to_loaded_value(inp)
    assert db.db().shape == (240, 111)  # missing cross-section should now be resolved and loaded


def test_fmxs_from_cf():
    p = './tests/unit_tests/test_datasets/example_fm_cross_sections.ecf'
    cf = ControlFileBuildState(p)
    inp = cf.find_input('xs database')[0]
    db = cf.input_to_loaded_value(inp)[0]
    assert db.db().shape == (213, 510)


def test_fmxs_from_cf_ctx():
    p = './tests/unit_tests/test_datasets/example_fm_cross_sections.ecf'
    cf = ControlFileBuildState(p)
    ctx = cf.context()
    inp = ctx.find_input('xs database')[0]
    db = ctx.input_to_loaded_value(inp)
    assert db.db().shape == (213, 510)
