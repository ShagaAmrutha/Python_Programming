def app_discount(price, disc_percentage):
    disc_price = price - ((price * disc_percentage / 100))
    return disc_price

def app_gst(price, gst_percentage=18):
    new_price = price + ((price * gst_percentage / 100))
    return new_price

def generate_invoice(cart, disc_percentage=0, gst_percentage=18):
    subtotal = 0
    print("------ INVOICE ------")
    for product, price in cart.items():
        print(f"{product:<15}: ₹{price}")
        subtotal += price

    print("---------------------")
    print(f"Subtotal: ₹{subtotal}")

    # Proper indentation here
    if disc_percentage > 0:
        total_after_discount = app_discount(subtotal, disc_percentage)
        print(f"After {disc_percentage}% discount: ₹{total_after_discount}")
    else:
        total_after_discount = subtotal

    total_after_gst = app_gst(total_after_discount, gst_percentage)
    print(f"After {gst_percentage}% GST: ₹{total_after_gst:.2f}")
    print("---------------------")
    print("Thank you for shopping with us!")

