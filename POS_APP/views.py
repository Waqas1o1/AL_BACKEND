from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from . import serializers as s
from . import models as m

# Create your views here.


class PartyViewset(viewsets.ViewSet):
    def list(self, request):
        query_set = m.Party.objects.all()
        serializer = s.PartySerializer(
            query_set, many=True, context={'request': request})
        context = {'data': serializer.data}
        return Response(context)

    def create(self, request):
        serializer = s.PartySerializer(
            data=request.data, context={'request': request})
        serializer.is_valid()
        if serializer.errors:
            context = {"error": True, 'message': serializer.errors}
        else:
            serializer.save()
            context = {'error': False, 'message': 'Data Saved Successfully!'}
        Response(context)

    def retrieve(self, request, pk=None):
        query_set = m.Party.objects.all()
        query_set = get_object_or_404(query_set, pk=pk)
        serializer = s.PartySerializer(query_set, context={'request': request})
        data = serializer.data
        return Response({'error': False, 'message': 'Success!', 'data': data})

    def update(self, request, pk=None):
        query_set = m.Party.objects.all()
        query_set = get_object_or_404(query_set, pk=pk)
        serializer = s.PartySerializer(
            query_set, data=request.data, context={'request': request})
        serializer.is_valid()
        if serializer.errors:
            context = {"error": True, 'message': serializer.errors}
        else:
            serializer.save()
            context = {'error': False, 'message': 'Data updated Successfully!'}
        return Response(context)

    def delete(self, request, pk=None):
        query_set = m.Party.objects.all()
        party = get_object_or_404(query_set, pk=pk)
        party.delete()
        return Response({'error': False, 'message': 'Data Deleted Successfully!'})


class SalesOfficerViewset(viewsets.ViewSet):
    def list(self, request):
        query_set = m.SalesOfficer.objects.all()
        serializer = s.SalesOfficerSerializer(
            query_set, many=True, context={'request': request})
        context = {'data': serializer.data}
        return Response(context)

    def create(self, request):
        serializer = s.SalesOfficerSerializer(
            data=request.data, context={'request': request})
        serializer.is_valid()
        if serializer.errors:
            context = {"error": True, 'message': serializer.errors}
        else:
            serializer.save()
            context = {'error': False, 'message': 'Data Saved Succesfully!'}
        return Response(context)

    def retrieve(self, request, pk=None):
        query_set = m.SalesOfficer.objects.all()
        query_set = get_object_or_404(query_set, pk=pk)
        serializer = s.SalesOfficerSerializer(
            query_set, context={'request': request})
        context = {'data': serializer.data}
        return Response(context)

    def update(self, request, pk=None):
        query_set = m.SalesOfficer.objects.all()
        SalesOfficer = get_object_or_404(query_set, pk=pk)
        serializer = s.SalesOfficerSerializer(
            SalesOfficer, data=request.data,  context={'request': request})
        serializer.is_valid()
        if serializer.errors:
            context = {"error": True, 'message': serializer.errors}
        else:
            serializer.save()

            context = {'error': False, 'message': 'Data Updated Succesfully!'}
        return Response(context)

    def delete(self, request, pk=None):
        m.SalesOfficer.objects.get(id=pk).delete()
        return Response({'error': False, 'message': 'Data Deleted Succesfully.'})


class BankViewset(viewsets.ViewSet):
    def list(self, request):
        query_set = m.Bank.objects.all()
        serializer = s.BankSerializer(
            query_set, many=True, context={'request': request})
        context = {'data': serializer.data}
        return Response(context)

    def create(self, request):
        serializer = s.BankSerializer(
            data=request.data, context={'request': request})
        serializer.is_valid()
        if serializer.errors:
            context = {"error": True, 'message': serializer.errors}
        else:
            serializer.save()
            context = {'error': False, 'message': 'Data Saved Succesfully!'}
        return Response(context)

    def retrieve(self, request, pk=None):
        query_set = m.Bank.objects.all()
        query_set = get_object_or_404(query_set, pk=pk)
        serializer = s.BankSerializer(
            query_set, context={'request': request})
        context = {'data': serializer.data}
        return Response(context)

    def update(self, request, pk=None):
        query_set = m.Bank.objects.all()
        bank = get_object_or_404(query_set, pk=pk)
        serializer = s.BankSerializer(
            bank, data=request.data,  context={'request': request})
        serializer.is_valid()
        if serializer.errors:
            context = {"error": True, 'message': serializer.errors}
        else:
            serializer.save()

            context = {'error': False, 'message': 'Data Updated Succesfully!'}
        return Response(context)

    def delete(self, request, pk=None):
        m.Bank.objects.get(id=pk).delete()
        return Response({'error': False, 'message': 'Data Deleted Succesfully.'})


