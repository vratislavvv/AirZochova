from price_calculator import destinationcheck, srlr

print("---------------------------------------------------------------")
print("----------------------- Air Zochova ---------------------------")
print("---------------------------------------------------------------")

print("Welcome to the booking system of Air Zochova!")
print("Our airline is currently offering 5 direct flight connections from Bratislava (BTS) to:")
print("""1. Paris- CDG
2. London- LHR
3. Dubai- DXB
4. Miami- MIA
5. New York- JFK""")

destination = input("Where are you travelling? ")

destinationcheck(destination)

srlr(destination)
