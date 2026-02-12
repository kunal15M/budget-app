from budget import Category, create_spend_chart


def main():
    food = Category("Food")
    clothing = Category("Clothing")
    auto = Category("Auto")

    food.deposit(1000, "Initial deposit")
    food.withdraw(150.15, "Groceries")
    food.withdraw(50.89, "Restaurant")

    clothing.deposit(500, "Initial deposit")
    clothing.withdraw(75.55, "Clothes")

    food.transfer(50, clothing)

    print(food)
    print(clothing)

    print(create_spend_chart([food, clothing, auto]))


if __name__ == "__main__":
    main()
