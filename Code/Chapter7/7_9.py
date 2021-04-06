sandwich_orders = ['tuna', 'vegemite', 'pastrami','bacon', 'pastrami', 'chicken', 'vegetable', 'pastrami']
print("Pastrami is sold out.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print("The final list:")
for sandwich_order in sandwich_orders:
    print(sandwich_order.title())