import json
from datetime import datetime
path=r"D:\Restaurent Management system\Vikas_Restaurent_Management_system_Py\SRC\Database\menu.json"
patho=r"D:\Restaurent Management system\Vikas_Restaurent_Management_system_Py\SRC\Database\order.json"

def load_menu():
    with open(path, "r") as f:
        return json.load(f)

def show_menu(menu):
    print("\n--- MENU ---")
    for item in menu:
        print(f"{item['id']}. {item['name']} - Half: ₹{item['half_price']} | Full: ₹{item['full_price']}")

def take_order(menu):
    orders = []
    while True:
        try:
            food_id = int(input("\nEnter the food ID you want to order: "))
            item = next((i for i in menu if i['id'] == food_id), None)
            if not item:
                print("Invalid food ID.")
                continue

            portion = input("Enter portion (half/full): ").strip().lower()
            if portion not in ["half", "full"]:
                print("Invalid portion.")
                continue

            quantity = int(input("Enter quantity: "))
            price = item['half_price'] if portion == 'half' else item['full_price']
            total_price = price * quantity

            orders.append({
                "id": item['id'],
                "name": item['name'],
                "portion": portion,
                "quantity": quantity,
                "unit_price": price,
                "total_price": total_price
            })

            more = input("Do you want to order another item? (yes/no): ").strip().lower()
            if more != "yes":
                break
        except ValueError:
            print("Invalid input. Try again.")

    return orders

def show_summary(orders):
    print("\n--- ORDER SUMMARY ---")
    grand_total = 0
    for order in orders:
        print(f"{order['name']} ({order['portion']}) x {order['quantity']} = ₹{order['total_price']}")
        grand_total += order['total_price']
    print(f"Total Amount: ₹{grand_total}")
    return grand_total

def process_payment(amount):
    method = input("\nPlease pay the bill (cash/online/card): ").strip().lower()
    if method == "cash":
        print("Payment successful by cash.")
    elif method == "online":
        number = input("Enter UPI or phone number: ")
        print("Payment successful via online.")
    elif method == "card":
        card = input("Enter card number: ")
        print("Payment successful by card.")
    else:
        print("Invalid payment method. Assuming cash.")
        method = "cash"
        print("Payment successful by cash.")
    return method

def save_order(orders, total, payment_method, filename="order.json"):
    order_summary = {
        "orders": orders,
        "total": total,
        "payment_method": payment_method,
        "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    try:
        with open(patho, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append(order_summary)

    with open(patho, "w") as f:
        json.dump(data, f, indent=4)
    print("Order saved successfully!")

def main():
    menu = load_menu()
    show_menu(menu)
    orders = take_order(menu)
    total = show_summary(orders)
    payment_method = process_payment(total)
    save_order(orders, total, payment_method)


main()
