from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register((Party,Vender,Bank,Product,SalesOfficer,CashHead))
admin.site.register((BankLedger,PartyLedger,VenderLedger,SalesOfficerLedger,CashLedger))
admin.site.register((PurchaseProducts,Purchase))

