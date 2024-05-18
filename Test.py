Temperature = int(input("What is the temperature\n"))

if Temperature < 15:
    print("It's too cold, stay inside")
elif Temperature < 30:
    print("It's a nice day, let's go outside")
else:
    print("It's too hot, stay inside")
