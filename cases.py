BASE = {"order_id": "CA-2024-100001", "sales": 261.96, "quantity": 2, "discount": 0.0,
        "region": "West", "order_date": "2024-03-10", "ship_date": "2024-03-14"}

def make(**over):
    r = dict(BASE); r.update(over); return r

# (id, type, description, record, expected_error_or_None)
CASES = [
 ("TC01","Positive","Valid record passes all checks",make(),None),
 ("TC02","Positive","Zero discount is accepted",make(discount=0),None),
 ("TC03","Boundary","Discount exactly 1 is accepted",make(discount=1),None),
 ("TC04","Boundary","Quantity exactly 1 is accepted",make(quantity=1),None),
 ("TC05","Boundary","Sales of 0 is accepted",make(sales=0),None),
 ("TC06","Boundary","Ship date same as order date is accepted",make(ship_date="2024-03-10"),None),
 ("TC07","Negative","Empty order_id is rejected",make(order_id=""),"order_id is required"),
 ("TC08","Negative","Blank-space order_id is rejected",make(order_id="   "),"order_id is required"),
 ("TC09","Negative","Negative sales is rejected",make(sales=-5),"sales cannot be negative"),
 ("TC10","Negative","Text in sales is rejected",make(sales="abc"),"sales must be a number"),
 ("TC11","Negative","Quantity 0 is rejected",make(quantity=0),"quantity must be at least 1"),
 ("TC12","Negative","Negative quantity is rejected",make(quantity=-3),"quantity must be at least 1"),
 ("TC13","Negative","Decimal quantity is rejected",make(quantity=2.5),"quantity must be a whole number"),
 ("TC14","Boundary","Discount just above 1 is rejected",make(discount=1.01),"discount must be between 0 and 1"),
 ("TC15","Boundary","Negative discount is rejected",make(discount=-0.1),"discount must be between 0 and 1"),
 ("TC16","Negative","Unknown region is rejected",make(region="North-East"),"region is not valid"),
 ("TC17","Negative","Missing region is rejected",make(region=None),"region is not valid"),
 ("TC18","Negative","Wrong date format is rejected",make(order_date="10/03/2024"),"order_date is invalid"),
 ("TC19","Negative","Future order date is rejected",make(order_date="2999-01-01",ship_date="2999-01-05"),"order_date cannot be in the future"),
 ("TC20","Negative","Ship date before order date is rejected",make(ship_date="2024-03-01"),"ship_date cannot be before order_date"),
]
