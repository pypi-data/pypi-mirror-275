import os
from datetime import datetime
from pathlib import Path

import numpy as np

from comtrade_pysharp import read_comtrade

here = Path(os.path.dirname(__file__))
data_folder = here / ".." / "data"
simple = data_folder / "data.cfg"


def test_data_types():
    data = read_comtrade(simple)

    assert len(list(data.analog.keys())) == 130
    assert list(data.analog.keys())[0] == "UR1_ARU_uGSync_A"
    assert len(list(data.digital.keys())) == 45
    assert list(data.digital.keys())[0] == "UR1_50Hz LS Q1 geschlossen"

    for key, value in data.analog.items():
        assert isinstance(key, str)
        assert isinstance(value, np.ndarray)
        for data_point in value:
            assert isinstance(data_point, np.float32)

    for key, value in data.digital.items():
        assert isinstance(key, str)
        assert isinstance(value, np.ndarray)
        for data_point in value:
            assert isinstance(data_point, np.intc)

    assert isinstance(data.timestamps, list)
    for item in data.timestamps:
        assert isinstance(item, datetime)


def test_sparse():
    data = read_comtrade(simple, analog_channels=["UR1_ARU_uGSync_A"])
    assert list(data.analog.keys()) == ["UR1_ARU_uGSync_A"]
    assert len(data.digital.keys()) == 45

    data = read_comtrade(simple, digital_channels=["UR1_50Hz LS Q1 geschlossen"])
    assert list(data.digital.keys()) == ["UR1_50Hz LS Q1 geschlossen"]
    assert len(data.analog.keys()) == 130

    data = read_comtrade(
        simple,
        analog_channels=["UR1_ARU_uGSync_A"],
        digital_channels=["UR1_50Hz LS Q1 geschlossen"],
    )
    assert list(data.analog.keys()) == ["UR1_ARU_uGSync_A"]
    assert list(data.digital.keys()) == ["UR1_50Hz LS Q1 geschlossen"]


if __name__ == "__main__":
    test_data_types()
    test_sparse()
