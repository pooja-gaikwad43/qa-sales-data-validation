"""Validation rules for a sales order record (Superstore-style data)."""
from datetime import date, datetime

ALLOWED_REGIONS = {"East", "West", "Central", "South"}


def _parse_date(value):
    try:
        return datetime.strptime(str(value), "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return None


def validate_order(rec: dict) -> list:
    """Return a list of error messages. An empty list means the record is valid."""
    errors = []

    if not str(rec.get("order_id", "")).strip():
        errors.append("order_id is required")

    sales = rec.get("sales")
    if not isinstance(sales, (int, float)) or isinstance(sales, bool):
        errors.append("sales must be a number")
    elif sales < 0:
        errors.append("sales cannot be negative")

    qty = rec.get("quantity")
    if not isinstance(qty, int) or isinstance(qty, bool):
        errors.append("quantity must be a whole number")
    elif qty < 1:
        errors.append("quantity must be at least 1")

    disc = rec.get("discount")
    if not isinstance(disc, (int, float)) or isinstance(disc, bool):
        errors.append("discount must be a number")
    elif not 0 <= disc <= 1:
        errors.append("discount must be between 0 and 1")

    if rec.get("region") not in ALLOWED_REGIONS:
        errors.append("region is not valid")

    order_d = _parse_date(rec.get("order_date"))
    ship_d = _parse_date(rec.get("ship_date"))
    if order_d is None:
        errors.append("order_date is invalid")
    elif order_d > date.today():
        errors.append("order_date cannot be in the future")
    if ship_d is None:
        errors.append("ship_date is invalid")
    if order_d and ship_d and ship_d < order_d:
        errors.append("ship_date cannot be before order_date")

    return errors
