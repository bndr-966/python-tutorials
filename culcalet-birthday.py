from datetime import datetime

def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    return age

people = {}  # Dictionary to hold names and birthdates

# How number pepole
count = int(input("how person"))

for _ in range(count):
    name = input("enter name : ")
    date_str = input("entert date(like   YYYY-MM-DD): ")
    
    try:
        birthdate = datetime.strptime(date_str, "%Y-%m-%d")
        people[name] = birthdate
    except ValueError:
        print("❌ invalid date ")
        continue
                                                                            
# culcalet date
print("\n📋 old : ")
for name, birthdate in people.items():
    age = calculate_age(birthdate)
    print(f"{name}: {age} years old ")
# /////////////////////////////////////////////
