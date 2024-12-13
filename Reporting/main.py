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
    plt.plot(income, label="Income")
    plt.plot(expenses, label="Expenses")
    plt.legend()
    plt.show()

def plot_category_expenses():
    pass