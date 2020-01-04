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
collected 5 items                                                                                                                          

tests/test_money.py::MoneyTest::testCurrency PASSED                                                                                  [ 20%]
tests/test_money.py::MoneyTest::testDifferentClassEquality PASSED                                                                    [ 40%]
tests/test_money.py::MoneyTest::testEquality PASSED                                                                                  [ 60%]
tests/test_money.py::MoneyTest::testFrancMultiplication PASSED                                                                       [ 80%]
tests/test_money.py::MoneyTest::testMultiplication PASSED                                                                            [100%]

---------- coverage: platform darwin, python 3.8.0-final-0 -----------
Name                  Stmts   Miss  Cover
-----------------------------------------
example/__init__.py       0      0   100%
example/money.py         22      0   100%
-----------------------------------------
TOTAL                    22      0   100%


============================================================ 5 passed in 0.18s =============================================================
```
