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
collected 12 items                                                                                                                         

tests/test_money.py::MoneyTest::testCurrency PASSED                                                                                  [  8%]
tests/test_money.py::MoneyTest::testEquality PASSED                                                                                  [ 16%]
tests/test_money.py::MoneyTest::testIdentityRate PASSED                                                                              [ 25%]
tests/test_money.py::MoneyTest::testMixedAddition PASSED                                                                             [ 33%]
tests/test_money.py::MoneyTest::testMultiplication PASSED                                                                            [ 41%]
tests/test_money.py::MoneyTest::testPlusReturnsSum PASSED                                                                            [ 50%]
tests/test_money.py::MoneyTest::testReduceMoney PASSED                                                                               [ 58%]
tests/test_money.py::MoneyTest::testReduceMoneyDifferentCurrency PASSED                                                              [ 66%]
tests/test_money.py::MoneyTest::testReduceSum PASSED                                                                                 [ 75%]
tests/test_money.py::MoneyTest::testSimpleAddition PASSED                                                                            [ 83%]
tests/test_money.py::MoneyTest::testSumPlusMoney PASSED                                                                              [ 91%]
tests/test_money.py::MoneyTest::testSumTimes PASSED                                                                                  [100%]

---------- coverage: platform darwin, python 3.8.0-final-0 -----------
Name                    Stmts   Miss  Cover
-------------------------------------------
example/__init__.py         0      0   100%
example/bank.py            13      0   100%
example/expression.py      11      3    73%
example/money.py           35      0   100%
-------------------------------------------
TOTAL                      59      3    95%


============================================================ 12 passed in 0.22s ============================================================
```
