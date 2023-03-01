def junk():
    return 0

try:
    print(junk)
except:
    print("Bad input")
else:
    print ("execution continues!")
finally:
    print("runs no matter what.")
