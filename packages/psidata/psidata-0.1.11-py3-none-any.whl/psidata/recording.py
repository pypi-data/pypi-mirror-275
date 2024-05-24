import logging
log = logging.getLogger(__name__)

import functools
from pathlib import Path
import yaml
import zipfile

import numpy as np
import pandas as pd


try:
    from . import bcolz_tools
    log.info('Using actual bcolz backend')
except ImportError:
    try:
        from . import legacy_bcolz_tools as bcolz_tools
        log.info('Using legacy bcolz backend')
    except ImportError:
        log.info('Legacy bcolz backend is not available')


UNSET = object()


class Recording:
    '''
    Wrapper around a recording created by psiexperiment

    Parameters
    ----------
    base_path : :obj:`str` or :obj:`pathlib.Path`
        Folder containing recordings

    Attributes
    ----------
    base_path : pathlib.Path
        Folder containing recordings
    carray_names : set
        List of Bcolz carrays in this recording
    ctable_names : set
        List of Bcolz ctables in this recording
    ttable_names : set
        List of CSV-formatted tables in this recording

    The `__getattr__` method is implemented to allow accessing arrays and
    tables by name. For example, if you have a ctable called `erp_metadata`:

        recording = Recording(base_path)
        erp_md = recording.erp_metadata

    When using this approach, all tables are loaded into memory and returned as
    instances of `pandas.DataFrame`. All arrays are returned as `Signal`
    instances. Signal instances do not load the data into memory until the data
    is requested.
    '''

    #: Mapping of names for CSV-formatted table to a list of columns that
    #: should be used as indices. For example:
    #:     {'tone_sens': ['channel_name', 'frequency']}
    #: This attribute is typically used by subclasses to automate handling of
    #: loading tables into DataFrames.
    _ttable_indices = {}

    #: This is the name of the table containing the settings that we may wish
    #: to extract.
    _setting_table = None

    def __init__(self, base_path, setting_table=None, store_class=None):
        self._setting_table = setting_table
        self.base_path = Path(base_path)
        if store_class is None:
            if self.base_path.suffix == '.zip':
                store_class = ZipStore
            elif (self.base_path / self.base_path.with_suffix('.zip').name).exists():
                store_class = NestedZipStore
            elif self.base_path.is_dir():
                store_class = DirStore
            else:
                raise ValueError(f'Unrecognized recording format at {base_path}')
        elif isinstance(store_class, str):
            store_class = globals()[store_class]
        self._store = store_class(self.base_path, self._ttable_indices)

    def get_parameters(self):
        preferences = yaml.safe_load(self._store._get_text_stream('initial.preferences'))
        expressions = {}
        for context_items in preferences['context']['parameters'].values():
            for name, setting in context_items.items():
                if 'expression' in setting:
                    expressions[name] = setting['expression']
                elif 'selected' in setting:
                    expressions[name] = setting['selected']
                else:
                    raise ValueError
        return expressions

    def get_setting(self, setting_name, default=UNSET):
        '''
        Return value for setting

        Parameters
        ----------
        setting_name : string
            Setting to extract

        Returns
        -------
        object
            Value of setting

        Raises
        ------
        ValueError
            If the setting is not identical across all trials.
        KeyError
            If the setting does not exist.
        '''
        table = getattr(self, self._setting_table)
        try:
            values = np.unique(table[setting_name])
        except KeyError:
            if default is not UNSET:
                return default
            else:
                raise
        if len(values) != 1:
            raise ValueError(f'{setting_name} is not unique across all epochs.')
        return values[0]

    def get_setting_default(self, setting_name, default):
        '''
        Return value for setting

        Parameters
        ----------
        setting_name : string
            Setting to extract
        default : obj
            Value to return if setting doesn't exist.

        Returns
        -------
        object
            Value of setting

        Raises
        ------
        ValueError
            If the setting is not identical across all trials.
        '''
        try:
            return self.get_setting(setting_name)
        except KeyError:
            return default

    def __getattr__(self, attr):
        return self._store.__getattr__(attr)

    def __repr__(self):
        lines = [f'Recording at {self.base_path.name} with:']
        if self._store.zarr_names:
            lines.append(f'* Zarr arrays {self._store.zarr_names}')
        if self._store.carray_names:
            lines.append(f'* Bcolz carrays {self._store.carray_names}')
        if self._store.ctable_names:
            lines.append(f'* Bcolz ctables {self._store.ctable_names}')
        if self._store.ttable_names:
            lines.append(f'* CSV tables {self._store.ttable_names}')
        return '\n'.join(lines)


