from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "t_type", "amount", "date", "note")
    list_filter = ("t_type", "date")
    search_fields = ("note", )


