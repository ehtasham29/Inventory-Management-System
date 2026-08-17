class Product :
    def __init__(self, product_id, name, price, category, quantity, min_stock_level, description):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category
        self.quantity = quantity
        self.min_stock_level = min_stock_level
        self.description = description

    def to_dict(self) :
        return {
            'product_id' : self.product_id,
            'name' : self.name,
            'price' : self.price,
            'category' : self.category,
            'quantity' : self.quantity,
            'min_stock_level' : self.min_stock_level,
            'description' : self.description
        }
    
    def update_price(self, new_price) : 
        self.price = new_price

    def adjust_stock(self, amount) :
        self.quantity += amount

class Electronics(Product) :
    def __init__(self, product_id, name, price, category, quantity, min_stock_level, description, brand_name, warranty):

        super().__init__(product_id, name, price, category, quantity, min_stock_level, description)

        self.brand = brand_name
        self.warranty = warranty

    def to_dict(self):
        data = super().to_dict()
        data['brand'] = self.brand
        data['warranty'] = self.warranty
        return data

class GroceriesAndFood(Product) :
    def __init__(self,product_id, name, price, category, quantity, min_stock_level, description, expiry_date, is_perishable):

        super().__init__(product_id, name, price, category, quantity, min_stock_level, description)

        self.expiry_date = expiry_date
        self.is_perishable = is_perishable

    def to_dict(self):
        data = super().to_dict()
        data['expiry_date'] = self.expiry_date
        data['is_perishable'] = self.is_perishable
        return data

class ApparelAndClothing(Product) :
    def __init__(self, product_id, name, price, category, quantity, min_stock_level, description, brand_name, size, color, season):

        super().__init__(product_id, name, price, category, quantity, min_stock_level, description)

        self.brand = brand_name
        self.size = size
        self.color = color
        self.season = season

    def to_dict(self):
        data = super().to_dict()
        data['brand'] = self.brand
        data['size'] = self.size
        data['color'] = self.color
        data['season'] = self.season
        return data
    

class Transaction:
    def __init__(self,transaction_id, timestamp, product_id, action_type, quantity, reason):
        self.transaction_id = transaction_id
        self.timestamp = timestamp
        self.product_id = product_id
        self.action_type = action_type
        self.quantity = quantity
        self.reason = reason

    def to_dict(self) :
        return {
            'transaction_id' : self.transaction_id,
            'timestamp' : self.timestamp,
            'product_id' : self.product_id,
            'action_type' : self.action_type,
            'quantity' : self.quantity,
            'reason' : self.reason
        }