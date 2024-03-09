from django.db import models

class Clients(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    pfp = models.ImageField()

class Employees(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    pfp = models.ImageField()

class Categories(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=150)

class Products(models.Model):
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    qtd = models.IntegerField()
    description = models.CharField(max_length=150)
    price = models.IntegerField()
    stars = models.IntegerField()
    details = models.JSONField()
    visualization_image = models.ImageField()
    images = models.JSONField()

class Categories_Products(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)

class Comments(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    client_id = models.ForeignKey(Clients, on_delete=models.CASCADE)

class Cart(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    client_id = models.ForeignKey(Clients, on_delete=models.CASCADE)
    qtd = models.IntegerField()