def get_day(user_info):
    day: int(input("What is the dat of your bday? "))
    user_info.append(day)

def get_month(user_info):
    month = int(input("What is the month (1-12) of your bday?"))

def get_year(user_info):
    year = int(input("What is the year of your bday?"))
    user_info.append(year)
    
def get_user_bday(user_info):
    try:   
        get_day(user_info)
        get_month(user_info)
        get_year(user_info)
        print("So your bday is", user_info)
    except ValueError:
        print("You entered incorrect data, bye!")
    
print("Hi, I will collect some info about your bday!")
user_info = []
get_user_bday(user_info)