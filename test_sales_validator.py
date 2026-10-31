import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import pytest
from sales_validator import validate_order
from cases import CASES

@pytest.mark.parametrize("tc_id,tc_type,desc,record,expected", CASES, ids=[c[0] for c in CASES])
def test_validate_order(tc_id, tc_type, desc, record, expected):
    errors = validate_order(record)
    if expected is None:
        assert errors == [], f"{tc_id}: expected valid, got {errors}"
    else:
        assert expected in errors, f"{tc_id}: expected '{expected}', got {errors}"
