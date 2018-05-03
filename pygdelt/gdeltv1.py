"""Has all data and utility functions for dealing with
GDELT data version 1.0
"""

import os

import requests as rq
from tqdm import tqdm

_DATA_DIR = 'pygdelt/data'


def download(url, op_file='output'):
    """Download the data file

    Parameters
    ----------
    url     :   str
        URL of the file to be downloaded

    op_file :   str
        Output file name (Defaults to output.zip)

    Returns
    -------
    Path to the downloaded file
    """
    resp = rq.get(url, stream=True)
    if not os.path.exists(_DATA_DIR):
        os.makedirs(_DATA_DIR)
    pref_loc = os.path.join(_DATA_DIR, op_file + '.zip')

    with open(pref_loc, 'wb') as data_file:
        for chunk in tqdm(resp.iter_content()):
            data_file.write(chunk)

    return pref_loc


class Events(object):
    """Handles all the queyring for events table in  GDELT version 1.0"""

    def __init__(self):
        self._url = 'http://data.gdeltproject.org/events'

    def query(self, req_date):
        """Query the data for the specified datetime

        Parameters
        ----------
        req_date  :   integer
            Represents the date of the event data to download
        """
        url = "%s/%s.export.CSV.zip" % (self._url, req_date)
        f_name = download(url, req_date)

        return f_name

    def __repr__(self):
        return "PyGDELT Version1 - Events Data"
