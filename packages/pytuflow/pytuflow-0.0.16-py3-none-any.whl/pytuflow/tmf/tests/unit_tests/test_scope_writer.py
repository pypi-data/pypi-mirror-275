from tmf.tuflow_model_files.utils.scope_writer import ScopeWriter
from tmf.tuflow_model_files.dataclasses.scope import Scope, ScopeList


def test_indent_1():
    scope_writer = ScopeWriter()
    assert scope_writer.indent() == ''
    assert scope_writer.indent(1) == ''


def test_indent_2():
    scope_writer = ScopeWriter()
    scope_writer.active_scope.append(Scope('Scenario', 'DEV'))
    assert scope_writer.indent() == '    '
    assert scope_writer.indent(1) == ''


def test_calc_exist_width_1():
    scope_writer = ScopeWriter()
    assert scope_writer.calc_existing_width('Hardware == GPU') == 0


def test_calc_exist_width_2():
    scope_writer = ScopeWriter()
    assert scope_writer.calc_existing_width('    Hardware == GPU') == 4


def test_calc_exist_width_3():
    scope_writer = ScopeWriter()
    assert scope_writer.calc_existing_width('    \tHardware == GPU') == 8


def test_write_1():
    scope_writer = ScopeWriter()
    assert scope_writer.write('Hardware == GPU') == 'Hardware == GPU'


def test_write_2():
    scope_writer = ScopeWriter()
    assert scope_writer.write('    Hardware == GPU') == 'Hardware == GPU'


def test_write_3():
    scope_writer = ScopeWriter()
    assert scope_writer.write('\tHardware == GPU') == 'Hardware == GPU'


def test_write_4():
    scope_writer = ScopeWriter()
    scope_writer.active_scope.append(Scope('Scenario', 'DEV'))
    assert scope_writer.write('Hardware == GPU') == '    Hardware == GPU'
    assert scope_writer.write('\tHardware == GPU') == '\tHardware == GPU'


def test_write_5():
    scope_writer = ScopeWriter()
    scope_writer.active_scope.append(Scope('Scenario', 'DEV'))
    assert scope_writer.write('If Scenario == DEV', header=True) == 'If Scenario == DEV'
    assert scope_writer.write('\tIf Scenario == DEV', header=True) == 'If Scenario == DEV'


def test_write_scope_1():
    scope_writer = ScopeWriter()
    assert scope_writer.write_scope(None) == ''
    assert scope_writer.write_scope(ScopeList([Scope('GLOBAL')])) == ''


def test_write_scope_scenario():
    scope_writer = ScopeWriter()
    scope = ScopeList([Scope('SCENARIO', 'DEV')])
    assert scope_writer.write_scope(scope) == 'If Scenario == DEV\n'
    scope = ScopeList([Scope('SCENARIO', 'DEV2')])
    assert scope_writer.write_scope(scope) == 'Else If Scenario == DEV2\n'
    assert scope_writer.write_scope(None) == 'End If\n'


def test_write_scope_else():
    scope_writer = ScopeWriter()
    scope = ScopeList([Scope('SCENARIO (ELSE)')])
    assert scope_writer.write_scope(scope) == 'Else\n'


def test_write_scope_event():
    scope_writer = ScopeWriter()
    scope = ScopeList([Scope('EVENT', 'Q100')])
    assert scope_writer.write_scope(scope) == 'If Event == Q100\n'
    scope = ScopeList([Scope('Event', 'Q50')])
    assert scope_writer.write_scope(scope) == 'Else If Event == Q50\n'
    assert scope_writer.write_scope(None) == 'End If\n'


def test_write_scope_event_variable():
    scope_writer = ScopeWriter()
    scope = ScopeList([Scope('EVENT VARIABLE', 'Q100')])
    assert scope_writer.write_scope(scope) == 'Define Event == Q100\n'
    assert scope_writer.write_scope(None) == 'End Define\n'
    assert scope_writer.write_scope(scope) == 'Define Event == Q100\n'
    scope = ScopeList([Scope('EVENT VARIABLE', 'Q50')])
    assert scope_writer.write_scope(scope) == 'End Define\nDefine Event == Q50\n'


def test_write_scope_oned_domain():
    scope_writer = ScopeWriter()
    scope = ScopeList([Scope('1D DOMAIN')])
    assert scope_writer.write_scope(scope) == 'Start 1D Domain\n'
    assert scope_writer.write_scope(None) == 'End 1D Domain\n'


def test_write_scope_ouput_zone():
    scope_writer = ScopeWriter()
    scope = ScopeList([Scope('OUTPUT ZONE', 'Zone A')])
    assert scope_writer.write_scope(scope) == 'Define Map Output Zone\n'
    assert scope_writer.write_scope(None) == 'End Define\n'
    assert scope_writer.write_scope(scope) == 'Define Map Output Zone\n'
    scope = ScopeList([Scope('OUTPUT ZONE', 'Zone B')])
    assert scope_writer.write_scope(scope) == 'End Define\nDefine Map Output Zone\n'
