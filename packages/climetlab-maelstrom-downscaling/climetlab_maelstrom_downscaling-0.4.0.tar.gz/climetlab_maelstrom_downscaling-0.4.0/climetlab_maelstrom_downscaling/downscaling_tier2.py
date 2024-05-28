#!/usr/bin/env python3# (C) Copyright 2024 ECMWF and JSC
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF and JSC do not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#
#from __future__ import annotations

from typing import Union, List
import numpy as np
import pandas as pd
import xarray as xr
import climetlab as cml
from climetlab import Dataset
from climetlab.decorators import normalize

List_or_string = Union[List, str]

__version__ = "0.4.0"


URL = "https://object-store.os-api.cci1.ecmwf.int"
PATTERN = "{url}/maelstrom-ap5/tier-2/downscaling_tier2_{date}.nc"

@normalize("x","date-list(%Y-%m)")
def DateListNormaliser(x):
    return x

class Downscaling(Dataset):
    class_name = "Downsclaing_Dataset"
    name = "Tier-2 dataset based on ERA 5 and COSMO REA6 reanalysis data"
    home_page = "https://git.ecmwf.int/projects/MLFET/repos/maelstrom-downscaling-ap5"
    licence = "Apache Licence Version 2.0"
    documentation = "-"
    citation = "-"
    terms_of_use = (
        "By downloading data from this dataset, you agree to the terms and conditions defined at "
        "https://git.ecmwf.int/projects/MLFET/repos/maelstrom-downscaling-ap5/browse/climetlab-maelstrom-downscaling-ap5/LICENSE"
        "If you do not agree with such terms, do not download the data. "
    )

    dataset = None

    dates_all = pd.date_range("1995-01-01", "2018-12-01", freq="MS")

    all_datelist = DateListNormaliser(dates_all)    

    dataset_types = {"training": dates_all[dates_all.year.isin(list(np.arange(1995, 2017)))],
                     "validation": dates_all[dates_all.year.isin([2017])],
                     "testing": dates_all[dates_all.year.isin([2018])]}

    default_datelist = dataset_types["training"]

    def __init__(self, months: List = None, dataset: str = None):
        """
        Initialize data loader instance
        :param months: list of months for which downscaling data is requested
        :param dataset: name of dataset (see dataset_types-dictionary)
        """
        self.dataset = dataset

        assert not (months is None and dataset is None), "Either list of months or dataset-name must be passed."

        if (not dataset is None) and (not months is None):
            print("List of months and dataset-name cannot be processed simultaneously. months will be ignored.")

        if dataset is None:
            self.date = self.parse_date(months)
        else:
            if not dataset in self.dataset_types.keys():
                raise ValueError("Unknown dataset type {0} passed. Valid choices are [{1}]"
                                 .format(dataset, ",".join(self.dataset_types.keys())))
            self.date = self.parse_date(self.dataset_types[dataset])
        
        # get the requested data
        self._load()

    def _load(self):
        """
        Builds the URL-request and retrieves the data
        :return: -
        """
        request_dict = dict(url=URL, date=self.date)
        self.source = cml.load_source("url-pattern", PATTERN, request_dict, merger=Merger(self.dataset))

    def parse_date(self, dates: List_or_string):
        """
        Parse individual date or list of dates for downscaling dataset
        :param dates: list of dates (months) or individual month
        :return: normalized date string suitable for requiring downscaling data
        """
        if dates is None:
            dates = self.default_datelist
        
        dates = DateListNormaliser(dates)
        
        check_date = [d for d, date in enumerate(dates) if date not in self.all_datelist]
        if check_date:
            print("The following passed months are not available in the dataset:")
            for index in check_date:
                print("* {0}".format(dates[index]))
            raise ValueError("Unavailable months requested. Check your input.")

        return dates

class Merger:
    def __init__(self, dataset: str, engine: str = "netcdf4", options=None):
        """Initializes merger based on xarray's open_mfdataset.
        :param engine: Engine to read netCDF-files (see open_mfdataset-documentation for more details).
        :param options: Additional options passed to open_mfdataset.
        :return: -
        """
        self.dataset = dataset
        self.engine = engine
        self.options = options if options is not None else {}

    def to_xarray(self, paths: List, persist: bool=False, data_dir: str=None):
        """
        Merger to read data from multiple netCDF-files
        :param paths: list containing paths to netCDF-data files to be read
        :param persist: boolean to save data persistently to disk (in addition to caching)
        :param data_dir: directory under which data will be saved persistently
        :return: the data as xarray.Dataset
        """
        # read all files to provide xarray dataset
        ds_all = xr.open_mfdataset(paths, engine=self.engine, parallel=True, **self.options)
        
        # save data to disk if desired
        if persist:
            try:
                os.makedirs(data_dir, exist_ok=True)
            except TypeError as e:
                print(f"Please parse a proper directory-path data_dir")
                raise
            
            if self.dataset == "training":
                nfiles = len(paths)
                
                for i, path in enumerate(paths):
                    ds = xr.open_dataset(path, chunks=-1)
                    time0 = pd.to_datetime(ds["time"][0].values)

                    fname_tar = os.path.join(data_dir, f"downscaling_tier2_train_{time0.strftime('%Y-%m')}.nc")

                    shutil.copy(path, fname_tar)
                    print(f"Persistently saved file for {self.dataset} under {fname_tar} ({i}/{nfiles})")
            else:
                fname_tar = os.path.join(data_dir, f"downscaling_tier1_{self.dataset.replace('ing', '').replace('idation', '')}.nc")

                ds_all.to_netcdf(fname_tar, engine=self.engine)
                print(f"Persistently saved data for {self.dataset} under {fname_tar}")
            
        return ds_all
