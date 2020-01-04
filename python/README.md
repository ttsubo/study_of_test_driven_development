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
collected 11 items                                                                                                                         

tests/test_money.py::MoneyTest::testCurrency PASSED                                                                                  [  9%]
tests/test_money.py::MoneyTest::testEquality PASSED                                                                                  [ 18%]
tests/test_money.py::MoneyTest::testIdentityRate PASSED                                                                              [ 27%]
tests/test_money.py::MoneyTest::testMixedAddition PASSED                                                                             [ 36%]
tests/test_money.py::MoneyTest::testMultiplication PASSED                                                                            [ 45%]
tests/test_money.py::MoneyTest::testPlusReturnsSum PASSED                                                                            [ 54%]
tests/test_money.py::MoneyTest::testReduceMoney PASSED                                                                               [ 63%]
tests/test_money.py::MoneyTest::testReduceMoneyDifferentCurrency PASSED                                                              [ 72%]
tests/test_money.py::MoneyTest::testReduceSum PASSED                                                                                 [ 81%]
tests/test_money.py::MoneyTest::testSimpleAddition PASSED                                                                            [ 90%]
tests/test_money.py::MoneyTest::testSumPlusMoney PASSED                                                                              [100%]

---------- coverage: platform darwin, python 3.8.0-final-0 -----------
Name                    Stmts   Miss  Cover
-------------------------------------------
example/__init__.py         0      0   100%
example/bank.py            11      0   100%
example/expression.py       8      2    75%
example/money.py           31      0   100%
-------------------------------------------
TOTAL                      50      2    96%


============================================================ 11 passed in 0.23s ============================================================
```
