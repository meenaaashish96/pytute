#coffee customization
order_size = "Large"
extra_shot = False

if extra_shot:
    order = order_size + "coffee with extra shot"
else:
    order = order_size + " coffee"

print("Order:", order)
