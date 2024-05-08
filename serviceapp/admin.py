from django.contrib import admin
from serviceapp.models import *

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display=('id','company_name','company_username','company_create_password','company_image')
admin.site.register(Company,CompanyAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=('id','company','product_name','product_color','product_features')
admin.site.register(Product,ProductAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display=('id','user_fname','user_email','user_create_password')
admin.site.register(Customer,CustomerAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display=('id','odproname','odcomname','oduserfname','odproprice')
admin.site.register(Order,OrderAdmin)
