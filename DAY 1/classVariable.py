# class Circle:
#     pi = 3.14
#     def __init__(self,radius):
#         self.radius = radius
        
        
        
#     def area(self):
#         return  Circle.pi *self.radius*self.radius    
    
#     def circumference(self):
#         return 2*Circle.pi*self.radius

# c1 = Circle(4)

# print(c1.area())



class Laptop:
    dicount_percent = 10
    def __init__(self,brand_name, model_name,price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        self.laptop_name = brand_name +' '+ model_name
        self.toatal_description = brand_name +' '+ model_name + ' ' + str(price)
    
    def discount(self):
        # new_price = self.price - (self.price * Laptop.dicount_percent/100 )
        new_price = self.price - (self.price * self.dicount_percent/100 ) 
        return new_price
        
l1 = Laptop("HP","pavilion gaming", 70000)        

l2 = Laptop("asus","asus tuf",54000)
l2.dicount_percent = 50
print(l2.discount())
print(l2.__dict__)

    