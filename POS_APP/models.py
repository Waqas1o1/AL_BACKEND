from django.db import models
from django.utils import timezone
from .utils.utils import UpdateLeadgers, DeleteLeadgers
# Create your models here.


class SalesOfficer(models.Model):
    name = models.CharField(max_length=200, unique=True)
    commission = models.FloatField(default=0.0)
    contact = models.CharField(max_length=13)
    cnic = models.CharField(max_length=18) 
    opening_Balance = models.FloatField()
    current_Balance = models.FloatField(blank=True, null=True)

    date = models.DateField(default=timezone.now, blank=True)

    def save(self, *args, **kwargs):
        if self.id == None:
            self.current_Balance = self.opening_Balance
        super(SalesOfficer, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Party(models.Model):
    name = models.CharField(max_length=500,unique=True)
    cnic = models.CharField(max_length=20, null=True, blank=True)
    contact = models.CharField(max_length=11, null=True, blank=True)
    opening_Balance = models.FloatField()
    current_Balance = models.FloatField(blank=True, null=True)

    date = models.DateField(default=timezone.now, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.id == None:
            self.current_Balance = self.opening_Balance
        super(Party, self).save(*args, **kwargs)


class Bank(models.Model):
    name = models.CharField(max_length=30, unique=True)
    account_no = models.CharField(max_length=400)
    opening_Balance = models.FloatField()
    current_Balance = models.FloatField(blank=True, null=True)

    date = models.DateField(default=timezone.now, blank=True)

    def save(self, *args, **kwargs):
        if self.id == None:
            self.current_Balance = self.opening_Balance

        super(Bank, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Vender(models.Model):
    name = models.CharField(max_length=500, blank=False, null=False)
    address = models.CharField(max_length=1000, blank=True, null=True)
    contact = models.CharField(max_length=11, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    attachments = models.FileField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CashHead(models.Model):
    name = models.CharField(max_length=30, unique=True)
    # Opening
    opening_Balance = models.FloatField()
    current_Balance = models.FloatField(blank=True, null=True)

    date = models.DateField(default=timezone.now, blank=True)

    def save(self, *args, **kwargs):
        if self.id == None:
            self.current_Balance = self.opening_Balance

        super(CashHead, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    particular = models.CharField(max_length=300, unique=True)
    model_no = models.CharField(max_length=100)
    capasity = models.IntegerField(blank=True)
    unit = models.CharField(max_length=300)
    size = models.CharField(max_length=300,default='40 MG')
    cost_price = models.IntegerField()
    sale_price = models.IntegerField()
    date = models.DateField(default=timezone.now, blank=True)
    def __str__(self) -> str:
        return self.particular
# Ledgers


class Ledger(models.Model):
    date = models.DateField(default=timezone.now, blank=True)
    description = models.CharField(max_length=300000, null=True)
    transaction_type = models.CharField(max_length=50, choices=(
        ('Debit', 'Debit'), ('Credit', 'Credit')))
    total_amount = models.FloatField(null=True)
    net_balance = models.FloatField(blank=True, default=0.0)

    def __str__(self):
        return str(self.id)


class BankLedger(Ledger):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)

    def __str__(self):
        return self.bank.name

    def save(self, *args, **kwargs):
        if self.id == None:
            if self.transaction_type == 'Credit':
                self.bank.current_Balance -= self.total_amount
                self.net_balance = self.bank.current_Balance
            else:
                self.bank.current_Balance += self.total_amount
                self.net_balance = self.bank.current_Balance
            self.bank.save()
            super(BankLedger, self).save(*args, **kwargs)
        else:
            up = kwargs.pop('updating', {})
            obj = self
            if up == {}:
                obj = UpdateLeadgers(self, BankLedger, 'Bank', True)
                obj.total_amount = self.total_amount

            super(BankLedger, obj).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        up = kwargs.pop('updating', {})
        if up == {}:
            DeleteLeadgers(self, BankLedger, 'Bank', True)
        else:
            super(BankLedger, self).delete()


class CashLedger(Ledger):
    cash_head = models.ForeignKey(CashHead, on_delete=models.CASCADE)

    def __str__(self):
        return self.cash_head.name

    def save(self, *args, **kwargs):
        if self.id == None:
            ch = CashHead.objects.all()
            if not ch:
                ch = CashHead(name='CashHead').save()   
            else:
                ch.first()
            if self.transaction_type == 'Credit':
                self.cash_head.current_Balance -= self.total_amount
                self.net_balance = self.cash_head.current_Balance
            else:
                self.cash_head.current_Balance += self.total_amount
                self.net_balance = self.cash_head.current_Balance
            
            self.cash_head.save()
            super(CashLedger, self).save(*args, **kwargs)
        else:
            up = kwargs.pop('updating', {})
            obj = self
            if up == {}:
                obj = UpdateLeadgers(self, CashLedger, 'Cash', True)
                obj.total_amount = self.total_amount

            super(CashLedger, obj).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        up = kwargs.pop('updating', {})
        if up == {}:
            DeleteLeadgers(self, CashLedger, 'Cash', True)
        else:
            super(CashLedger, self).delete()


class PartyLedger(Ledger):
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    sales_officer = models.ForeignKey(
        SalesOfficer, on_delete=models.CASCADE, null=True, blank=True)
    freight = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.party.name + str(self.id)

    def save(self, *args, **kwargs):
        if self.id == None:
            if self.transaction_type == 'Credit':
                self.party.current_Balance -= self.total_amount
                self.net_balance = self.party.current_Balance
            else:
                self.party.current_Balance += self.total_amount
                self.net_balance = self.party.current_Balance
            self.party.save()
            super(PartyLedger, self).save(*args, **kwargs)
        else:
            up = kwargs.pop('updating', {})
            obj = self
            if up == {}:
                obj = UpdateLeadgers(self, PartyLedger, 'Party', True)
                obj.total_amount = self.total_amount

            super(PartyLedger, obj).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        up = kwargs.pop('updating', {})
        if up == {}:
            DeleteLeadgers(self, PartyLedger, 'Party', True)
        else:
            super(PartyLedger, self).delete()


class VenderLedger(Ledger):
    sales_officer = models.ForeignKey(Vender, on_delete=models.CASCADE)
    purchases = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.sales_officer.name + str(self.id)

    def save(self, *args, **kwargs):
        if self.id == None:
            if self.transaction_type == 'Credit':
                self.sales_officer.current_Balance -= self.total_amount
                self.net_balance = self.sales_officer.current_Balance
            else:
                self.sales_officer.current_Balance += self.total_amount
                self.net_balance = self.sales_officer.current_Balance
            self.sales_officer.save()

            super(VenderLedger, self).save(*args, **kwargs)
        else:
            up = kwargs.pop('updating', {})
            obj = self
            if up == {}:
                obj = UpdateLeadgers(self, VenderLedger, 'Vender', True)
                obj.description = self.description
                obj.total_amount = self.total_amount

            super(VenderLedger, obj).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        up = kwargs.pop('updating', {})
        if up == {}:
            DeleteLeadgers(self, VenderLedger, 'Vender', True)
        else:
            super(VenderLedger, self).delete()


class SalesOfficerLedger(Ledger):
    sales_officer = models.ForeignKey(SalesOfficer, on_delete=models.CASCADE)
    party_order = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.sales_officer.name + str(self.id)

    def save(self, *args, **kwargs):
        if self.id == None:
            if self.transaction_type == 'Credit':
                self.sales_officer.current_Balance -= self.total_amount
                self.net_balance = self.sales_officer.current_Balance
            else:
                self.sales_officer.current_Balance += self.total_amount
                self.net_balance = self.sales_officer.current_Balance
            self.sales_officer.save()

            super(SalesOfficerLedger, self).save(*args, **kwargs)
        else:
            up = kwargs.pop('updating', {})
            obj = self
            if up == {}:
                obj = UpdateLeadgers(
                    self, SalesOfficerLedger, 'SalesOfficer', True)
                obj.description = self.description
                obj.total_amount = self.total_amount

            super(SalesOfficerLedger, obj).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        up = kwargs.pop('updating', {})
        if up == {}:
            DeleteLeadgers(self, SalesOfficerLedger, 'SalesOfficer', True)
        else:
            super(SalesOfficerLedger, self).delete()

# UI


class Purchase(models.Model):
    sales_officer = models.ForeignKey(SalesOfficer, on_delete=models.CASCADE)
    vender = models.ForeignKey(Vender, on_delete=models.CASCADE)
    total_amount = models.FloatField()
    transaction_type = models.CharField(
        max_length=5, choices=(('Bank', 'Bank'), ('Cash', 'Cash')))
    description = models.TextField(blank=True, default='Not Set')
    status = models.CharField(max_length=20, choices=(
        ('Pending', 'Pending'), ('Arrived', 'Arrived')))
    qty_remaining = models.IntegerField(blank=True, default=0)

    vl = models.ForeignKey(VenderLedger, on_delete=models.CASCADE)
    cl = models.ForeignKey(CashLedger, on_delete=models.CASCADE)
    bl = models.ForeignKey(BankLedger, on_delete=models.CASCADE)


class PurchaseProducts(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField()
    rate = models.IntegerField()
    purchas = models.ForeignKey(Purchase, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.product.particular
