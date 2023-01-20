# Task 2

def hotel_cost(nights):
    return nights * 63

def plane_cost(city):

    if city.lower() == "london":
        return 650
    elif city.lower() == "paris":
        return 600
    elif city.lower() == "rome":
        return 550
    elif city.lower() == "berlin":
        return 580
    elif city.lower() == "new york":
        return 500
    elif city.lower() == "amsterdam":
        return 530
    elif city.lower() == "tokyo":
        return 750
    else:
        return 625

def car_rental(days):
    return days * 45

def holiday_cost(nights, city, days):

    total_cost = hotel_cost(nights) + plane_cost(city) + car_rental(days)
    print(f"The total cost of the holiday is: {total_cost}")

holiday_cost(5, "Tokyo", 4)