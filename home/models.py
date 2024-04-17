from django.contrib.auth.models import AbstractUser
from django.db import models
# from .models import Category, Subcategory

# Create your models here.


class CustomUser(AbstractUser):
    usertype = models.CharField(max_length=20)  # Add any additional fields you need


    
    def __str__(self):
       return self.email


from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

class CompanyProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=100)
    pincode = models.CharField(max_length=20)
    website = models.URLField()
    company_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)

    # Add any additional fields specific to company profiles

    def __str__(self):
        return self.company_name if self.company_name else str(self.user)
    



class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=100)
    pincode = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return str(self.user)




# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     rating = models.DecimalField(max_digits=3, decimal_places=2)
#     price_per_day = models.DecimalField(max_digits=10, decimal_places=1)
#     category = models.CharField(max_length=50, default='Uncategorized')
   
#     availability = models.BooleanField(default=True)
    
#     image = models.ImageField(upload_to='product_images/', default='default-image.jpg')

#     def __str__(self):
#         return self.name






from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=1)
    category = models.CharField(max_length=50, default='Uncategorized')
    subcategory = models.CharField(max_length=50, blank=True, null=True)
    availability = models.BooleanField(default=True)
    image = models.ImageField(upload_to='product_images/', default='default-image.jpg')
    

    def __str__(self):
        return self.name

# category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    # subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='products')
#quantity = models.PositiveIntegerField(default=1) 
# class Category(models.Model):
#     name = models.CharField(max_length=50, unique=True)

#     def __str__(self):
#         return self.name
    

# class Subcategory(models.Model):
#     name = models.CharField(max_length=50)
#     category = models.ForeignKey('Category', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'product')


class Warehouse(models.Model):
    warehouse_id = models.AutoField(primary_key=True)
    warehouse_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
      

    def __str__(self):
        return self.warehouse_name
    

class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return f"Cart for {self.user.username}"

User.profile = property(lambda u: CustomUser.objects.get_or_create(user=u)[0])
User.cart = property(lambda u: Cart.objects.get_or_create(user=u)[0])


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_id = models.CharField(max_length=100, null=True, blank=True)
    payment_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    item_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order {self.order.id}"
    

    #add drivers 

 

class Driver(models.Model):
    driver_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name


from django.db import models

class Technician(models.Model):
    tech_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    expertise = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name
    

from django.db import models
from .models import Product

class ProductBooking(models.Model):
    name = models.CharField(max_length=100, default='Default Product Name')
    start_date = models.DateField()
    end_date = models.DateField()
    driver_needed = models.BooleanField(default=False)
    technician_needed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product_name} Booking"

