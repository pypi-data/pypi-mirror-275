import re
from typing import TYPE_CHECKING, Union
from collections import OrderedDict

from ...convert_tuflow_model_gis_format.conv_tf_gis_format.helpers.file import TuflowPath
from ..dataclasses.scope import Scope, ScopeList

if TYPE_CHECKING:
    from ..utils.commands import Command
    from ..cf._cf_build_state import ControlFileBuildState
    from ..inp._inp_build_state import InputBuildState

from ..utils import logging as tmf_logging
logger = tmf_logging.get_tmf_logger()


class AlteredInput:

    def __new__(cls, cmd: 'Command', scope: ScopeList, cf: 'ControlFileBuildState', trd: TuflowPath, i: int, j: int, uuid, change_type: str):
        if change_type == 'update_value':
            cls = AlteredInputUpdatedValue
        elif change_type == 'update_command':
            cls = AlteredInputUpdatedCommand
        elif change_type == 'add_input':
            cls = AlteredInputAddedInput
        elif change_type == 'remove_input':
            cls = AlteredInputRemovedInput
        elif change_type == 'set_scope':
            cls = AlteredInputSetScope
        return super().__new__(cls)

    def __init__(self, cmd: 'Command', scope: ScopeList, cf: 'ControlFileBuildState', trd: TuflowPath, i: int, j: int, uuid, change_type: str):
        self.cmd = cmd
        self.scope = scope
        self.cf = cf
        self.trd = trd
        self.i = i
        self.j = j
        self.uuid = uuid
        self.change_type = change_type

    def __repr__(self):
        return '<{0} {1} {2} {3}>'.format(__class__.__name__, self.i, self.j, self.cmd)

    def undo(self):
        logger.error('undo method should be implemented by subclass')
        raise NotImplementedError


class AlteredInputUpdatedValue(AlteredInput):

    def undo(self):
        if self.i >= 0:
            inp = self.cf.inputs[self.i]
        else:
            inp = self.cf.inputs._inputs[self.j]
        inp.set_raw_command_obj(self.cmd)


class AlteredInputUpdatedCommand(AlteredInputUpdatedValue):
    pass


class AlteredInputAddedInput(AlteredInput):

    def undo(self):
        if self.i >= 0:
            self.cf.remove_input(self.cf.inputs[self.i])
        else:
            self.cf.inputs._inputs.pop(self.j)


class AlteredInputRemovedInput(AlteredInput):

    def undo(self):
        self.cf._insert_input(self.i, self.cmd, self.trd, False)


class AlteredInputSetScope(AlteredInput):

    def undo(self):
        if self.i >= 0:
            inp = self.cf.inputs[self.i]
        else:
            inp = self.cf.inputs._inputs[self.j]
        inp._set_scope(self.scope)


class AlteredInputs:

    def __init__(self):
        self._updated_inputs = []
        self._block = False

    def __repr__(self):
        return '<AlteredInputs>'

    def add(self, inp: 'InputBuildState', i: int, j: int, uuid, change_type: str):
        if not self._block:
            ac = AlteredInput(inp.raw_command_obj(), inp._scope, inp.parent, inp.trd, i, j, uuid, change_type)
            self._updated_inputs.append(ac)

    def undo(self, cf: 'ControlFileBuildState', reset_children: bool):
        self._block = True  # so changes aren't recorded while undoing
        inputs = []
        if self._updated_inputs:
            ac = self._updated_inputs.pop()
            inputs = [x for x in self._updated_inputs[::-1] if x.uuid == ac.uuid]
            inputs.insert(0, ac)
        if inputs:
            for ac in inputs:
                if ac.cf != cf and not reset_children:
                    continue
                ac.undo()
                if ac in self._updated_inputs:
                    self._updated_inputs.remove(ac)
        self._block = False
        if inputs:
            return inputs

    def reset(self, cf: 'ControlFileBuildState', reset_children: bool):
        while self.undo(cf, reset_children):
            pass

    def is_dirty(self, cf: 'ControlFileBuildState'):
        for ac in self._updated_inputs:
            if ac.cf == cf:
                return True
        return False

    def clear(self):
        for ac in self._updated_inputs:
            for inp in ac.cf.inputs:
                inp.dirty = False
            ac.cf.dirty = False
            ac.cf.tcf.dirty = False
        self._updated_inputs.clear()
