from POS_APP import models as m
from django.db.models import Q

def GetLegder(type,id,description,total_amount,transaction_type):
    if type == 'Party':
        pty = m.Party.objects.get(id=id)
        return m.PartyLedger(party=pty,description=description,transaction_type=transaction_type,total_amount=total_amount)
    if type == 'Vender':
        vn = m.Vender.objects.get(id=id)
        return m.Vender(vender=vn,description=description,transaction_type=transaction_type,total_amount=total_amount)
    elif type == 'SalesOfficer':
        sl = m.SalesOfficer.objects.get(id=id)
        return m.SalesOfficerLedger(sales_officer=sl,description=description,transaction_type=transaction_type,total_amount=total_amount)
    elif type == 'Bank':
        bk = m.Bank.objects.get(id=id)
        return m.BankLedger(bank=bk,description=description,transaction_type=transaction_type,total_amount=total_amount)
    elif type == 'Cash':
        c = m.CashPerson.objects.first(description=description,transaction_type=transaction_type,total_amount=total_amount)
        return m.CashLedger(cash_person=c,)


def updateCurrentBalance(type,last):

    if type == 'Party':
        last.party.current_Balance = last.net_balance
        last.party.save()
    if type == 'Vender':
        last.vender.current_Balance = last.net_balance
        last.vender.save()
    elif type == 'SalesOfficer':
        last.sales_officer.current_Balance = last.net_balance
        last.sales_officer.save()
    elif type == 'Bank':
        last.bank.current_Balance = last.net_balance
        last.bank.save()
    elif type == 'Cash':
        last.cash_person.current_Balance = last.net_balance
        last.cash_person.save()

   
def updateCurrentBalanceToOpeniing(type,last):
    if type == 'Party':
        last.party.current_Balance = last.party.opening_Balance
        last.party.save()
    elif type == 'Vender':
        last.vender.current_Balance = last.vender.opening_Balance
        last.vender.save()
    elif type == 'SalesOfficer':
        last.sales_officer.current_Balance = last.sales_officer.opening_Balance
        last.party.save()
    elif type == 'Bank':
        last.bank.current_Balance = last.bank.opening_Balance
        last.bank.save()
    elif type == 'Cash':
        last.cash_person.current_Balance = last.cash_person.opening_Balance
        last.cash_person.save()



def GetReliventLeadger(type,l,obj):
    if type == 'Party':
        l =l.filter(party=obj.party)
    elif type == 'SalesOfficer':
        l =l.filter(sales_officer=obj.sales_officer)
    elif type == 'Vender':
        l =l.filter(vender=obj.vender)
    elif type == 'Bank':
        l =l.filter(bank=obj.bank)
    elif type == 'Cash':
        l =l.filter(cash_person=obj.cash_person)
    return l


def UpdateLeadgers(obj, leadger, type, isReverse=False):
    l = leadger.objects.all()

    l = GetReliventLeadger(type,l,obj)
    
    l = l.filter(id__gte=obj.id).order_by('id')
    
    try:
        obj.total_amount = obj.total_amount[0]
        diff = obj.total_amount - l.first().total_amount
    except TypeError:
        diff = obj.total_amount - l.first().total_amount
    
    last = obj

    for i in l:
        if obj.transaction_type == 'Credit':
            if isReverse:
                i.net_balance -= diff
            else:
                i.net_balance += diff

        else:
            if isReverse:
                i.net_balance += diff
            else:
                i.net_balance -= diff

        i.save(updating=True)
        if i == l.last():
            last = i
    
    updateCurrentBalance(type,last)

    return l.first()


def DeleteLeadgers(obj, leadger, type, isReverse=False):
    l = leadger.objects.all()
    
    l = GetReliventLeadger(type,l,obj)
    relvent_lg = l
    l = l.filter(id__gte=obj.id).order_by('id')

    last = obj
    
    # First
    if relvent_lg.count() == 1:
        updateCurrentBalanceToOpeniing(type,last) 
    # last
    elif obj == relvent_lg.last():
        lg = leadger.objects.get(id=obj.id)
        last = relvent_lg.filter(Q(id__lte=lg.id) and ~Q(id=lg.id)).last()
        updateCurrentBalance(type,last)
        print(last.id,last.total_amount)
    # Middle
    else:
        for i in l[1:]:
            if obj.transaction_type == 'Credit':
                if isReverse:
                    i.net_balance += obj.total_amount
                else:
                    i.net_balance -= obj.total_amount
                i.save(updating=True)
            else:
                if isReverse:
                    i.net_balance -= obj.total_amount
                else:
                    i.net_balance += obj.total_amount
                i.save(updating=True)

            if i == l.last():
                last = i
        updateCurrentBalance(type,last)
    
    
    obj.delete(updating=True)



