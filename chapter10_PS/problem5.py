# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
# and get fare information of train running under Indian Railways.

from random import randint

class Train:

    # constructor
    def __init__(self, trainNo):
        self.trainNo = trainNo

    
    #instance methods
    def bookTicket(self, fro, to):
        print(f"your ticket is booked in Train No {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Your Train {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in Train {self.trainNo} from {fro} to {to} is {randint(200, 1000)}")


a = Train(123456)
a.bookTicket("Delhi", "Mumbai")
a.getStatus()
a.getFare("Kolkata", "Chennai")