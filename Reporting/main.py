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


def plot_income_vs_expenses(income: int | float, expenses: int | float) -> None:
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

def plot_category_expenses(categories: list[dict[str, int | float]]) -> None:
    if categories is None:
        raise ValueError("Categories must be provided")

    if not all(type(category) == dict for category in categories):
        raise ValueError("Categories must be dictionaries")

    if not all("name" in category and "value" in category for category in categories):
        raise ValueError("Categories must have 'name' and 'value' keys")

    if not all(type(category["name"]) == str for category in categories):
        raise ValueError("Category names must be strings")

    if not all(type(category["value"]) in [int, float] for category in categories):
        raise ValueError("Category values must be numbers")

    if not all(category["value"] >= 0 for category in categories):
        raise ValueError("Category values must be positive")


    plt.pie([category["value"] for category in categories], labels=[f"{category["name"]} - £{category['value']}" for category in categories], autopct="%1.1f%%")
    plt.show()