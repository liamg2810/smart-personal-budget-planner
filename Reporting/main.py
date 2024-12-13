import subprocess

try:
    import matplotlib.pyplot as plt
except ImportError:
    subprocess.check_call(["python", "-m", "pip", "install", "matplotlib"])

    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("Error installing matplotlib. Please install it manually.")
        exit(1)


def plot_income_vs_expenses(income, expenses):
    if income is None or expenses is None:
        raise ValueError("Income and expenses must be provided")
    
    if type(income) not in [int, float] or type(expenses) not in [int, float]:
        raise ValueError("Income and expenses must be numbers")

    if income < 0 or expenses < 0:
        raise ValueError("Income and expenses must be positive")

    plt.bar(0, income, label="Income")
    plt.bar(1, expenses, label="Expenses")
    plt.legend()
    plt.show()

def plot_category_expenses():
    pass