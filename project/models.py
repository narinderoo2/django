from django.db import models

class Pizza(models.Model):
    STATUS = (
        ('Regular','Regular'),
        ('Square','Square'),
    )
    STATUS1 = (
        ('Small','Small'),
        ('Medium','Medium'),
        ('Large','Large'),
        ('Extra-Large','Extra-Large'),
        ('Party-Pizza','Party-Pizza'),
    )
    STATUS2=(
        ('Onion','Onion'),
        ('Tomato','Tomato'),
        ('Corn','Corn'),
        ('Capsicum','Capsicum'),
        ('Cheese','Cheese'),
        ('Jalapeno','Jalapeno'),
        ('Sausage','Sausage'),
        ('Mushroom','Mushroom'),
    )
    Type_of_pizza = models.CharField(max_length=32,choices=STATUS, default='Regular')
    Size_of_pizza = models.CharField(max_length=32,choices=STATUS1, default='Small')
    Topping_of_pizza = models.CharField(max_length=32,choices=STATUS2, default='Onion')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Type_of_pizza
