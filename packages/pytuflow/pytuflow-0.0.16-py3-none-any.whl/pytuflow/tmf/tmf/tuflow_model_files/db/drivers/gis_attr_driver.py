from collections import OrderedDict
from collections.abc import Iterable
from pathlib import Path
from ...dataclasses.file import TuflowPath

from ...dataclasses.types import PathLike


class GISAttributes(Iterable):
    """Class that will iterate over TUFLOW GIS supported file format attributes.

    This class does not use GDAL and therefore can be used as a light-weight alternative to extract
    attribute information for selected GIS formats.

    Supported formats:

    * SHP/DBF
    * MIF/MID
    * GPKG
    """

    def __new__(cls, fpath: PathLike) -> object:
        if '>>' in fpath:
            fpath = fpath.split(' >> ')[0]
        fpath = Path(fpath)
        if fpath.suffix.lower() == '.dbf' or fpath.suffix.lower() == '.shp':
            cls = DBFAttributes
        elif fpath.suffix.lower() == '.mid' or fpath.suffix.lower() == '.mif':
            cls = MIDAttributes
        elif fpath.suffix.lower() == '.gpkg':
            cls = GPKGAttributes
        return super().__new__(cls)

    def __init__(self, fpath: PathLike) -> None:
        """
        Parameters
        ----------
        fpath : PathLike
            Path to the GIS file.
        """
        self.fpath = TuflowPath(fpath)
        self._db = None
        self.open()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def open(self) -> None:
        raise NotImplementedError

    def close(self) -> None:
        raise NotImplementedError


class DBFAttributes(GISAttributes):

    def __init__(self, fpath: PathLike) -> None:
        fpath = TuflowPath(fpath).dbpath
        if fpath.suffix.lower() == '.shp':
            if fpath.with_suffix('.dbf').exists():
                fpath = fpath.with_suffix('.dbf')
            elif fpath.with_suffix('.DBF').exists():
                fpath = fpath.with_suffix('.DBF')
            else:
                raise FileNotFoundError(f'Accompanying DBF file not found for: {self.fpath}')
        super().__init__(fpath)

    def __iter__(self) -> OrderedDict:
        for record in self._db:
            yield record

    def open(self) -> None:
        from dbfread import DBF
        self._db = DBF(self.fpath)

    def close(self) -> None:
        self._db = None


class MIDAttributes(GISAttributes):

    def __init__(self, fpath: PathLike) -> None:
        fpath = TuflowPath(fpath).dbpath
        self._col_names = []
        if fpath.suffix.lower() == '.mif':
            self._mif = fpath
            if fpath.with_suffix('.mid').exists():
                fpath = fpath.with_suffix('.mid')
            elif fpath.with_suffix('.MID').exists():
                fpath = fpath.with_suffix('.MID')
            else:
                raise FileNotFoundError(f'Accompanying MID file not found for: {fpath}')
        else:
            if fpath.with_suffix('.mif').exists():
                self._mif = fpath.with_suffix('.mif')
            elif fpath.with_suffix('.MIF').exists():
                self._mif = fpath.with_suffix('.MIF')
            else:
                raise FileNotFoundError(f'Accompanying MIF file not found for: {fpath}')
        super().__init__(fpath)

    def __iter__(self) -> OrderedDict:
        for line in self._db:
            yield OrderedDict(zip(self._col_names, [x.strip(' \t\n"\'') for x in line.split(',')]))

    def open(self) -> None:
        self._db = self.fpath.open()
        ncol = 0
        with self._mif.open() as f:
            for line in f:
                if line.startswith('Columns'):
                    ncol = int(line.split()[1])
                    for i in range(ncol):
                        self._col_names.append(f.readline().split()[0])
                    break
        if not ncol:
            raise Exception(f'MIF file must have at least one attribute column: {self._mif}')

    def close(self) -> None:
        self._db.close()
        self._db = None


class GPKGAttributes(GISAttributes):

    def __init__(self, fpath: TuflowPath) -> None:
        fpath = TuflowPath(fpath)
        self._tname = fpath.lyrname
        fpath = fpath.dbpath
        self._tname = self._get_case_insensitive_table_name(fpath, self._tname)
        self._geom_col = self._get_geom_col(fpath, self._tname)
        self._fid_col = self._get_fid_col(fpath, self._tname)
        super().__init__(fpath)

    def __iter__(self) -> OrderedDict:
        import sqlite3
        try:
            self._db = sqlite3.connect(self.fpath)
            self._cursor = self._db.cursor()
            self._cursor.execute(f'SELECT * FROM "{self._tname}";')
            for row in self._cursor:
                inds = [i for i, x in enumerate(self._cursor.description) if x[0] not in (self._fid_col, self._geom_col)]
                yield OrderedDict([(self._cursor.description[i][0], row[i]) for i in inds])
        except:
            pass
        finally:
            self._db.close()
            self._cursor = None
            self._db = None

    def open(self) -> None:
        pass

    def close(self) -> None:
        pass

    def _get_case_insensitive_table_name(self, fpath: PathLike, tname: str) -> str:
        import sqlite3
        db = sqlite3.connect(fpath)
        try:
            cursor = db.cursor()
            cursor.execute(f'SELECT name FROM sqlite_master WHERE type="table" AND name="{tname}" COLLATE NOCASE;')
            tname = cursor.fetchone()[0]
        except:
            tname = tname
        finally:
            db.close()
            return tname

    def _get_geom_col(self, fpath: PathLike, tname: str) -> str:
        import sqlite3
        db = sqlite3.connect(fpath)
        try:
            cursor = db.cursor()
            cursor.execute(f'SELECT column_name FROM gpkg_geometry_columns WHERE table_name="{tname}";')
            geom_col = cursor.fetchone()[0]
        except:
            geom_col = 'geometry'
        finally:
            db.close()
        return geom_col

    def _get_fid_col(self, fpath: PathLike, tname: str) -> str:
        import sqlite3
        db = sqlite3.connect(fpath)
        try:
            cursor = db.cursor()
            cursor.execute(f'SELECT name FROM PRAGMA_TABLE_INFO("{self._tname}") WHERE pk = 1;')
            fid_col = cursor.fetchone()[0]
        except:
            fid_col = 'fid'
        finally:
            db.close()
        return fid_col
