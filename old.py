from datetime import datetime
def calculat_age(birth):
    now=datetime.today()
    age=now.year-birth.year
    if(now.month,now.day)<(birth.month,birth.day): 
      age-=1
    return age
ages=[]
while True:
    cont_input = input('Enter how many people: ')
    if cont_input.isdigit():
        cont = int(cont_input)
        break
    else:
        print("❌ Please enter a valid whole number (integer only).")
 
for _ in range(cont):   
    name=input('enter your name: ')
    old_date_str = input(" enter old date (EX: YYYY-MM-DD): ")
    old_date = datetime.strptime(old_date_str, "%Y-%m-%d")

    age=calculat_age(old_date)        
    ages.append((name, age,old_date)) 
   
   

print('\n ')
ages.sort(key=lambda x: x[1], reverse=True)
oldest = max(ages, key=lambda x: x[1])
youngest = min(ages, key=lambda x: x[1])

for name, age ,birth_date in ages:
    day_name = birth_date.strftime('%A')  

    print(f"I am {name} i have {age} years old and she/he was born on ({day_name})")
if cont>1:
    print(f'👴 Oldest: {oldest[0]} ({oldest[1]} years)')
    print(f'🧒 Youngest: {youngest[0]} ({youngest[1]} years)')
print(f'total people: {cont}')
