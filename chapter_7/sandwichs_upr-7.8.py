sandwich_orders = ['sandwich with tuna', 'sandwich with chicken', 'sandwich with roastbeef']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich}!")
    finished_sandwiches.append(current_sandwich)
print(sandwich_orders)
