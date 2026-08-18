import json
import os

INVENTORY_FILE = 'inventory.json'
TRANSACTIONS_FILE = 'transactions.json'

# ==========================================
# INVENTORY STORAGE
# ==========================================

def load_inventory() :
    if not os.path.exists(INVENTORY_FILE) :
        return []
    
    try :
        with open(INVENTORY_FILE, mode='r', encoding='utf-8') as file : 
            return json.load(file)
        
    except json.JSONDecodeError:
        print("[Storage Warning] inventory.json is corrupted or empty. Starting fresh.")
        return []

def save_inventory(data_list) :
    with open(INVENTORY_FILE, mode='w', encoding='utf-8') as file :
        json.dump(data_list, file, indent=4)


# ==========================================
# TRANSACTION STORAGE
# ==========================================

def load_transactions():
    if not os.path.exists(TRANSACTIONS_FILE):
        return []
    
    try:
        with open(TRANSACTIONS_FILE, mode='r', encoding='utf-8') as file:
            return json.load(file)
        
    except json.JSONDecodeError:
        print("[Storage Warning] inventory.json is corrupted or empty. Starting fresh.")
        return []

def save_transactions(data_list):
    with open(TRANSACTIONS_FILE, mode='w', encoding='utf-8') as file:
        json.dump(data_list, file, indent=4)