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


class SalesProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.SalesProducts
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


class SalesOfficerLedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.SalesOfficerLedger
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['sales_officer'] = SalesOfficerSerializer(
            instance.sales_officer).data
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
        products = m.PurchaseProducts.objects.filter(purchas=instance)
        response['products'] = PurchaseProductsSerializer(
            products, many=True).data
        return response


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Sales
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['party'] = PartySerializer(instance.party).data
        response['salesOfficer'] = SalesOfficerSerializer(
            instance.salesOfficer).data
        response['bank'] = BankSerializer(instance.bank).data
        products = m.SalesProducts.objects.filter(sales=instance)
        response['products'] = SalesProductsSerializer(
            products, many=True).data
        return response
