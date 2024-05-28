import pathlib
from typing import Iterator, Optional, Union

import pandas as pd


def import_from_directory(
    root: str, levels: list[str] = ["Experiment"], file_extension: str = "csv"
) -> pd.DataFrame:
    """Reads FACS data files from a nested directory and returns a dataframe.

    Use an empty string for a level to prevent adding this level as a new column to the
    dataframe.

    The length of 'levels' corresponds to the depth of subdirectories that is walked
    down to reach the folder from which FACS data files are imported.

    Args:
        root: Root directory for importing FACS data files.
        levels: Default ["Experiment"]. A list of strings that represent the
            subdirectory structure of the specified root directory. The first entry
            corresponds to the root directory. Each level is added as a new column to
            the imported data and filled with the actual folder name.
        file_extension: File extension to identify FACS data files. Must not contain the
            dot that separates filename from file extension.

    Returns:
        A dataframe containing all imported data.
    """
    if not file_extension.startswith("."):
        file_extension = f".{file_extension}"

    target_subdir_depth = len(levels) - 1

    dataframes = []
    for path_entry, subdir_depth in _iterdir(root):
        if (
            subdir_depth == target_subdir_depth
            and path_entry.suffix.lower() == file_extension
        ):
            dataframe = import_facs_csv(path_entry)
            for pos, column in enumerate(levels[::-1]):
                if column:
                    dataframe[column] = path_entry.parents[pos].name
            dataframes.append(dataframe)

    if dataframes:
        data = pd.concat(dataframes)
    else:
        data = pd.DataFrame()
    return data


def import_facs_csv(filepath: str) -> pd.DataFrame:
    """Reads FACS data from a CSV file and returns a dataframe.

    Note that also also other value delimiters are allowed, such as tab, because the
    delimiter is automatically detected by the pandas.read_csv() function.

    Args:
        filepath: Path of CSV file containing FACS data.

    Returns:
        A dataframe containing FACS data. Also adds the column "Filename", containing
        the filename without the file extension.
    """
    filepath = pathlib.Path(filepath)
    data = pd.read_csv(filepath)
    data["Filename"] = filepath.stem
    return data


def infer_setup_from_filename(
    data: pd.DataFrame,
    strip: Union[list[str], str] = ["export_", "_Singlets"],
    inplace: bool = False,
) -> Optional[pd.DataFrame]:
    """Infers condition and replicate from filenames and adds them to the dataframe.

    To extract condition and replicate, entries from the "Filename" column are split at
    the last underscore, with the first part being used as the condition and the last
    part as the replicate. Inferred values are added as new columns "Condition" and
    "Replicate". Filename entries should not contain file extensions.

    Args:
        data: Dataframe containing a column "Filename", which is used for inferring the
            experimental condition and the replicate.
        strip_filename: String or list of strings that will be removed from the filename
            before replicate and condition are extracted.
        inplace: Default False. If True, performs operation inplace and returns None.

    Returns:
        A copy of the dataframe containing the additional columns "Condition" and
        "Replicate".
    """
    strip = [strip] if isinstance(strip, str) else strip
    filename_mapping = {f: f for f in data["Filename"].unique()}
    for string in strip:
        for filename, mapping in filename_mapping.items():
            filename_mapping[filename] = mapping.replace(string, "")
    replicate_mapping = {}
    condition_mapping = {}
    for filename, mapping in filename_mapping.items():
        replicate_mapping[filename] = mapping.split("_")[-1]
        condition_mapping[filename] = "_".join(mapping.split("_")[:-1])
    replicates = [replicate_mapping[filename] for filename in data["Filename"]]
    conditions = [condition_mapping[filename] for filename in data["Filename"]]

    if not inplace:
        data = data.copy()
        data["Replicate"] = replicates
        data["Condition"] = conditions
        return data
    else:
        data["Replicate"] = replicates
        data["Condition"] = conditions
        return None


def _iterdir(path: str, curr_subdir_depth: int = 0) -> Iterator[tuple[str, int]]:
    """Recursive iterator that returns filenames and directory depth of iteration."""
    for path_entry in pathlib.Path(path).iterdir():
        if path_entry.is_file():
            yield path_entry, curr_subdir_depth
        else:
            yield from _iterdir(path_entry, curr_subdir_depth=curr_subdir_depth + 1)
