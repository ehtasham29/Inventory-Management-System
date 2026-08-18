import storage
import datetime
from models import Product, Transaction

def add_product(product_id, name, price, category, quantity, min_stock_level, description="NA") :
    inventory = storage.load_inventory()
    transactions = storage.load_transactions()

    new_item = Product(product_id,name,price,category,quantity,min_stock_level,description)

    inventory.append(new_item.to_dict())

    storage.save_inventory(inventory)

    ## NEED TO CHECK FOR TRANSACTIONS
    if quantity > 0 :
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        txn_id = f"TXN-{len(transactions)+1}"

        new_txn = Transaction( 
            transaction_id = txn_id,
            timestamp = timestamp,
            product_id = product_id,
            action_type= "INITIAL_STOCK",
            quantity= quantity,
            reason= "System setup / Inital Entry"
        )
        transactions.append(new_txn.to_dict())
        storage.save_transactions(transactions)

    return True # Tell UI it worked.

def delete_product(product_id) :
    inventory = storage.load_inventory()

    for data in inventory : 
        if data.get('product_id') == product_id :
            if data.get('quantity', 0) > 0:
                return False, f"Cannot delete! There are still {data.get('quantity')} units in stock. Please do a Stock Out first."

            # If stock is 0, proceed with deletion
            inventory.remove(data)
            storage.save_inventory(inventory)
            return True, "Success"
        
    return False, "Product ID not found in database."


def get_product(product_id) :
    inventory = storage.load_inventory()

    for data in inventory :
        if data.get('product_id') == product_id : 
            return data

    return None


def update_product(product_id, updates_dict):
    inventory = storage.load_inventory()

    for data in inventory:
        if data.get('product_id') == product_id:

            for key, new_value in updates_dict.items():
                # SECURITY CHECK: Block direct quantity updates!
                if key == 'quantity':
                    return False, "Security Violation: Quantity must be changed via Stock Adjustment."
                data[key] = new_value
            storage.save_inventory(inventory)
            return True, "Success"
            
    return False, "Product ID not found."