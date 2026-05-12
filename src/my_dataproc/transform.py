from datetime import datetime

import numpy as np


def str_to_datetime(time_str: str) -> datetime:
    """문자열을 datetime 타입으로 변환하는 함수

    Parameters
    ----------
    time_str: str
        ISO8061 형태의 문자열 시간 데이터

    Returns
    -------
    datetime
        datetime 으로 변경된 데이터

    Examples
    --------
    >>> str_to_datetime('2024-05-01T10:31:00')
    datetime(2024, 5, 1, 10, 31)
    """
    temp_datetime = datetime.fromisoformat(time_str)
    if temp_datetime > datetime.now():
        raise ValueError(f"{temp_datetime} is future datetime. It's not allowed")
    return temp_datetime


def str_to_unixtime(time_str: str) -> np.int64:
    """문자열 시간 데이터를 마이크로초로 변환하는 함수
    Parameters
    ----------
    time_str: str
        ISO8061 형태의 문자열 시간 데이터

    Returns
    -------
    np.int64
        마이크로초 데이터

    Examples
    --------
    >>> str_to_unixtime("2024-05-01T10:31:00")
    1714527060000000
    """
    datetime_value = str_to_datetime(time_str)
    unix_time = np.int64(datetime_value.timestamp() * 1_000_000)
    return unix_time


if __name__ == "__main__":
    temp_timedate = str_to_unixtime("2024-05-01T10:31:00")
    temp_unixtime = str_to_unixtime("2024-05-01T10:31:00")
    print(temp_timedate, temp_unixtime)
