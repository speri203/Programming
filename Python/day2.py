def solve(meal_cost, tip_percent, tax_percent):
    print(
        "{}".format(
            round(
                meal_cost
                + (meal_cost * tip_percent / 100)
                + (meal_cost * tax_percent / 100)
            )
        )
    )


meal_cost = float(input())
tip_percent = int(input())
tax_percent = int(input())

solve(meal_cost, tip_percent, tax_percent)
