from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    brand = models.CharField(max_length = 255)
    model = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', default='static/loading.gif')
    ram = models.DecimalField(max_digits=3, decimal_places=0)
    rom = models.DecimalField(max_digits=4, decimal_places=0)
    camera = models.DecimalField(max_digits=3, decimal_places=0)
    price = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return f"{self.id} {self.brand} {self.model}"
   
class Cart(models.Model):
    username = models.CharField(max_length = 255)
    product = models.CharField(max_length = 255)
    quantity = models.DecimalField(max_digits=2, decimal_places=0)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    image = models.ImageField(default='static/loading.gif')

    def __str__(self):
        return f"{self.username} {self.product}"
    
class Order(models.Model):
    username = models.CharField(max_length = 255)
    product = models.CharField(max_length = 255)
    quantity = models.DecimalField(max_digits=2, decimal_places=0)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    image = models.ImageField(default='static/loading.gif')
    status = models.CharField(max_length = 25)

    def __str__(self):
        return f"{self.id}"
    
class Profile(models.Model):
    username = models.CharField(max_length = 255)
    name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255, null=True)
    phone = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    flat_no_building = models.CharField(max_length = 255, null=True)
    landmark = models.CharField(max_length = 255, null=True)
    locality = models.CharField(max_length = 255, null=True)
    city_state = models.CharField(max_length = 255, null=True)
    pin_code = models.DecimalField(max_digits = 10, decimal_places = 0, null=True)

    def __str__(self) :
        return f"{self.username}"
    
class Support(models.Model):
    text_choices = [
        ('p', 'password' ),
        ('d', 'delivery'),
        ('o' ,'other'),
        ]

    username = models.CharField(max_length = 255)
    order_id = models.IntegerField(null = True)
    type = models.TextField(choices = text_choices)
    query = models.TextField()
    solved = models.BooleanField(default="False", null=True)

    def __str__(self):
        return f"{self.id} {self.username}"
    
class Reviews(models.Model):
    product_id = models.IntegerField()
    name = models.CharField(max_length = 255)
    review = models.TextField()
    ratings = models.IntegerField()

    def __str__(self):
        return f"{self.product_id} {self.name}"
