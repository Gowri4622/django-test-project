from django.contrib import admin

# Register your models here.

from .models import Product
from .models import writer
from .models import Entry


admin.site.register(Product)
admin.site.register(writer)
admin.site.register(Entry)
