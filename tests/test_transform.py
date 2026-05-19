from contextlib import nullcontext
from datetime import datetime

import numpy as np
import pandas as pd
import pytest

from my_dataproc.transform import str_to_datetime, str_to_unixtime


@pytest.fixture
def sample_datetime_string_df():
    data = {
        "datetime_string": [
            "2026-05-06T11:30:12.365233",
            "2024-05-01 10:30:10.000100",
            "2024-05-01 10:30",
            "2024/05/01 10:30",
        ],
        "expected": [
            datetime(2026, 5, 6, 11, 30, 12, 365233),
            datetime(2024, 5, 1, 10, 30, 10, 100),
            datetime(2024, 5, 1, 10, 30),
            datetime(2024, 5, 1, 10, 30),
        ],
    }

    return pd.DataFrame(data)


def test_datetime_df(sample_datetime_string_df):
    for i, row in sample_datetime_string_df.iterrows():
        if i == 3:
            with pytest.raises(ValueError):
                str_to_datetime(row["datetime_string"])
        else:
            assert str_to_datetime(row["datetime_string"]) == row["expected"]


DATASTRINGS = [
    (
        "2026-05-06T11:30:12.365233",
        datetime(2026, 5, 6, 11, 30, 12, 365233),
        1778034612365233,
        nullcontext(),
    ),
    (
        "2024-05-01 10:30:10.000100",
        datetime(2024, 5, 1, 10, 30, 10, 100),
        1714527010000100,
        nullcontext(),
    ),
    ("2024-05-01 10:30", datetime(2024, 5, 1, 10, 30), 1714527000000000, nullcontext()),
    (
        "2024/05/01 10:30",
        datetime(2024, 5, 1, 10, 30),
        1714527000000000,
        pytest.raises(ValueError),
    ),
]


@pytest.mark.parametrize("time_str, expect_date, expect_unix, err_ctx", DATASTRINGS)
def test_str_to_datetime(time_str, expect_date, expect_unix, err_ctx):
    with err_ctx:
        assert str_to_datetime(time_str) == expect_date


@pytest.mark.parametrize("time_str, expect_date, expect_unix, err_ctx", DATASTRINGS)
def test_str_to_unixtime(time_str, expect_date, expect_unix, err_ctx):
    with err_ctx:
        assert str_to_unixtime(time_str) == expect_unix
