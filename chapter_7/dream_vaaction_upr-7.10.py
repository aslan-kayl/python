responses = {}
active = True
while active:
    name = input("\nWhat you name? : ")
    place = input("\nWhere would you like to spend your vacation? : ")
    responses[name] = place

    repeat = input("\nWould you like to continue the survey? (yes / no) : ")
    if repeat == 'no':
        active = False
print("     ----Poll Results----")
for name, place in responses.items():
    print(f"{name.title()} would like to go {place.title()}.")
    print(responses)
