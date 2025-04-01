class Car:
    price = 400
    
    def __init__(self,model,year,color,for_sale):
        self.model=model
        self.year=year
        self.color=color
        self.for_sale= for_sale
    
    def get_info(self):
        return f"Model is {self.model} \nYear is {self.year} \nColor is {self.color} \nfor_sale ? {self.for_sale}"
    
    def repaint(self,new_color):
        self.color = new_color
        return f"the color is changed to {self.color}"
    
    def get_price(self):
        return f"the price is : {self.price}"
    
    def change_price(self,new_price):
        self.price = new_price
