from ..dataclasses.scope import Scope, GlobalScope

from ..utils import logging as tmf_logging
logger = tmf_logging.get_tmf_logger()


class Inputs(list):

    def __init__(self, inputs=()):
        list.__init__(self)
        self._inputs = list(inputs)
        list.extend(self, [x for x in inputs if x])
        self._indexes = []

    def __repr__(self):
        return '{0}({1})'.format(self.__class__.__name__, [str(x) for x in self])

    def _known_scopes(self) -> list[Scope]:
        scopes = [x._scope for x in self if x._scope]
        if scopes:
            scopes = [x for x in sum(scopes,[]) if x.known() or isinstance(x, GlobalScope)]
        return scopes

    def append(self, input) -> None:
        try:
            if input.is_start_block() or input.is_end_block():
                return
            is_input = True
        except AttributeError:
            is_input = False

        self._inputs.append(input)
        if input or not is_input:
            list.append(self, input)

        # this section is so that this class can be used to help record changes to the inputs, recording the
        # index of each input as it is added (which may only be correct at the instance it is added, changing as soon
        # as the next input is added) - therefore allowing the ability to unwind in reverse order
        # only available via the 'append' method
        if hasattr(input, 'parent') and input.parent and hasattr(input.parent, 'inputs') and hasattr(input, 'uuid'):
            if input.uuid in [x.uuid for x in input.parent.inputs]:
                i = [x.uuid for x in input.parent.inputs].index(input.uuid)
            else:
                i = -1
            try:
                j = [x.uuid for x in input.parent.inputs._inputs].index(input.uuid)
            except ValueError:
                logger.error('Input not found in parent - please use append_input or insert_input methods to add inputs')
                raise ValueError('Input not found in parent - please use append_input or insert_input methods to add inputs')
        else:
            i, j = -1, -1
        self._indexes.append((i, j))  # used for undoing later if needed

    def insert(self, ind, input, after=False) -> None:
        try:
            if input.is_start_block() or input.is_end_block():
                return
        except AttributeError:
            pass
        inp = self[ind]
        i = self._inputs.index(inp)
        if after:
            if input:
                list.insert(self, ind + 1, input)
            self._inputs.insert(i + 1, input)
        else:
            if input:
                list.insert(self, ind, input)
            self._inputs.insert(i, input)

    def extend(self, items) -> None:
        self._inputs.extend(items)
        for input in items:
            if input:
                list.append(self, input)

    def remove(self, value):
        self._inputs.remove(value)
        list.remove(self, value)

    def resolve_scopes(self) -> None:
        scopes = self._known_scopes()
        if not scopes:
            return
        for input in self:
            input.figure_out_file_scopes(scopes)

    def iter_indexes(self):
        for i, inp in enumerate(self._inputs):
            yield inp, self._indexes[i]


class ComplexInputs(Inputs):
    pass

