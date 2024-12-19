from main import plot_income_vs_expenses, plot_category_expenses

def test_plot_income_vs_expenses_valid():
    plot_income_vs_expenses(1000, 500)
    assert True

def test_plot_income_vs_expenses_invalid_value():
    try:
        plot_income_vs_expenses(1000, -500)
    except ValueError as ve:
        print(ve)
        assert True
        return

    assert False

def test_plot_income_vs_expenses_invalid_type():

    try:
        plot_income_vs_expenses("1000", 500)
    except ValueError as ve:
        print(ve)
        assert True
        return

    assert False

def test_plot_income_vs_expenses_invalid_none():
    try:
        plot_income_vs_expenses(None, 500)
    except ValueError as ve:
        print(ve)
        assert True
        return

    assert False

def test_plot_income_vs_expenses():
    test_plot_income_vs_expenses_valid()
    test_plot_income_vs_expenses_invalid_value()
    test_plot_income_vs_expenses_invalid_type()
    test_plot_income_vs_expenses_invalid_none()

def test_plot_category_expenses_valid():
    categories = [
        {"name": "Food", "value": 100},
        {"name": "Rent", "value": 500},
        {"name": "Utilities", "value": 150},
        {"name": "Transportation", "value": 50},
    ]

    plot_category_expenses(categories)
    assert True

def test_plot_category_expenses_invalid_value():
    categories = [
        {"name": "Food", "value": 100},
        {"name": "Rent", "value": 500},
        {"name": "Utilities", "value": 150},
        {"name": "Transportation", "value": -50},
    ]

    try:
        plot_category_expenses(categories)
    except ValueError as ve:
        print(ve)
        assert True
        return

    assert False

def test_plot_category_expenses_invalid_type():
    categories = [
        {"name": "Food", "value": 100},
        {"name": "Rent", "value": 500},
        {"name": "Utilities", "value": 150},
        "Transportation",
    ]

    try:
        plot_category_expenses(categories)
    except ValueError as ve:
        print(ve)
        assert True
        return

    assert False

def test_plot_category_expenses_invalid_key():
    categories = [
        {"name": "Food", "value": 100},
        {"name": "Rent", "value": 500},
        {"name": "Utilities", "value": 150},
        {"value": 50},
    ]

    try:
        plot_category_expenses(categories)
    except ValueError as ve:
        print(ve)
        assert True
        return

    assert False

def test_plot_category_expenses_invalid_name():
    categories = [
        {"name": "Food", "value": 100},
        {"name": 500, "value": 500},
        {"name": "Utilities", "value": 150},
        {"name": "Transportation", "value": 50},
    ]

    try:
        plot_category_expenses(categories)
    except ValueError as ve:
        print(ve)
        assert True
        return

    assert False

def test_plot_category_expensed_non_number_value():
    categories = [
        {"name": "Food", "value": 100},
        {"name": "Rent", "value": 500},
        {"name": "Utilities", "value": "150"},
        {"name": "Transportation", "value": 50},
    ]

    try:
        plot_category_expenses(categories)
    except ValueError as ve:
        print(ve)
        assert True
        return

    assert False

def test_plot_category_expenses():
    test_plot_category_expenses_valid()
    test_plot_category_expenses_invalid_value()
    test_plot_category_expenses_invalid_type()
    test_plot_category_expenses_invalid_key()
    test_plot_category_expenses_invalid_name()
    test_plot_category_expensed_non_number_value()

def run_tests():
    test_plot_income_vs_expenses()
    test_plot_category_expenses()

if __name__ == "__main__":
    run_tests()