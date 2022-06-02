from get_currency_code import get_countries_info

url = "https://www.iban.com/currency-codes"
all_country_infos = get_countries_info(url)

print("Welcome to the Currency Trader")
print("Choose the country you want to consult the currency code for by the number from the list")

for idx, x in enumerate(all_country_infos):
    print(f"#{idx} {x['name']}")

while True:
  try:
    op = int(input("#: "))
  
    if op > 268 or op <0:
      print("This options doesn't exist, please choose a numbre from the list.")
    else:
      print(f"You chose {all_country_infos[op]['name']}")
      print(f"The currency code is: {all_country_infos[op]['currency_code']}")
      break
  except:
    print("This is not a number, please enter a number")
