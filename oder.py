orders = []
FILE_NAME = "orders.txt"


def load_orders():
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split(",")
                orders.append({
                    "order_id": data[0],
                    "customer_name": data[1],
                    "product": data[2],
                    "quantity": int(data[3]),
                    "status": data[4]
                })
    except FileNotFoundError:
        pass

def save_orders():
    with open(FILE_NAME, "w") as file:
        for o in orders:
            file.write(
                f"{o['order_id']},{o['customer_name']},{o['product']},{o['quantity']},{o['status']}\n"
            )


def add_order():
    print("\n➕ Add New Order")
    order_id = input("Order ID        : ")
    customer_name = input("Customer Name  : ")
    product = input("Product Name   : ")
    quantity = int(input("Quantity       : "))

    orders.append({
        "order_id": order_id,
        "customer_name": customer_name,
        "product": product,
        "quantity": quantity,
        "status": "Pending"
    })

    save_orders()
    print("\nOrder added & saved successfully!\n")

def view_orders():
    if not orders:
        print("\n❌ No orders found.\n")
        return

    print("\nAll Orders")
    print("-" * 60)
    print(f"{'ID':<10}{'Customer':<15}{'Product':<15}{'Qty':<5}{'Status'}")
    print("-" * 60)

    for o in orders:
        print(f"{o['order_id']:<10}{o['customer_name']:<15}{o['product']:<15}{o['quantity']:<5}{o['status']}")

    print("-" * 60 + "\n")

def search_order():
    oid = input("\n Enter Order ID to search: ")
    for o in orders:
        if o["order_id"] == oid:
            print("\n Order Found")
            print(o, "\n")
            return
    print("\nOrder not found.\n")

def update_order():
    oid = input("\n Enter Order ID to update: ")
    for o in orders:
        if o["order_id"] == oid:
            o["status"] = input("Enter new status: ")
            save_orders()
            print("\n Order status updated!\n")
            return
    print("\nOrder not found.\n")

def delete_order():
    oid = input("\n Enter Order ID to delete: ")
    for o in orders:
        if o["order_id"] == oid:
            orders.remove(o)
            save_orders()
            print("\n🗑 Order deleted successfully!\n")
            return
    print("\n Order not found.\n")


def menu():
    load_orders()
    while True:
        print("===== Restaurant Order Management System =====")
        print("1. Add Order")
        print("2. View Orders")
        print("3. Search Order")
        print("4. Update Order Status")
        print("5. Delete Order")
        print("6. Exit")

        choice = input("\n Enter your choice: ")

        if choice == "1":
            add_order()
        elif choice == "2":
            view_orders()
        elif choice == "3":
            search_order()
        elif choice == "4":
            update_order()
        elif choice == "5":
            delete_order()
        elif choice == "6":
            print("\n Thank you! Exiting...\n")
            break
        else:
            print("\n❌ Invalid choice. Try again.\n")

menu()
