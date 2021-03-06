from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets,generics
from rest_framework.response import Response
from . import serializers as s
from . import models as m
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
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
        return Response(context)

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


class SalesViewset(viewsets.ViewSet):

    def list(self, request):
        query_set = m.Sales.objects.all()
        serializer = s.SalesSerializer(
            query_set, many=True, context={'request': request})
        context = {'data': serializer.data}
        return Response(context)

    def create(self, request):
        serializer = s.SalesSerializer(data=request.data, context={'request': request})
        serializer.is_valid()
        if serializer.errors:
            context = {"error": True, 'message': serializer.errors}
        else:
            products = request.data['products']
            obj = serializer.save()
            Saless_pdt_objs = [m.SalesProducts(sales=obj, product=m.Product.objects.get(
                particular=pdt['particular']), rate=pdt['rate'], qty=pdt['qty']) for pdt in products]
            m.SalesProducts.objects.bulk_create(Saless_pdt_objs)
            
            context = {'error': False, 'message': 'Data Saved Succesfully!'}
        return Response(context)

    def retrieve(self, request, pk=None):
        query_set = m.Sales.objects.all()
        Sales = get_object_or_404(query_set, pk=pk)
        serializer = s.SalesSerializer(
            Sales, context={'request': request})
        context = {'data': serializer.data}
        return Response(context)

    def update(self, request, pk=None):
        query_set = m.Sales.objects.all()
        Sales = get_object_or_404(query_set, pk=pk)
        serializer = s.SalesSerializer(
            Sales, data=request.data,  context={'request': request})
        serializer.is_valid()
        if serializer.errors:
            context = {"error": True, 'message': serializer.errors}
        else:
            obj = serializer.save()
            m.SalesProducts.objects.filter(sales=obj).delete()
            products = request.data['products']
            Saless_pdt_objs = [m.SalesProducts(sales=obj, product=m.Product.objects.get(
                particular=pdt['particular']), rate=pdt['rate'], qty=pdt['qty']) for pdt in products]
            m.SalesProducts.objects.bulk_create(Saless_pdt_objs)

            context = {"error": False, 'message': 'Success Fully Saved'}
        return Response(context)

    def delete(self, request, pk=None):
        m.Sales.objects.get(id=pk).delete()
        return Response({'error': False, 'message': 'Data Deleted Successfully!'})

# Ledgers

class PartyLedgerFilter(generics.ListAPIView):
    
    serializer_class = s.PartyLedgerSerializer

    def get_queryset(self):
        f_date = self.kwargs['FromDate']
        t_date = self.kwargs['ToDate']
        id = self.kwargs['id']
        ledgers  = m.PartyLedger.objects.filter(party__id=id, date__lte=t_date, date__gte=f_date)
        print(m.PartyLedger.objects.all())
        return ledgers

class SalesOfficerLedgerFilter(generics.ListAPIView):
    
    serializer_class = s.SalesOfficerLedgerSerializer

    def get_queryset(self):
        f_date = self.kwargs['FromDate']
        t_date = self.kwargs['ToDate']
        id = self.kwargs['id']
        return m.SalesOfficerLedger.objects.filter(sales_officer__id=id, date__lte=t_date, date__gte=f_date)

class BankLedgerFilter(generics.ListAPIView):
    
    serializer_class = s.BankLedgerSerializer

    def get_queryset(self):
        f_date = self.kwargs['FromDate']
        t_date = self.kwargs['ToDate']
        id = self.kwargs['id']
        return m.BankLedger.objects.filter(bank__id=id, date__lte=t_date, date__gte=f_date)

class CashLedgerFilter(generics.ListAPIView):
    
    serializer_class = s.CashLedgerSerializer

    def get_queryset(self):
        f_date = self.kwargs['FromDate']
        t_date = self.kwargs['ToDate']
        return m.CashLedger.objects.filter(date__lte=t_date, date__gte=f_date)

class VenderLedgerFilter(generics.ListAPIView):
    
    serializer_class = s.VenderLedgerSerializer

    def get_queryset(self):
        f_date = self.kwargs['FromDate']
        t_date = self.kwargs['ToDate']
        id = self.kwargs['id']
        return m.VenderLedger.objects.filter(vender__lte=id,date__lte=t_date, date__gte=f_date)

# Ledger
@api_view(['POST'])
def RecivedPurchase(request,id):
    freight = request.data['freight']
    if freight:
        p = m.Purchase.objects.get(id=id)
        p.status ='Arrived'
        p.freight = freight
        p.save()
    send_dict = {'error':False,'message':'Purchased Revied'}
    return JsonResponse(send_dict)
@api_view(['POST'])
def DeliveredSales(request,id):
    freight = request.data['freight']
    if freight:
        p = m.Sales.objects.get(id=id)
        p.status ='Delivered'
        p.freight = freight
        p.save()
    send_dict = {'error':False,'message':'Purchased Revied'}
    return JsonResponse(send_dict)