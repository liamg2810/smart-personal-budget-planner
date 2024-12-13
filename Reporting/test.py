from main import plot_income_vs_expenses

def test_plot_income_vs_expenses():
    income = [100, 200, 300]
    expenses = [50, 100, 150]
    plot_income_vs_expenses(income, expenses)
    assert True

if __name__ == "__main__":
    test_plot_income_vs_expenses()