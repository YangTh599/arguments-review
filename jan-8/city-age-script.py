def get_city():
    city = input("Enter the name of the city you live in:\n")
    return city

def get_age():
    age = input("Enter your age:\n")
    return age

def build_output(city,age):
    return f"You are {age} years old and live in {city.title()}."

c = get_city()
a = get_age()
print(build_output(c,a))