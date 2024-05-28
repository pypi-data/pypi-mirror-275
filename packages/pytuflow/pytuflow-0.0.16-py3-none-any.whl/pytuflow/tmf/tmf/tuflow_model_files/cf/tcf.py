from ._cf_build_state import ControlFileBuildState
from ._cf_load_factory import ControlFileLoadMixin
from ..dataclasses.scope import ScopeList
from ..dataclasses.types import PathLike
from ..utils.settings import Settings
from ..abc.build_state import BuildState
from ..dataclasses.event import EventDatabase
from ..dataclasses.scope import Scope
from ..utils.context import Context
from ..dataclasses.file import TuflowPath
from ..abc.cf import ControlFile
from ..db.bc_dbase import BCDatabase
from ..db.mat import MatDatabase
from ..db.soil import SoilDatabase
from .. import const


class TCF(ControlFileLoadMixin, ControlFileBuildState):
    """Initialises the TCF class in a build state. This is the main entry point for reading/writing
    control files.

    If the class is initialised with the :code:`fpath` parameter set to None, an empty class will be initialised.

    Typically, this class is initialised with only the :code:`fpath` parameter set to the path of the control file.
    """
    TUFLOW_TYPE = const.CONTROLFILE.TCF

    def __new__(cls,
                path: PathLike = None,
                settings: Settings = None,
                parent: BuildState = None,
                scope: ScopeList = None,
                **kwargs) -> object:
        """Override __new__ to make sure a TCF class is returned."""
        return object.__new__(cls)
    
    def __init__(self,
                path: PathLike = None,
                settings: Settings = None,
                parent: BuildState = None,
                scope: ScopeList = None,
                **kwargs) -> None:
        """
        Parameters
        ----------
        path : PathLike, optional
            The path to the control file. If set to None, will initialise an empty control file.
        settings : Settings, optional
            A Settings object ("ConvertSettings" object from the convert_tuflow_model_gis_format library).
            This object stores useful information such as variable mappings, current spatial database etc. If
            set to None, a new Settings object will be created. For TCFs, the settings object should be left as None.
        parent : ControlFile, optional
            Will set the parent of the control file to another control file e.g. for a TGC, the parent
            should be set to the TCF. For TCFs, the parent should be set to None.
        scope : ScopeList, optional
            A list of scope objects that will be inherited by the control file itself. Not currently used
            but reserved in case this is useful information in the future.
        log_level : str, optional
            The logging level to use for the control file. Options are 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'.
            Default is 'WARNING'.
        log_to_file : PathLike, optional
            If set, will log the control file to the given file path. Default is None.
        """
        super(TCF, self).__init__(path, settings, parent, scope, **kwargs)

    def tgc(self, context: Context = None) -> 'ControlFile':
        """Returns the TGC ControlFile object.

        If more than one TGC control file object exists, a Context object must be provided to resolve to the correct
        TGC.

        Parameters
        ----------
        context : Context, optional
            A context object to resolve the correct TGC control file object. Not required unless more than one
            TGC control file object exists.

        Returns
        -------
        ControlFile
            The TGC control file object.
        """
        return self._find_control_file('geometry control file', context)

    def tbc(self, context: Context = None) -> 'ControlFile':
        """Returns the TBC ControlFile object.

        If more than one TBC control file object exists, a Context object must be provided to resolve to the correct
        TBC.

        Parameters
        ----------
        context : Context, optional
            A context object to resolve the correct TBC control file object. Not required unless more than one
            TBC control file object exists.

        Returns
        -------
        ControlFile
            The TBC control file object.
        """
        return self._find_control_file('bc control file', context)

    def ecf(self, context: Context = None) -> 'ControlFile':
        """Returns the ECF ControlFile object.

        If more than one ECF control file object exists, a Context object must be provided to resolve to the correct
        ECF.

        Parameters
        ----------
        context : Context, optional
            A context object to resolve the correct ECF control file object. Not required unless more than one
            ECF control file object exists.

        Returns
        -------
        ControlFile
            The ECF control file object.
        """
        return self._find_control_file('estry control file', context)

    def tscf(self, context: Context = None) -> 'ControlFile':
        """Returns the TSCF ControlFile object.

        If more than one TSCF control file object exists, a Context object must be provided to resolve to the correct
        TSCF.

        Parameters
        ----------
        context : Context, optional
            A context object to resolve the correct TSCF control file object. Not required unless more than one
            TSCF control file object exists.

        Returns
        -------
        ControlFile
            The TSCF control file object.
        """
        return self._find_control_file('swmm control file', context)

    def bc_dbase(self, context: Context = None) -> BCDatabase:
        """Returns the BcDatabase Database object.

        If more than one BcDatabase object exists, a Context object must be provided to resolve to the correct
        BcDatabase.

        Parameters
        ----------
        context : Context, optional
            A context object to resolve the correct BCDatabase object. Not required unless more than one
            BCDatabase file object exists.

        Returns
        -------
        BCDatabase
            The BCDatabase object.
        """
        return self._find_control_file('bc database', context)

    def mat_file(self, context: Context = None) -> MatDatabase:
        """Returns the Materials Database object.

        If more than one Materials Database object exists, a Context object must be provided to resolve to the correct
        Materials Database.

        Parameters
        ----------
        context : Context, optional
            A context object to resolve the correct MatDatabase object. Not required unless more than one
            MatDatabase file object exists.

        Returns
        -------
        MatDatabase
            The MatDatabase object.
        """
        return self._find_control_file('read materials? file', context, regex=True)

    def tef(self, context: Context = None) -> 'ControlFile':
        """Returns the TEF ControlFile object.

        If more than one TEF control file object exists, a Context object must be provided to resolve to the correct
        TEF.

        Parameters
        ----------
        context : Context, optional
            A context object to resolve the correct TEF control file object. Not required unless more than one
            TEF control file object exists.

        Returns
        -------
        ControlFile
            The TEF control file object.
        """
        return self._find_control_file('event file', context)

    def event_database(self, context: Context = None) -> EventDatabase:
        """Returns the EventDatabase object.

        If more than one EventDatabase object exists, a Context object must be provided to resolve to the correct
        EventDatabase.

        Parameters
        ----------
        context : Context, optional
            A context object to resolve the correct EventDatabase object. Not required unless more than one
            EventDatabase file object exists.

        Returns
        -------
        EventDatabase
            The EventDatabase object.
        """
        tef = self._find_control_file('event file', context)
        if tef is None:
            return EventDatabase()
        return self._event_cf_to_db(tef)

    def output_folder_1d(self, context: Context = None) -> TuflowPath:
        """Returns the 1D output folder.

        Returns the last instance of the command. If more than one Output Folder exists and some exist in
        IF logic blocks an exception will be raised.

        Parameters
        ----------
        context : Context, optional
            A context object to resolve the correct 1D output directory. Not required unless more than one
            1D output directory exists.

        Returns
        -------
        TuflowPath
            The 1D output directory.
        """
        output_folders = []
        inputs = self.find_input(command='output folder', recursive=True)
        for inp in inputs:
            if '1D' in inp.command.upper():
                output_folders.append(inp)
            if hasattr(self, 'scope') and Scope('1D Domain') in inp.scope():
                output_folders.append(inp)
            if hasattr(self, '_bs') and Scope('1D Domain') in inp._bs.scope():
                output_folders.append(inp)
            if '<EstryControlFile>' in repr(inp.parent) or '<ECFContext>' in repr(inp.parent):
                output_folders.append(inp)

        if len(output_folders) > 1 and hasattr(self, 'scope') and [x for x in output_folders if Scope('GLOBAL') not in x.scope()]:
            if not context:
                raise ValueError('{0} requires context to resolve'.format('Output Folder'))
            else:  # context has been provided, can try and resolve
                for i, inp in enumerate(output_folders[:]):
                    if context.in_context_by_scope(inp._scope):
                        output_folders[i] = inp

        if output_folders:
            return TuflowPath(output_folders[-1].expanded_value)
        else:
            return self._path.parent

    def output_folder_2d(self, context: Context = None) -> TuflowPath:
        """Returns the 2D output folder.

        Returns the last instance of the command. If more than one Output Folder exists and some exist in
        IF logic blocks an exception will be raised.

        Parameters
        ----------
        context : Context, optional
            A context object to resolve the correct 2D output directory. Not required unless more than one
            1D output directory exists.

        Returns
        -------
        TuflowPath
            The 2D output directory.
        """
        output_folders = []
        inputs = self.find_input(command='output folder', recursive=True)
        for inp in inputs:
            if '1D' in inp.command.upper():
                continue
            if hasattr(self, 'scope') and Scope('1D Domain') in inp.scope():
                continue
            if hasattr(self, '_bs') and Scope('1D Domain') in inp._bs.scope():
                continue
            if '<EstryControlFile>' in repr(inp.parent) or '<ECFContext>' in repr(inp.parent):
                continue
            if '<TuflowSWMMControl>' in repr(inp.parent) or '<TSCFContext>' in repr(inp.parent):
                continue
            output_folders.append(inp)

        if len(output_folders) > 1 and hasattr(self, 'scope') and [x for x in output_folders if Scope('GLOBAL') not in x.scope()]:
            if not context:
                raise ValueError('{0} requires context to resolve'.format('Output Folder'))
            else:  # context has been provided, can try and resolve
                for i, inp in enumerate(output_folders[:]):
                    if context.in_context_by_scope(inp._scope):
                        output_folders[i] = inp

        if output_folders:
            return TuflowPath(output_folders[-1].expanded_value)

