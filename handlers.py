import logic
import validators
import user_interface
import storage

def add_products() :
    user_interface.main_messages(" 📦 ADD NEW PRODUCT",'-',40)
    print("(Type '0' or 'CANCEL' at any prompt to abort)")

    name = validators.get_valid_strings("Enter product name : ", 3)

    if str(name).upper() == 'CANCEL' or name == '0' :
        print("❌ Action canceled. Returning to menu.")
        return

    inventory = storage.load_inventory()
    category = validators.get_valid_strings("Enter category (e.g., Electronics, Grocery) : ",3)
    price = validators.get_valid_amount("Enter price (₹) : ")
    quantity = validators.get_valid_integer("Enter quantity : ")
    min_stock = validators.get_valid_integer("Enter minimum stock alert level : ")
    description = validators.get_valid_strings("Enter brief description : ", 3)
    product_id = validators.get_product_id(inventory, category)

    user_interface.main_messages("SUMMARY", "-", 20)
    print(f""" Product ID : {product_id} | Name : {name} | Category : {category} | Price : {price} | 
        Quanity : {quantity} | Min Stock Alert Level : {min_stock} | Description : {description}""")

    confirm = input("Save this product ? (Y/N) : ").upper()
    if confirm != 'Y' :
        print("❌ Action canceled")
        return 

    success = logic.add_product(
        product_id=product_id,
        name=name,
        price=price,
        category=category,
        quantity=quantity,
        min_stock_level=min_stock,
        description=description
    )

    if success:
        print(f"\n✅ Successfully added [{product_id}] {name} to inventory!")
    else:
        print("\n❌ Failed to add product. (ID might already exist).")


def delete_products():
    user_interface.main_messages("🗑️ DELETE PRODUCT",'-',40)
    print("(Type '0' or 'CANCEL' at any prompt to abort)")

    prod_id = validators.get_valid_strings("Enter product id : ", 7).upper()

    if str(prod_id).upper() == 'CANCEL' or prod_id == '0' :
        print("❌ Action canceled. Returning to menu.")
        return

    print(f"\n⚠️ WARNING: You are about to permanently delete {prod_id}.")
    confirm = input("Type 'DELETE' to confirm: ")

    if confirm == 'DELETE' :
        success, message = logic.delete_product(prod_id) 
        if success :
            print(f"\n✅ Product {prod_id} deleted successfully.")
        else:
            print(f"\n❌ Error: {message}")
    else:
        print("\n❌ Deletion canceled.")


def view_product_details():
    user_interface.main_messages("🔍 VIEW PRODUCT DETAILS", '-', 40)
    print("(Type '0' or 'CANCEL' at any prompt to abort)")

    raw_id = validators.get_valid_strings("Enter product id : ")
    prod_id = str(raw_id).upper()

    if prod_id == 'CANCEL' or prod_id == '0':
        print("❌ Action canceled. Returning to menu.")
        return

    # 2. Ask logic.py to find the product
    product_data = logic.get_product(prod_id)

    # 3. Print the results professionally
    if product_data:
        user_interface.main_messages("PRODUCT RECORD",'-', 40)
        # We use .get() here to prevent crashes if a field is missing
        print(f" ID          : {product_data.get('product_id')}")
        print(f" Name        : {product_data.get('name')}")
        print(f" Category    : {product_data.get('category')}")
        print(f" Price       : ₹{product_data.get('price'):,.2f}")
        print(f" Description : {product_data.get('description')}")
        print("-" * 40)
        
        # We can add dynamic warnings right here in the UI!
        current_stock = product_data.get('quantity', 0)
        min_stock = product_data.get('min_stock_level', 0)
        
        if current_stock == 0:
            print(f" Stock       : {current_stock} ❌ (OUT OF STOCK)")
        elif current_stock <= min_stock:
            print(f" Stock       : {current_stock} ⚠️ (LOW STOCK ALERT)")
        else:
            print(f" Stock       : {current_stock} ✅ (Healthy)")
            
        print("="*40)
        
    else:
        print(f"\n❌ Error: Product '{prod_id}' not found in database.")
        
    # Pause so the user can actually read it before the menu loops
    input("\nPress ENTER to return to the menu...")



def update_product():
    user_interface.main_messages(" ✏️  UPDATE PRODUCT DETAILS ", "-", 40)
    print("(Type '0' or 'CANCEL' at any prompt to abort)")

    prod_id = validators.get_valid_strings("Enter product id : ", 1).upper()

    if prod_id == 'CANCEL' or prod_id == '0':
        return

    product_data = logic.get_product(prod_id)
    if not product_data:
        print(f"\n❌ Error: Product '{prod_id}' not found.")
        return

    # 3. Print the safe update menu
    print("\n📋 CURRENT DETAILS:")
    print(f"[1] Name     : {product_data.get('name')}")
    print(f"[2] Category : {product_data.get('category')}")
    print(f"[3] Price    : ₹{product_data.get('price')}")
    print(f"[4] Min Stock: {product_data.get('min_stock_level')}")
    print("\n🔒 Note: Current Stock cannot be changed here. Use the 'Manage Stock' menu.")
    
    # Map their choice to the actual JSON key
    update_map = {
        1: "name",
        2: "category",
        3: "price",
        4: "min_stock_level",
        0: "cancel"
    }
    
    choice = validators.get_valid_choice("\nWhich field would you like to update? (0-4): ", update_map.keys())
    
    if choice == 0:
        print("❌ Action canceled.")
        return
        
    field_to_update = update_map[choice]
    
    # 4. Use the correct validator based on the field they chose
    print(f"\nCurrent {field_to_update.replace('_', ' ').title()}: {product_data.get(field_to_update)}")
    
    if field_to_update == "price":
        new_value = validators.get_valid_amount("Enter new price (₹): ")
    elif field_to_update == "min_stock_level":
        new_value = validators.get_valid_integer("Enter new minimum stock level: ")
    else:
        new_value = validators.get_valid_strings(f"Enter new {field_to_update}: ", 3)

    # 5. Confirm and send to Logic
    confirm = input(f"\n⚠️ Change {field_to_update} to '{new_value}'? (Y/N): ").upper()
    
    if confirm == 'Y':
        # Create the dictionary of updates to send to logic.py
        updates = {field_to_update: new_value}
        
        success, message = logic.update_product(prod_id, updates)
        if success:
            print("\n✅ Product updated successfully!")
        else:
            print(f"\n❌ Error: {message}")
    else :
        print("\n❌ Update canceled.")

def stock_in():
    print("\n[!] Stock In coming soon.")

def stock_out():
    print("\n[!] Stock Out coming soon.")

def stock_adjustment():
    print("\n[!] Stock Adjustment coming soon.")

def view_inventory():
    print("\n[!] View Inventory coming soon.")

def search_product_name():
    print("\n[!] Search by Name coming soon.")

def search_product_id():
    print("\n[!] Search by ID coming soon.")

def search_product_category():
    print("\n[!] Search by Category coming soon.")

def recent_transactions():
    print("\n[!] Recent Transactions coming soon.")

def transaction_by_prod_id():
    print("\n[!] Transactions by ID coming soon.")

def transaction_action_type():
    print("\n[!] Transactions by Type coming soon.")

def view_low_stock():
    print("\n[!] Low Stock Alerts coming soon.")

def system_management():
    print("\n[!] System Management coming soon.")