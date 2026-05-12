
## 라이브러리의 주된 용도
* ISO8601 기반 문자열을 python 에서 활용가능한 형태로 변환하는 용도
  - datetime 변환
  - microsecond (np.int64) 변환

## 프로젝트 디렉토리 구조
```
docs/
  source/
    conf.py
    getting_started.rst
    index.rst
    make.bat
    Makefile
src/
  my_dataproc/
    transform.py
tests/
  test_transform.py
Pipfile
Pipfile.lock
pyproject.toml
```
## 라이브러리 설치 방법

`pip install my_dataproc`

## 라이브러리 사용 방법
1. str_to_datetime
  * ISO8601 형식의 문자열을 datetime으로 변환
  * 사용 예시
    ```python
    from my_dataproc import transform
    transform.str_to_datetime("2024-05-01T10:31:00")
    # 결과: datetime(2024, 5, 1, 10, 31)
    ```

2. str_to_unixtime
  * ISO8601 형식의 문자열을 microsecond(np.int64)로 변환
  * 사용 예시
    ```python
    from my_dataproc import transform

    transform.str_to_unixtime("2024-05-01T10:31:00")
    # 결과: 1714527060000000
    ```
