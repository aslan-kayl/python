sandwich_orders = ['tuna', 'pastrami', 'chicken', 'pastrami', 'salmon', 'roastbeef', 'pastrami']
finished_sandwiches = []
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(f"Sorry, but we don't have pastrami at the moment.")
print(sandwich_orders)
