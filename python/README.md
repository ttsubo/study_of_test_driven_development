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
collected 9 items                                                                                                                          

tests/test_money.py::MoneyTest::testCurrency PASSED                                                                                  [ 11%]
tests/test_money.py::MoneyTest::testEquality PASSED                                                                                  [ 22%]
tests/test_money.py::MoneyTest::testIdentityRate PASSED                                                                              [ 33%]
tests/test_money.py::MoneyTest::testMultiplication PASSED                                                                            [ 44%]
tests/test_money.py::MoneyTest::testPlusReturnsSum PASSED                                                                            [ 55%]
tests/test_money.py::MoneyTest::testReduceMoney PASSED                                                                               [ 66%]
tests/test_money.py::MoneyTest::testReduceMoneyDifferentCurrency PASSED                                                              [ 77%]
tests/test_money.py::MoneyTest::testReduceSum PASSED                                                                                 [ 88%]
tests/test_money.py::MoneyTest::testSimpleAddition PASSED                                                                            [100%]

---------- coverage: platform darwin, python 3.8.0-final-0 -----------
Name                    Stmts   Miss  Cover
-------------------------------------------
example/__init__.py         0      0   100%
example/bank.py            13      0   100%
example/expression.py       5      1    80%
example/money.py           31      0   100%
-------------------------------------------
TOTAL                      49      1    98%


============================================================ 9 passed in 0.19s =============================================================
```
