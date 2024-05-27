"""
Holds the function to get a Comtrade object which can be used to access data in np arrays.
The data is parsed using the C# parser.
Memory is tentatively kept to a minimum. One can use the sparse reading to improve it.
"""

import sys
from dataclasses import dataclass
from datetime import datetime
from importlib import resources
from pathlib import Path
from typing import Dict, List, Union

import numpy as np

# have to do in this order
from pythonnet import load

load("coreclr")
import clr  # noqa: E402

with resources.path("comtrade_pysharp", "FileReader.dll") as p:
    path = str(p)
    sys.path.append(path)
    clr.AddReference(path)

# always red, unclear if there's a way to clear this.
from ReaderDll import Reader  # noqa: E402


@dataclass
class Comtrade:
    """
    Holder for data
    """

    timestamps: list[datetime]
    analog: Dict[str, np.array]
    digital: Dict[str, np.array]


def read_comtrade(
    filename: Union[str, Path],
    analog_channels: List[str] = None,
    digital_channels: List[str] = None,
) -> Comtrade:
    """
    Reads the file at filename and returns a Comtrade object containing its data
    :param filename:
    :param analog_channels: to restrict which signals to read
    :param digital_channels: to restrict which signals to read
    :return:
    """
    reader = Reader(str(filename), analog_channels, digital_channels)
    timestamps = [datetime.fromtimestamp(timestamp) for timestamp in reader.timestamps]
    analog = {}
    for n, name in enumerate(reader.analog_names):
        analog[str(name)] = np.array(reader.analog_data[n])

    digital = {}
    for n, name in enumerate(reader.digital_names):
        digital[str(name)] = np.array(reader.digital_data[n])

    reader.Clear()
    return Comtrade(
        timestamps=timestamps,
        analog=analog,
        digital=digital,
    )
