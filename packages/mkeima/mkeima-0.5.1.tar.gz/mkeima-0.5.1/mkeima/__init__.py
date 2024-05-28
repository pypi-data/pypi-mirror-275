"""Analysis of flow cytometry-based mKeima assays in Python."""

import os.path
from typing import Optional, Union

import pandas as pd
import numpy as np

from .read import import_from_directory, import_facs_csv, infer_setup_from_filename
from .analyze import calculate_mkeima_score, summarize, summarize_outliers


__version__ = "0.5.1"
