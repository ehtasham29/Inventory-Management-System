import storage

def get_valid_choice(text, length) :
    while True :
        try : 
            choice = int(input(f"{text}"))
            if 0 <= choice <= length :
                return choice
            else :
                print(f"Please select number from 0 to {length} only. ")
        except ValueError :
            print("Invalid input. Please enter numbers only.")

def get_valid_strings(text, length) :
    while True :
        try : 
            valid_string = str(input(f"{text}").strip().lower())
            if len(valid_string) >= length :
                return valid_string
            else :
                print(f"Please enter strings of minimum {len} length only.")
        except ValueError :
            print("Invalid input. Please enter strings.")

def get_valid_amount(text) :
    while True : 
        try :
            amount = float(input(f"{text}"))
            if amount > 0 : 
                return float(f"{amount:.2f}")
            else :
                print(f"Please enter value greater then 0.")
        except ValueError :
            print("Invalid input. Please enter numbers.")
        
def get_valid_integer(text) :
    while True : 
        try :
            integer = int(input(f"{text}"))
            if integer > 0 : 
                return integer 
            else :
                print(f"Please select positive integer only.")
        except ValueError :
            print("Invalid input. Please enter numbers.")

def get_product_id(inventory, category) :
    prefix = category[0].upper()
    existing_numbers = []
    for item in inventory : 
        item_id = item.get("id", "")
        if item_id.startswith(prefix) :
            try :
                number_part = int(item_id[1:])
                existing_numbers.append(number_part)
            except ValueError :
                print("Invalid Error Occured")
    if existing_numbers : 
        next_number = max(existing_numbers) + 1
    else :
        next_number = 1
    return f"{prefix}{next_number:03d}"