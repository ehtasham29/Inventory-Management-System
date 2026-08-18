import handlers
import validators
import user_interface

def run_menu(title, menu_data):
    while True:
        user_interface.main_messages(title, "-")
        
        for key, value in menu_data.items():
            print(f"[{key}] {value['name']}")
            
        choice = validators.get_valid_choice("\nEnter choice: ", menu_data.keys())

        if choice == 0:
            break
        
        action_function = menu_data[choice]['action']

        if action_function:
            action_function() 
        else:
            print(f"\n[!] Feature '{menu_data[choice]['name']}' is under development.")


def open_manage_products():
    run_menu("MANAGE PRODUCTS", manage_product_dict)

def open_manage_stock():
    run_menu("MANAGE STOCK", manage_stock_dict)

def open_search_product():
    run_menu("FILTER STOCK", search_product_dict)

def open_transaction_history():
    run_menu("TRANSACTION HISTORY", transaction_dict)
    

actions_dict = {
    1: {'name': 'Manage Products', 'action': open_manage_products},
    2: {'name': 'Manage Stock', 'action': open_manage_stock},
    3: {'name': 'View Inventory', 'action': handlers.view_inventory}, 
    4: {'name': 'Search Products', 'action': open_search_product},
    5: {'name': 'View Transaction History', 'action': open_transaction_history},
    6: {'name': 'View Low Stock Alerts', 'action': handlers.view_low_stock},
    7: {'name': 'System & Data Management', 'action': handlers.system_management},
    0: {'name': 'Exit', 'action': None}
}

manage_product_dict = {
    1: {'name': 'Add New Product', 'action': handlers.add_products},
    2: {'name': 'View Product Details', 'action': handlers.view_product_details},
    3: {'name': 'Update Product', 'action': handlers.update_product},
    4: {'name': 'Delete Product', 'action': handlers.delete_products},
    0: {'name': 'Back to Main Menu', 'action': None}
}

manage_stock_dict = {
    1: {'name': 'Stock In', 'action': handlers.stock_in},
    2: {'name': 'Stock Out', 'action': handlers.stock_out},
    3: {'name': 'Stock Adjustment', 'action': handlers.stock_adjustment},
    0: {'name': 'Back to Main Menu', 'action': None}
}

search_product_dict = {
    1 :{'name' : 'Product Name', 'action' : handlers.search_product_name},
    2 :{'name' : 'Product ID', 'action' : handlers.search_product_id},
    3 :{'name' : 'Product Category', 'action' : handlers.search_product_category},
    0 :{'name' : 'Back to Main Menu', 'action' : None}
}

transaction_dict = {
    1 :{'name' : 'View All Recent Transactions (Last 50)', 'action' : handlers.recent_transactions},
    2 :{'name' : 'Filter by Product ID', 'action' : handlers.transaction_by_prod_id},
    3 :{'name' : 'Filter by Action Type (STOCK IN, STOCK OUT, ADJUST)', 'action' : handlers.transaction_action_type},
    0 :{'name' : 'Back to Main Menu', 'action' : None}
    }

# 4. START THE APP
if __name__ == "__main__":
    user_interface.main_messages("WELCOME TO INVENTORY MANAGEMENT SYSTEM")
    print("Welcome Ehte!\nSystem Status: Online")
    
    # Just call the engine ONCE with the main menu dictionary!
    run_menu("MAIN MENU", actions_dict)
    
    user_interface.main_messages("INVENTORY MANAGEMENT SYSTEM CLOSING...")