class VenderViewset(viewsets.ViewSet):
    def list(self, request):
        query_set = m.Vender.objects.all()
        serializer = s.VenderSerializer(
            query_set, many=True, context={'request': request})
        context = {'data': serializer.data}
        return Response(context)

    def create(self, request):
        serializer = s.VenderSerializer(
            data=request.data, context={'request': request})
        serializer.is_valid()
        if serializer.errors:
            context = {"error": True, 'message': serializer.errors}
        else:
            serializer.save()
            context = {'error': False, 'message': 'Data Saved Succesfully!'}
        return Response(context)

    def retrieve(self, request, pk=None):
        query_set = m.Vender.objects.all()
        vender = get_object_or_404(query_set, pk=pk)
        serializer = s.VenderSerializer(vender, context={'request': request})
        context = {'data': serializer.data}
        return Response(context)

    def update(self, request, pk=None):
        query_set = m.Vender.objects.all()
        vender = get_object_or_404(query_set, pk=pk)
        serializer = s.VenderSerializer(
            vender, data=request.data,  context={'request': request})
        serializer.is_valid()
        if serializer.errors:
            context = {"error": True, 'message': serializer.errors}
        else:
            serializer.save()
            context = {"error": False, 'message': 'Success Fully Saved'}
        return Response(context)

    def delete(self, request, pk=None):
        m.Vender.objects.get(id=pk).delete()
        return Response({'error': False, 'message': 'Data Deleted Successfully!'})


class ProductViewset(viewsets.ViewSet):
    def list(self, request):
        query_set = m.Product.objects.all()
        serializer = s.ProductSerializer(
            query_set, many=True, context={'request': request})
        context = {'data': serializer.data}
        return Response(context)

    def create(self, request):
        serializer = s.ProductSerializer(
            data=request.data, context={'request': request})
        serializer.is_valid()
        if serializer.errors:
            context = {"error": True, 'message': serializer.errors}
        else:
            serializer.save()
            context = {'error': False, 'message': 'Data Saved Succesfully!'}
        return Response(context)

    def retrieve(self, request, pk=None):
        query_set = m.Product.objects.all()
        Product = get_object_or_404(query_set, pk=pk)
        serializer = s.ProductSerializer(Product, context={'request': request})
        context = {'data': serializer.data}
        return Response(context)

    def update(self, request, pk=None):
        query_set = m.Product.objects.all()
        Product = get_object_or_404(query_set, pk=pk)
        serializer = s.ProductSerializer(
            Product, data=request.data,  context={'request': request})
        serializer.is_valid()
        if serializer.errors:
            context = {"error": True, 'message': serializer.errors}
        else:
            serializer.save()
            context = {"error": False, 'message': 'Success Fully Saved'}
        return Response(context)

    def delete(self, request, pk=None):
        m.Product.objects.get(id=pk).delete()
        return Response({'error': False, 'message': 'Data Deleted Successfully!'})


class PurchaseViewset(viewsets.ViewSet):

    def list(self, request):
        query_set = m.Purchase.objects.all()
        serializer = s.PurchaseSerializer(
            query_set, many=True, context={'request': request})
        context = {'data': serializer.data}
        return Response(context)

    def create(self, request):
        serializer = s.PurchaseSerializer(data=request.data, context={'request': request})
        serializer.is_valid()
        if serializer.errors:
            context = {"error": True, 'message': serializer.errors}
        else:
            products = request.data['products']
            obj = serializer.save()
            purchases_pdt_objs = [m.PurchaseProducts(purchas=obj, product=m.Product.objects.get(
                particular=pdt['particular']), rate=pdt['rate'], qty=pdt['qty']) for pdt in products]
            m.PurchaseProducts.objects.bulk_create(purchases_pdt_objs)
            
            context = {'error': False, 'message': 'Data Saved Succesfully!'}
        return Response(context)

    def retrieve(self, request, pk=None):
        query_set = m.Purchase.objects.all()
        Purchase = get_object_or_404(query_set, pk=pk)
        serializer = s.PurchaseSerializer(
            Purchase, context={'request': request})
        context = {'data': serializer.data}
        return Response(context)

    def update(self, request, pk=None):
        query_set = m.Purchase.objects.all()
        Purchase = get_object_or_404(query_set, pk=pk)
        serializer = s.PurchaseSerializer(
            Purchase, data=request.data,  context={'request': request})
        serializer.is_valid()
        if serializer.errors:
            context = {"error": True, 'message': serializer.errors}
        else:
            obj = serializer.save()
            m.PurchaseProducts.objects.filter(purchas=obj).delete()
            products = request.data['products']
            purchases_pdt_objs = [m.PurchaseProducts(purchas=obj, product=m.Product.objects.get(
                particular=pdt['particular']), rate=pdt['rate'], qty=pdt['qty']) for pdt in products]
            m.PurchaseProducts.objects.bulk_create(purchases_pdt_objs)

            context = {"error": False, 'message': 'Success Fully Saved'}
        return Response(context)

    def delete(self, request, pk=None):
        m.Purchase.objects.get(id=pk).delete()
        return Response({'error': False, 'message': 'Data Deleted Successfully!'})
