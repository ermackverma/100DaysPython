h = int(input("Height? "))
if (h > 120):
    print("can ride")
    a = int(input("Age? "))
    if (a < 12):
        print("$12")
    else:
        print("$7")
else:
    print("Can't ride")


#############

h = int(input("Height? "))
if (h > 120):
    print("can ride")
    a = int(input("Age? "))
    if (a < 12):
        print("$5")
    elif (a >= 12 and a <= 18):
        print("$7")
    else:
        print("$12")
else:
    print("Can't ride")
