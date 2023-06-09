import sys
from udaje import destinations, shortrange

def destinationcheck(destination):
    x = 0
    for i in range(len(destinations)):
        if destinations[i] != destination:
            if x + 1 == len(destinations):
                print("Our airline currently does not operate regular flights to the destination you entered!")
                sys.exit(100)
            else:
                x += 1
        else:
            break

def srlr(destination):
    from udaje import ticketprice

    for i in range(len(shortrange)):
        if shortrange[i] == destination:
            ticketprice += 150
            break
        else:
            ticketprice += 500
            break


#        if destination == shortrange:
#            price += 150
#        if destination == "Dubai" or destination ==


#       while destinations[i] != destination:
#           input("Our airline currently does not operate regular flights to the destination you
#           entered, please, type one of the destinations mentioned above: ")
