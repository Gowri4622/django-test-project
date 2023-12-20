from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
 
# Create your models here.
class Product(models.Model):
    
    title       = models.CharField(max_length=40)          #max_length= is required
    description = models.TextField(blank=True, null=True)
    price       = models.IntegerField(null=True,default=1)
    summary     = models.TextField()
    verified    = models.BooleanField()
    created_at = models.DateTimeField()
    owner = models.ForeignKey('auth.User', related_name='products', on_delete=models.CASCADE)
   
    
    
 
    def __str__(self):
        return self.title
   
 
class writer(models.Model):
    name        = models.CharField(max_length=20)
    age         = models.IntegerField()
 
    def __str__(self):
        return self.name
 
 
class Entry(models.Model):
    product     = models.ForeignKey(Product, on_delete=models.CASCADE) #check restriction
    title       = models.CharField(max_length=20)
    date        = models.DateField()
    writer      = models.ManyToManyField(writer)
 
    def __str__(self):
        return self.title




# def save(self, *args, **kwargs):
#     lexer = get_lexer_by_name(self.language)
#     title = 'table' if self.title else False
#     options = {'title': self.title} if self.title else {}
#     formatter = HtmlFormatter(price=self.price, title=title,
#                               full=True, **options)
#     self.highlighted = highlight(self.code, lexer, formatter)
#     super().save(*args, **kwargs)

