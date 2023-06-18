import random
from datetime import date
from udaje import destinations, shortrange

def destinationcheck(destination):
    while destination not in destinations:
        Ndestination = input("Our airline does not operate regular flights to the destination you've entered, please, type one of the destinations mentioned above: ")
        if Ndestination in destinations:
            destination = Ndestination
            break

def srlr(destination, sr, lr, ticketprice):
    if destination in shortrange:
        sr = True
        ticketprice += random.randint(100, 200)
    else:
        lr = True
        ticketprice += random.randint(400, 600)
    return sr, lr, ticketprice

def tclass(sr, destination, ticketprice):
    if sr is True:
        print("Flight to",destination,"is a short-range flight. In our airline, short-range flights are covered by Airbus A320 which offers ECONOMY and BUSINESS class.")
        sclass = input("Please select the class that you prefer: ")
        
        while sclass != "ECONOMY" and sclass != "BUSINESS":
            sclass = input("Please select the class that you prefer: ")

        if sclass == "BUSINESS":
            ticketprice = ticketprice * 2


    else:
        print("Flight to",destination,"is a long-range flight. In our airline, long-range flights are covered by Airbus A350 which offers ECONOMY, ECONOMY PREMIUM and BUSINESS class.")
        sclass = input("Please select the class that you prefer: ")
        
        while sclass != "ECONOMY" and sclass != "BUSINESS" and sclass != "ECONOMY PREMIUM":
            sclass = input("Please select a valid class option (ECONOMY, ECONOMY PREMIUM, or BUSINESS): ")
        
        if sclass == "BUSINESS":
            ticketprice = ticketprice * 2
        elif sclass == "ECONOMY PREMIUM":
            ticketprice = ticketprice * 1.5

    return ticketprice

def datee(date1, date2, ticketprice):
    oneret = input("Do you want ONEWAY or RETURN? ")
    
    if oneret == "ONEWAY":
        ticketprice = ticketprice * 0.75

        datum = input("Enter your departure date formatted as YYYY-MM-DD: ").split("-")
        year, month, day = [int(item) for item in datum]

        date1 = date(year, month, day)

        return date1, date2, ticketprice

    elif oneret == "RETURN":
        datum1 = input("Enter your departure date formatted as YYYY-MM-DD: ").split("-")
        year1, month1, day1 = [int(item) for item in datum1]

        date1 = date(year1, month1, day1)

        datum2 = input("Enter your departure date formatted as YYYY-MM-DD: ").split("-")
        year2, month2, day2 = [int(item) for item in datum2]

        date2 = date(year2, month2, day2)

        return date1, date2, ticketprice
    else:
        while oneret != "ONEWAY" and oneret != "RETURN":
            print("Do you want ONEWAY or RETURN? ")

def addons(ticketprice):
    print("Now, we will offer you some of our possible addons. If you would like to select any of them, type YES.")

    batozina = input("Do you want to add a checked baggage? ")
    if batozina == "YES":
        ticketprice = ticketprice * 1.2
    
    boarding = input("Do you want a priority boarding pass? ")
    if boarding == "YES":
        ticketprice = ticketprice * 1.05

    insurence = input("Do you want to insure your flight ticket? ")
    if insurence == "YES":
        ticketprice = ticketprice * 1.5

    return ticketprice

def contact_info(meno, priezvisko, email, num):
    meno = input("Name: ")
    priezvisko = input("Surname: ")
    email = input("Email: ")
    num = input("Phone number: ")

    return meno, priezvisko, email, num
