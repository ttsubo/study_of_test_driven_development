# study_of_test_driven_development

Checking result after executing testtools

## How to test

```console
$ pytest -v --cov=example
=========================================================== test session starts ============================================================
platform darwin -- Python 3.8.0, pytest-5.3.2, py-1.8.0, pluggy-0.13.1 -- /Users/ttsubo/.pyenv/versions/3.8.0/bin/python3.8
cachedir: .pytest_cache
rootdir: /Users/ttsubo/source/study_of_test_driven_development/python, inifile: pytest.ini
plugins: cov-2.8.1
collected 1 item                                                                                                                           

tests/test_money.py::MoneyTest::testMultiplication PASSED                                                                            [100%]

---------- coverage: platform darwin, python 3.8.0-final-0 -----------
Name                  Stmts   Miss  Cover
-----------------------------------------
example/__init__.py       0      0   100%
example/dollar.py         5      0   100%
-----------------------------------------
TOTAL                     5      0   100%


============================================================ 1 passed in 0.17s =============================================================
```
