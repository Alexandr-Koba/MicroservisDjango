"""
CREATE TABLE PRODUCTS (
    product_id INT AUTO_INCREMENT NOT NULL,
    name CHAR(255) NOT NULL,
    price FLOAT NOT NULL,

    PRIMARY KEY (product_id)
);

CREATE TABLE STAFF (
    staff_id INT AUTO_INCREMENT NOT NULL,
    full_name CHAR(255) NOT NULL,
    position CHAR(255) NOT NULL,
    labor_contract INT NOT NULL,

    PRIMARY KEY (staff_id)
);

"""


from django.db import models




# CREATE TABLE ORDERS (
#   order_id INT AUTO_INCREMENT NOT NULL,
#   time_in DATETIME NOT NULL,
#   time_out DATETIME,
#   cost FLOAT NOT NULL,
#   pickup INT NOT NULL,
#   staff INT NOT NULL,

#   PRIMARY KEY (order_id),
#   FOREIGN KEY (staff) REFERENCES STAFF (staff_id)
#);

director = 'DI'
admin = 'AD'
cook = 'CO'
cashier = 'CA'
cleaner = 'CL'

POSITIONS = [
    (director, 'Директор'),
    (admin, 'Администратор'),
    (cook, 'Повар'),
    (cashier, 'Кассир'),
    (cleaner, 'Уборщик')
]

class Staff(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=2,
                                choices=POSITIONS,
                                default=cashier)
    labor_contract = models.IntegerField()
class Order(models.Model):
    time_in = models.DateTimeField(auto_now_add = True)
    time_out = models.DateTimeField(null = True)
    cost = models.FloatField(default = 0.0)
    pickup = models.BooleanField(default = False)
    complete = models.BooleanField(default = False)
    staff = models.ForeignKey(Staff, on_delete = models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0.0)
class ProductOrder(models.Model):
    pass
