from main import plot_income_vs_expenses

def test_plot_income_vs_expenses():
    income = [100, "", 300]
    expenses = [50, "", -150]
    want_error = [False, True, True]

    for i, e, err in zip(income, expenses, want_error):
        try:
            plot_income_vs_expenses(i, e)
        except ValueError as ve:
            print(ve)
            assert err
            

    assert True

if __name__ == "__main__":
    test_plot_income_vs_expenses()