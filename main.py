import inventory_manager
import validators

def greetings(message, symbol="=", width=50):
    print("\n" + symbol * width)
    print(f" {message} ".center(width, symbol))
    print(symbol * width)

def run_menu(title, menu_data):
    while True:
        greetings(title, "-")
        
        for key, value in menu_data.items():
            print(f"[{key}] {value['name']}")
            
        choice = validators.get_valid_choice("\nEnter choice: ", len(menu_data))
        
        selected_name = menu_data[choice]['name']
        if selected_name in ["Exit", "Back to Main Menu"]:
            break 
        
        action_function = menu_data[choice]['action']

        if action_function:
            action_function()
        else:
            print(f"\n[!] Feature '{selected_name}' is under development.")


def open_manage_products():
    run_menu("MANAGE PRODUCTS", manage_product_dict)

def open_manage_stock():
    run_menu("MANAGE STOCK", manage_stock_dict)


actions_dict = {
    1: {'name': 'Manage Products', 'action': open_manage_products},
    2: {'name': 'Manage Stock', 'action': open_manage_stock},
    3: {'name': 'View Inventory', 'action': None}, # None used as a placeholder for now
    4: {'name': 'Search Products', 'action': None},
    5: {'name': 'View Transaction History', 'action': None},
    6: {'name': 'View Low Stock Alerts', 'action': None},
    7: {'name': 'System & Data Management', 'action': None},
    0: {'name': 'Exit', 'action': None}
}

manage_product_dict = {
    1: {'name': 'Add New Product', 'action': inventory_manager.add_product},
    2: {'name': 'View Product Details', 'action': inventory_manager.view_product_details},
    3: {'name': 'Update Product', 'action': inventory_manager.update_product},
    4: {'name': 'Delete Product', 'action': inventory_manager.delete_product},
    0: {'name': 'Back to Main Menu', 'action': None}
}

manage_stock_dict = {
    1: {'name': 'Stock In', 'action': inventory_manager.stock_in},
    2: {'name': 'Stock Out', 'action': inventory_manager.stock_out},
    3: {'name': 'Stock Adjustment', 'action': inventory_manager.stock_adjustment},
    0: {'name': 'Back to Main Menu', 'action': None}
}

# inventory = {1 :{'name' : 'Add New Product', 'action' : inventory_manager.add_product},
#            2 :{'name' : 'View Product Details', 'action' : inventory_manager.add_product},
#            3 :{'name' : 'Update Product', 'action' : inventory_manager.add_product},
#            4 :{'name' : 'Delete Product', 'action' : inventory_manager.add_product},
#            5 :{'name' : 'Back to Main Menu', 'action' : inventory_manager.add_product}}

# transaction_history = {1 :{'name' : 'Add New Product', 'action' : inventory_manager.add_product},
#            2 :{'name' : 'View Product Details', 'action' : inventory_manager.add_product},
#            3 :{'name' : 'Update Product', 'action' : inventory_manager.add_product},
#            4 :{'name' : 'Delete Product', 'action' : inventory_manager.add_product},
#            5 :{'name' : 'Back to Main Menu', 'action' : inventory_manager.add_product}}

# data_management = {1 :{'name' : 'Add New Product', 'action' : inventory_manager.add_product},
#            2 :{'name' : 'View Product Details', 'action' : inventory_manager.add_product},
#            3 :{'name' : 'Update Product', 'action' : inventory_manager.add_product},
#            4 :{'name' : 'Delete Product', 'action' : inventory_manager.add_product},
#            5 :{'name' : 'Back to Main Menu', 'action' : inventory_manager.add_product}}

# 4. START THE APP
if __name__ == "__main__":
    greetings("WELCOME TO INVENTORY MANAGEMENT SYSTEM")
    print("Welcome Ehte!\nSystem Status: Online")
    
    # Just call the engine ONCE with the main menu dictionary!
    run_menu("MAIN MENU", actions_dict)
    
    greetings("INVENTORY MANAGEMENT SYSTEM CLOSING...")