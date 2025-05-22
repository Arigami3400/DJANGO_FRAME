from django.db import models

class Product(models.Model):
    Product_image = models.ImageField(upload_to='Product_image/')
    Product_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.Product_name

class ProductModel(models.Model):
    Product_Model = models.CharField(max_length=15, unique=True)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Product}, {self.Product_Model}'


class Information(models.Model):
    P_name = models.CharField(max_length=50)
    Prise = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.DateField()
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)

