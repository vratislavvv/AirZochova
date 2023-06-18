from price_calculator import destinationcheck, srlr, tclass, contact_info, addons, datee
from udaje import sr, lr, ticketprice, meno, priezvisko, email, num, date1, date2

print("""---------------------------------------------------------------
------------------------ Air Zochova --------------------------
---------------------------------------------------------------""")

print("Welcome to the booking system of Air Zochova!")
print("Our airline is currently offering 5 direct flight connections from Bratislava (BTS) to:")
print("""1. Paris- CDG
2. London- LHR
3. Dubai- DXB
4. Miami- MIA
5. New York- JFK""")

destination = input("Where are you travelling? ")

destinationcheck(destination)

sr, lr, ticketprice = srlr(destination, sr, lr, ticketprice)

print(ticketprice)

ticketprice = tclass(sr, destination, ticketprice)

print(ticketprice)

ticketprice = addons(ticketprice)

date1, date2, ticketprice = datee(date1, date2, ticketprice)

print(ticketprice)

contact_info(meno, priezvisko, email, num)

print(date1)
print(date2)

print("""---------------------------------------------------------------
---------------------- FLIGHT TICKET --------------------------
---------------------------------------------------------------""")

print("""1. Paris- CDG
2. London- LHR
3. Dubai- DXB
4. Miami- MIA
5. New York- JFK""")
