# Sales Data Validation - QA Test Suite

A small QA project: test cases designed and automated with PyTest for a sales-order validation function.

## What is tested
`sales_validator.py` checks each sales record for: required order ID, numeric and non-negative sales,
whole-number quantity (min 1), discount between 0 and 1, valid region, valid order/ship dates,
no future order date, and ship date not before order date.

## Test design
20 test cases (see `test_cases.csv`) covering positive, boundary and negative scenarios,
each with ID, type, input, expected result, actual result and status.

## Run
```
pip install pytest
python -m pytest -v
```
Result: 20 passed.
