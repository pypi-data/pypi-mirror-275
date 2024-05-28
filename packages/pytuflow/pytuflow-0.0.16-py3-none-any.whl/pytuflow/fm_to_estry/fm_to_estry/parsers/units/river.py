import io
from typing import TextIO

import numpy as np
import pandas as pd

from .handler import Handler, SubHandler


class River(Handler):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._xs_point_count = 0
        self.TYPE = 'unit'
        self.headers = []
        self.ncol = 0
        self.spill_1 = None
        self.spill_2 = None
        self.lat_inflow_1 = None
        self.lat_inflow_2 = None
        self.lat_inflow_3 = None
        self.lat_inflow_4 = None
        self.dx = 0
        self.n = 0
        self.xs = pd.DataFrame()
        self.valid = True

    @staticmethod
    def unit_type_name() -> str:
        return 'RIVER'

    def load(self, line: str, fo: TextIO, fixed_field_len: int, line_no: int) -> None:
        super().load(line, fo, fixed_field_len, line_no)

        # load sub_type
        self._set_attrs_str(self.read_line(), ['sub_type'], log_errors=True)
        self.sub_type = self.sub_type.split(' ')[0]
        if self.sub_type == 'SECTION':
            self._sub_obj = RiverSection(self.parent)
        elif self.sub_type == 'CES':
            self._sub_obj = RiverCES(self.parent)
        self._sync_obj(self._sub_obj)

        # attributes
        self._set_attrs_str(self.read_line(True),
                            ['id', 'spill_1', 'spill_2', 'lat_inflow_1', 'lat_inflow_2', 'lat_inflow_3', 'lat_inflow_4'],
                            log_errors=[0])
        self.uid = self._get_uid()
        self._set_attrs_float(self.read_line(), ['dx'], log_errors=True)
        self._set_attrs_int(self.read_line(), ['n'], log_errors=True)

        # load cross-section DataFrame
        if self._sub_obj:
            self._sub_obj._sync_obj(self)
            self._sub_obj.load(line, fo, fixed_field_len, self.line_no)
            self._sync_obj(self._sub_obj)

        if self.n:
            a = np.genfromtxt(self.fo, delimiter=(10,10,10,10,10,10,10,10,10), max_rows=self.n, dtype='U')
            if len(a.shape) == 1:
                a = np.reshape(a, (self.n, a.size))
            a1 = a[:, :3].astype(float)
            self.xs = pd.DataFrame(a1, columns=self.headers[:3])
            if a.shape[1] >= 7:
                self.xs['deactivation_marker'] = a[:,7]
            self.line_no += self.n

            # self.xs.rename(columns={i: self.headers[i] for i in range(self.xs.shape[1])}, inplace=True)
        self._sub_obj._sync_obj(self)

        # subtype specific post loading steps
        self._sub_obj.post_load()
        self._sync_obj(self._sub_obj)


class RiverSection(SubHandler):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.headers = ['x', 'y', 'n', 'rel_path_len', 'chan_marker', 'easting', 'northing', 'deactivation_marker',
                        'sp_marker']
        self.ncol = len(self.headers)

    def post_load(self) -> None:
        if self.xs.empty:
            return
        if 'rel_path_len' in self.xs.columns and self.xs['rel_path_len'].dtype == np.float64:
            self.xs['path_marker'] = ['' for _ in range(self.n)]
        elif 'path_marker' in self.xs.columns and 'rel_path_len' in self.xs.columns:
            self.xs[['path_marker', 'rel_path_len']] = self.xs['rel_path_len'].str.split(' ', n=1, expand=True)
            self.xs['rel_path_len'] = np.where(self.xs['path_marker'] != '*', self.xs.path_marker, self.xs.rel_path_len)
            self.xs['path_marker'] = np.where(self.xs['path_marker'] == '*', self.xs.path_marker, '')
        if not self.xs.empty:
            self.bed_level = float(str(self.xs.y.min()))


class RiverCES(SubHandler):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.headers = ['x', 'y', 'bank_marker', 'sinuosity', 'chan_marker', 'easting', 'northing']
        self.ncol = len(self.headers)
        self.nrz = 0
        self.roughness_zone = pd.DataFrame()
        self.roughness_zone_headers = ['x', 'rz']
        self.ncol_roughness_zone = len(self.roughness_zone_headers)

    def load(self, line: str, fo: TextIO, fixed_field_len: int, line_no: int) -> None:
        self.nrz = int(self.read_line()[0])
        if self.nrz:
            a = np.genfromtxt(self.fo, delimiter=(10, 10), max_rows=self.nrz, dtype='f4')
            if a.shape != (self.nrz, self.ncol_roughness_zone):
                a = np.reshape(a, (self.nrz, self.ncol_roughness_zone))
            self.roughness_zone = pd.DataFrame(a, columns=self.roughness_zone_headers)
            self.line_no += self.nrz
