reservation = int(input("How long would you like to reserve a table for? "))
if reservation > 8:
    print("Sorry, you'll have to wait.")
else:
    print("You table is ready!")