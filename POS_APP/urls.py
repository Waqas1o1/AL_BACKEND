from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('Party', PartyViewset, basename='Party')
router.register('SalesOfficer', SalesOfficerViewset, basename='SalesOfficer')
router.register('Vender', VenderViewset, basename='Vender')
router.register('Bank', BankViewset, basename='Bank')
router.register('Product', ProductViewset, basename='Product')
# Majore
router.register('Purchase', PurchaseViewset, basename='Purchase')
router.register('Sales', SalesViewset, basename='Sales')



urlpatterns = [
    path('', include(router.urls)),
    # Ledgers
    path('PartyLedger/<int:id>/<str:FromDate>/<str:ToDate>', PartyLedgerFilter.as_view()),
    path('VenderLedger/<int:id>/<str:FromDate>/<str:ToDate>', VenderLedgerFilter.as_view()),
    path('SalesOfficerLedger/<int:id>/<str:FromDate>/<str:ToDate>', SalesOfficerLedgerFilter.as_view()),
    path('BankLedger/<int:id>/<str:FromDate>/<str:ToDate>', BankLedgerFilter.as_view()),
    path('CashLedger/<str:FromDate>/<str:ToDate>', CashLedgerFilter.as_view()),
    # Actions
    path('RecivedPurchase/<int:id>/', RecivedPurchase),
    path('DeliveredSales/<int:id>/', DeliveredSales)
]