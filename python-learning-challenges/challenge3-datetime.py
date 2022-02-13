import datetime

mstTime = datetime.datetime.now()

print(mstTime.strftime("%H"))

mstTimeSTR = mstTime.strftime("%H")

localTimeF = int(mstTimeSTR)

portland = localTimeF - 1

newyork = localTimeF + 2

london = localTimeF + 7

def checkOpen(time):
    while time > 24:
        time = time - 24
    while time < 1:
        time = time + 24
    if time > 8 and time < 17:
        return "is open!"
    else:
        return "is closed."

print("The campus in portland " + checkOpen(portland))

print("The campus in New York " + checkOpen(newyork))

print("The campus in London " + checkOpen(london))
