def solve(meal_cost, tip_percent, tax_percent):
    return round((meal_cost) + (tip_percent*meal_cost/100) + (tax_percent*meal_cost/100))

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    print(solve(meal_cost, tip_percent, tax_percent))
