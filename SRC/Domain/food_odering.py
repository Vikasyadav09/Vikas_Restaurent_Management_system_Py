import json
import os
#from billing import process_payment
path=r"D:\Restaurent Management system\Vikas_Restaurent_Management_system_Py\SRC\Database\menu.json"
patho=r"D:\Restaurent Management system\Vikas_Restaurent_Management_system_Py\SRC\Database\order.json"

def load_menu():
    with open(path, "r") as f:
        return json.load(f)

def display_menu(menu):
    print("\n--- MENU ---")
    print(f"{'ID':<5}{'Name':<20}{'Half Price':<15}{'Full Price'}")
    for item in menu:
        print(f"{item['id']:<5}{item['name']:<20}{item['half_price']:<15}{item['full_price']}")

def find_item_by_id(menu, item_id):
    for item in menu:
        if item['id'] == item_id:
            return item
    return None

def take_order():
    menu = load_menu()
    display_menu(menu)

    orders = []
    total_price = 0

    while True:
        try:
            item_id = int(input("\nEnter food ID to order: "))
            item = find_item_by_id(menu, item_id)
            if not item:
                print("❌ Please enter a correct food ID.")
                continue

            portion = input("Enter portion (half/full): ").strip().lower()
            if portion not in ['half', 'full']:
                print("❌ Invalid portion. Please enter 'half' or 'full'.")
                continue

            quantity = int(input("Enter quantity: "))
            price = item['half_price'] if portion == 'half' else item['full_price']
            item_total = price * quantity
            total_price += item_total

            orders.append({
                "id": item['id'],
                "name": item['name'],
                "portion": portion,
                "quantity": quantity,
                "unit_price": price,
                "total_price": item_total
               # "total_price":total_price,
                #"payment_status":payment_status
            })

            another = input("Do you want to order another item? (yes/no): ").strip().lower()
            if another != "yes":
                break
        except ValueError:
            print("❌ Invalid input. Please try again.")

    
    print("\n--- ORDER SUMMARY ---")
    print(f"{'ID':<5}{'Name':<20}{'Portion':<10}{'Qty':<5}{'Price':<10}{'Total'}")
    for order in orders:
        print(f"{order['id']:<5}{order['name']:<20}{order['portion']:<10}{order['quantity']:<5}{order['unit_price']:<10}{order['total_price']}")

    print(f"\nTotal Amount: ₹{total_price}")

    pay_now = input("\nDo you want to pay the bill now? (yes/no): ").strip().lower()
    if pay_now == 'yes':
        payment_method = input("Choose payment method (card/cash/online): ").strip().lower()
        if payment_method == 'card':
            card_number = input("Enter your card number: ")
            print("Processing payment...")
            print("✅ Payment successful via card. Thank you!")
        elif payment_method == 'online':
            print("📱 This is your scanner, pay on it!")
            print("✅ Payment successful via online. Thank you!")
        elif payment_method == 'cash':
            print("✅ Payment successful via cash. Thank you!")
        else:
            print("❌ Invalid payment method. Assuming cash payment.")
            print("✅ Payment successful via cash. Thank you!")
    else:
        print("😊 Thanks! You can pay after enjoying your food.")
        payment_status="Not paid"
        from billing import process_payment
  

    with open(patho, "w") as f:
        json.dump(order, f, indent=4)

    print("\n✅ Order saved to 'order.json'.")
    print("Thanku ! Visit again >")





take_order()
