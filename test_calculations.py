from utils.calculations import inventory_value, reorder_point, coverage_days

def test_inventory_value():
    assert inventory_value(10, 5) == 50

def test_reorder_point():
    assert reorder_point(10, 5, 20) == 70

def test_coverage():
    assert coverage_days(100, 10) == 10
