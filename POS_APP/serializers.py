from rest_framework import serializers
from . import models as m


class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Party
        fields = '__all__'


class SalesOfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.SalesOfficer
        fields = '__all__'


class VenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Vender
        fields = '__all__'


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Bank
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Product
        fields = '__all__'

class PurchaseProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.PurchaseProducts
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['product'] = ProductSerializer(instance.product).data
        return response
# Ledgers Serializers


class VenderLedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.VenderLedger
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['purchase'] = PurchaseSerializer(instance.purchase).data
        response['vender'] = VenderSerializer(instance.vender).data
        return response


class BankLedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.BankLedger
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['bank'] = BankSerializer(instance.bank).data
        return response


class CashLedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.CashLedger
        fields = '__all__'


class PartyLedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.PartyLedger
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['party'] = PartySerializer(instance.party).data
        return response


# UI


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Purchase
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['vender'] = VenderSerializer(instance.vender).data
        response['bank'] = BankSerializer(instance.bank).data
        products = []
        for i in m.PurchaseProducts.objects.filter(purchas=instance):
            products.append(i)
        
        response['products'] = PurchaseProductsSerializer(products,many=True).data
        return response
