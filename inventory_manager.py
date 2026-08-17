import storage
import product
import validators

def add_product() :
    inventory = storage.load_data()

    name = validators.get_valid_strings("Enter product name : ", 3)
    price = validators.get_valid_amount("Enter product price : ")
    quantity = validators.get_valid_integer("Enter product quantity : ")
    category = validators.get_valid_strings("Enter product category : ", 3)
    id = validators.get_product_id(inventory,category)

    new_item = product.Product(id, name, price, quantity, category)
    inventory.append(new_item.transform_dict())
    storage.save_data(inventory)
    print("Product added successfully")

# def view_product_details() :
#     inventory = storage.load_data() 


def update_product() :
    inventory = storage.load_data()

    id = validators.get_valid_strings("Enter product id : ", 4).upper()

    for data in inventory :
        if data.get('id') == id :
            text = "What do you want to update ? \n1. Update Name \n2. Update Price \n3. Update quantity \n4. Update Category"
            choice = validators.get_valid_choice(text, 4)
            if choice == 1 :
                data['name'] = validators.get_valid_strings("Please enter updated name : ")
            elif choice == 2 :
                data['price'] = validators.get_valid_amount("Please enter updated amount : ")
            elif choice == 3 :
                data['quantity'] = validators.get_valid_integer("Please enter updated quantity : ")
            else :
                data['category'] = validators.get_valid_strings("Please enter updated category : ")
            storage.save_data(inventory)
            print(f"{data} updated successfully ")
            return
    print("Please enter valid id.")
    return

def delete_product() :
    inventory = storage.load_data()
    id = validators.get_valid_strings("Enter product id : ", 4).upper()

    for data in inventory :
            if data.get('id') == id :
                inventory.remove(data)
                storage.save_data(inventory)
                print(" Deleted successfully ")
                return 
    print("Please enter valid id.")
    return


def view_product_details() :
    inventory = storage.load_data()
    id = validators.get_valid_strings("Enter product id : ", 4).upper()

    for data in inventory :
        if data.get('id') == id :
            for key, values in data.items() :
                print(f"{key} : {values}")
            return 
    print("Please enter valid id.")
    return

def stock_in() :
    pass
def stock_out() :
    pass

def stock_adjustment() :
    pass