class BaseStore:

    def _refresh_names(self):
        '''
        Utility function to refresh list of signals and tables
        '''
        raise NotImplementedError

    def __getattr__(self, attr):
        if attr in self.zarr_names:
            return self._load_zarr_signal(attr)
        if attr in self.carray_names:
            return self._load_bcolz_signal(attr)
        if attr in self.ctable_names:
            return self._load_bcolz_table(attr)
        if attr in self.ttable_names:
            return self._load_text_table(attr)
        raise AttributeError(attr)

    @functools.lru_cache()
    def _load_bcolz_signal(self, name):
        return bcolz_tools.BcolzSignal(self.base_path / name)

    @functools.lru_cache()
    def _load_zarr_signal(self, name):
        from .zarr_tools import ZarrSignal
        return ZarrSignal.from_path(self.base_path / name)

    @functools.lru_cache()
    def _load_bcolz_table(self, name):
        return bcolz_tools.load_ctable_as_df(self.base_path / name)

    def _get_text_stream(self, name):
        raise NotImplementedError

    @functools.lru_cache()
    def _load_text_table(self, name):
        import pandas as pd
        index_col = self._ttable_indices.get(name, None)
        with self._get_text_stream(f'{name}.csv') as stream:
            df = pd.read_csv(stream, index_col=index_col)

        drop = [c for c in df.columns if c.startswith('Unnamed:')]
        return df.drop(columns=drop)


class DirStore(BaseStore):

    def __init__(self, base_path, ttable_indices):
        self.base_path = Path(base_path)
        self._ttable_indices = ttable_indices
        self._refresh_names()

    def _get_text_stream(self, name):
        path = self.base_path / name
        return path.open()

    def _refresh_names(self):
        bp = self.base_path
        self.carray_names = {d.parent.stem for d in bp.glob('*/meta')}
        self.ctable_names = {d.parent.parent.stem for d in bp.glob('*/*/meta')}
        self.ttable_names = {d.stem for d in bp.glob('*.csv')}
        self.zarr_names = {d.stem for d in bp.glob('*.zarr')}


class ZipStore(BaseStore):

    def __init__(self, base_path, ttable_indices):
        self.base_path = Path(base_path)
        self._ttable_indices = ttable_indices
        self.zip_fh = zipfile.ZipFile(base_path)
        self._refresh_names()

    def _refresh_names(self):
        self.carray_names = set()
        self.ctable_names = set()
        self.ttable_names = set()
        self.zarr_names = set()
        for name in self.zip_fh.namelist():
            if name.endswith('.zarr/'):
                self.zarr_names.add(name.split('.', 1)[0])
            elif name.endswith('.csv'):
                self.ttable_names.add(name.split('.', 1)[0])
            elif name.endswith('meta'):
                raise ValueError('ZipRecording does not support bcolz')

    def _get_text_stream(self, name):
        return self.zip_fh.open(name)

    @functools.lru_cache()
    def _load_zarr_signal(self, name):
        from .zarr_tools import ZarrSignal
        return ZarrSignal.from_zip(self.base_path, name)


class NestedZipStore(ZipStore):

    def __init__(self, base_path, ttable_indices):
        base_path = base_path / base_path.with_suffix('.zip').name
        super().__init__(base_path, ttable_indices)
