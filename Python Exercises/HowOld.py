from datetime import date
birth_date = date(1986, 5, 27)
today = date.today()
delta = today - birth_date
years = delta.days // 365
months = (delta.days % 365) // 30
print("You are", years, "years and", months, "months old.")
