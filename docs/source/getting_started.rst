Getting Start
=============
패키지 설치
-----------
.. code-block:: bash

    pip install my_dataproc

사용 예시
---------

str_to_datetime
~~~~~~~~~~~~~~~

ISO8601 형식의 시간 문자열을 datetime 형식으로 변환

.. code-block:: python

   from my_dataproc import transform

   transform.str_to_datetime("2024-05-01T10:31:00")
   # 결과: datetime(2024, 5, 1, 10, 31)

str_to_unixtime
~~~~~~~~~~~~~~~

ISO8601 형식의 시간 문자열을 micro second (np.int64)로 변환

.. code-block:: python

   from my_dataproc import transform

   transform.str_to_unixtime("2024-05-01T10:31:00")
   # 결과: 1714527060000000
