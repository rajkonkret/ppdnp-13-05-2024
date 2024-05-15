from datetime import date, datetime, timedelta

today = date.today()
print("Dzisiejsza data", today)  # Dzisiejsza data 2024-05-15

time = datetime.now()
print("Aktualny czas", time)  # Aktualny czas 2024-05-15 12:08:44.237544
print(type(time))  # <class 'datetime.datetime'>

# tomorrow = today + 1  # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
# days = 0, seconds = 0, microseconds = 0,
# milliseconds = 0, minutes = 0, hours = 0, weeks = 0
tomorrow = today + timedelta(days=1)
print("Jutro będzie", tomorrow)  # Jutro będzie 2024-05-16

print(time.time())  # 12:16:27.919201
print(today.day)  # 15

formatted_date = datetime.now().strftime("%d/%m/%Y")
print(f"Sformatowana data {formatted_date}")  # Sformatowana data 15/05/2024

formatted_time = datetime.now().strftime('%H:%M')
print(f"Sformatowany czas {formatted_time}")  # Sformatowany czas 12:19

# czas w formacie 12h
formatted_time_12h = datetime.now().strftime('%I:%M %p')
print("Czas 12h", formatted_time_12h)  # Czas 12h 12:21 PM

products = [
    {'sku': 1, 'exp_date': today, 'price': 100.0},
    {'sku': 2, 'exp_date': today, 'price': 80.0},
    {'sku': 3, 'exp_date': tomorrow, 'price': 60.0},
    {'sku': 4, 'exp_date': today, 'price': 500},
]
# print(products)
for p in products:
    # print(p)  # {'sku': 4, 'exp_date': datetime.date(2024, 5, 15), 'price': 500}
    # print(p['sku'])
    if p['exp_date'] != today:
        continue  # wróć na początek
    p['price'] *= 0.8  # price = price * 0.8
    print(f"""
Price for sku {p['sku']}
is now {p['price']}""")
    # Price
    # for sku 1
    #     is now
    #     80.0
    #
    # Price
    # for sku 2
    #     is now
    #     64.0
    #
    # Price
    # for sku 4
    #     is now
    #     400.0
