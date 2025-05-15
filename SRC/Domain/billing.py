# src/Domain/billing.py

def process_payment(total):
    print("\n----- Payment Options -----")
    print("1. Card")
    print("2. Cash")
    print("3. Online")

    choice = input("Choose payment method (1/2/3): ")

    if choice == "1":
        input("Enter card number: ")
        input("Enter CVV: ")
        print("Processing card payment...")
    elif choice == "2":
        print("Please pay cash to the cashier.")
    elif choice == "3":
        input("Enter UPI ID: ")
        print("Processing online payment...")
    else:
        print("Invalid payment method. Defaulting to cash.")
    
    print("Payment successful! Thank you for your order.")
process_payment(1)    
