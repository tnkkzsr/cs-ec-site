from django.contrib import admin

from .models import PaymentInfo, User, User_Additional_Address

# Register your models here.
admin.site.register(User)
admin.site.register(User_Additional_Address)
admin.site.register(PaymentInfo)


