from django.contrib import admin
from .models import Customer 

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'cpf')
    search_fields = ('user', 'name', 'cpf')

admin.site.register(Customer, CustomerAdmin)