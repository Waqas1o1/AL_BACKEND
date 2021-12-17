from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('Party', PartyViewset, basename='Party')
router.register('SalesOfficer', SalesOfficerViewset, basename='SalesOfficer')
router.register('Vender', VenderViewset, basename='Vender')
router.register('Bank', BankViewset, basename='Bank')
router.register('Product', ProductViewset, basename='Product')



urlpatterns = [
    path('', include(router.urls))
]