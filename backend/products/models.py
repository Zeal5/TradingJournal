from django.db import models
from django.utils.text import slugify
from autoslug import AutoSlugField



# Create your models here.
class Product(models.Model):
    
    title = models.CharField(max_length=50)
    content= models.TextField(max_length=150,blank=True)
    price = models.DecimalField(max_digits=15, decimal_places= 2)
    slug = AutoSlugField(populate_from='title',unique=True,null=True,default=None)

    @property
    def sale_price(self):
        return f"{(float(self.price) * 0.8):.2f}"
    
    def get_discount(self):
        return '122'
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.pk)
        self.slug = self.pk
        super(Product,self).save(*args,**kwargs)
