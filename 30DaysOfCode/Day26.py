def calculate_fine(return_date, expected_date):

    return_day  = int(return_date[0])
    return_month  = int(return_date[1])
    return_year  = int(return_date[2])
    expected_day  = int(expected_date[0])
    expected_month  = int(expected_date[1])
    expected_year  = int(expected_date[2])

    fine = 0

    if return_year < expected_year:
        fine = fine
    elif return_year == expected_year:
        if return_month < expected_month:
            fine = fine
        elif return_month == expected_month:
            fine = 15 * (return_day-expected_day)
        else:
            fine = 500 * (return_month - expected_month)

    else:
        fine = 10000

    return fine
            

if __name__ == "__main__":
    return_date = input().split()
    expected_date = input().split()

    print(calculate_fine(return_date, expected_date))
