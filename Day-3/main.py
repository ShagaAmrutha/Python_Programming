
import ecommerce_utils as eu
cart = {
    "Laptop": 55000,
    "Phone": 30000,
    "Headphones": 2000
}
eu.generate_invoice(cart, disc_percentage=10)
