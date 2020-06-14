# 0504_Workshop

![erd](C:\Users\user\house\web_aclass\online-lecture\0504\workshop\erd.PNG)



1. accounts/models.py

```python
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    age = models.IntegerField()
```



2. products/models.py

```python
from django.db import models
from django.conf import settings

class Branch(models.Model):
    branch_name = models.CharField(max_length=255)
    manager_name = models.CharField(max_length=255)
    sales = models.BigIntegerField()

class Product(models.Model):
    branch = models.ManyToManyField(Branch, through='BranchProduct', related_name='products')
    product_name = models.CharField(max_length=255)
    expiration_date = models.DateField()
    price = models.BigIntegerField()
    category = models.CharField(max_length=20)

class BranchProduct(models.Model):
    order_user = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Order', related_name='branch_products')
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stock = models.BigIntegerField()

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    branch_product = models.ForeignKey(Branch_Product, on_delete=models.CASCADE)
    quantity = models.BigIntegerField()
    purchased_at = models.DateTimeField(auto_now_add=True)

```

