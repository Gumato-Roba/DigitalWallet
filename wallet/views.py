from django.shortcuts import redirect, render
from .forms import AccountRegistrationForm, CardRegistrationForm, CustomerRegistrationForm, LoanRegistrationForm, NotificationRegistrationForm, ReceiptRegistrationForm, RewardRegistrationForm, ThirdPartyRegistrationForm, TransactionRegistrationForm, WalletRegistrationForm
from .models import Account, Card, Customer, Loan, Notification, Receipt, Reward, ThirdParty, Transaction, Wallet

# Create your views here.
def register_customer(request):
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html",{"form": form})
def list_customers(request):
    customers = Customer.objects.all()
    return render(request, "wallet/customers_list.html", {"customers": customers})

def customer_profile(request, id):
    customer = Customer.objects.get(id=id)
    return render(request, "customer_profile.html", {"customer": customer})

def edit_profile(request,id):
    customer = Customer.objects.get(id=id)
    if request.method=="POST":
        form = CustomerRegistrationForm(request.POST,instance= customer)
        if form.is_valid():
            form.save()
            return redirect("customer_profile", id=customer.id)
    else:
        form = CustomerRegistrationForm(instance=customer)
        return render(request, "edit_profile.html", {"form": form})



def register_wallet(request):
    if request.method == "POST":
      form = WalletRegistrationForm(request.POST)
      if form.is_valid():
            form.save()
    else:
        form = WalletRegistrationForm()
    return render(request,"wallet.html",{"form": form})
def list_wallets(request):
    wallets = Wallet.objects.all()
    return render(request, "wallets_list.html", {"wallets": wallets})

def wallet_profile(request, id):
    wallet = Wallet.objects.get(id=id)
    return render(request, "wallet_profile.html", {"wallet": wallet})

def edit_wallet(request,id):
    wallet = Wallet.objects.get(id=id)
    if request.method=="POST":
        form = WalletRegistrationForm(request.POST,instance= wallet)
        if form.is_valid():
            form.save()
            return redirect("edit_wallet", id=wallet.id)
    else:
        form = WalletRegistrationForm(instance=wallet)
        return render(request, "edit_wallet.html", {"form": form})



def register_account(request):
    if request.method == "POST":
     form = AccountRegistrationForm(request.POST)
     if form.is_valid():
        form.save()
    else:
        form = AccountRegistrationForm()
    return render(request,"accounts.html",{"form": form})
def list_accounts(request):
    accounts = Account.objects.all()
    return render(request, "accounts_list.html", {"accounts": accounts})

def account_profile(request, id):
    account = Account.objects.get(id=id)
    return render(request, "account_profile.html", {"account": account})

def edit_account(request,id):
    account = Account.objects.get(id=id)
    if request.method=="POST":
        form = AccountRegistrationForm(request.POST,instance= account)
        if form.is_valid():
            form.save()
            return redirect("account_profile", id=account.id)
    else:
        form = AccountRegistrationForm(instance=account)
        return render(request, "edit_account.html", {"form": form})




def register_transaction(request):
    if request.method == "POST":
     form = TransactionRegistrationForm(request.POST)
     if form.is_valid():
        form.save()
    else:
        form =TransactionRegistrationForm()
    return render(request,"transaction.html",{"form": form})
def list_transactions(request):
    transactions = Transaction.objects.all()
    return render(request, "transactions_list.html", {"transactions": transactions})

def transaction_profile(request, id):
    transaction= Transaction.objects.get(id=id)
    return render(request, "transaction_profile.html", {"transaction": transaction})

def edit_transaction(request,id):
    transaction = Transaction.objects.get(id=id)
    if request.method=="POST":
        form = TransactionRegistrationForm(request.POST,instance= transaction)
        if form.is_valid():
            form.save()
            return redirect("transaction_profile", id=transaction.id)
    else:
        form = TransactionRegistrationForm(instance=transaction)
        return render(request, "edit_transacttion.html", {"form": form})


def register_card(request):
    if request.method == "POST":
     form = CardRegistrationForm(request.POST)
     if form.is_Valid():
        form.save()
    else:
        form = TransactionRegistrationForm()
    return render(request,"card.html",{"form": form})
def list_cards(request):
    cards = Card.objects.all()
    return render(request, "cards_list.html", {"cards": cards})

def card_profile(request, id):
    card = Card.objects.get(id=id)
    return render(request, "card_profile.html", {"card": card})

def edit_card(request,id):
    card = Card.objects.get(id=id)
    if request.method=="POST":
        form = CardRegistrationForm(request.POST,instance= card)
        if form.is_valid():
            form.save()
            return redirect("card_profile", id=card.id)
    else:
        form = CardRegistrationForm(instance=card)
        return render(request, "edit_card.html", {"form": form})


def register_thirdparty(request):
    if request.method == "POST":
     form = ThirdPartyRegistrationForm()
     if form.is_valid():
        form.save()
    else:
        form = ThirdPartyRegistrationForm()
    return render(request,"thirdparty.html",{"form": form})
def list_thirdpartys(request):
    thirdpartys = ThirdParty.objects.all()
    return render(request, "thirdpartys_list.html", {"thirdpartys":thirdpartys})

def thirdparty_profile(request, id):
    thirdparty = ThirdParty.objects.get(id=id)
    return render(request, "thirdparty_profile.html", {"thirdparty": thirdparty})

def edit_thirdparty(request,id):
    thirdparty = ThirdParty.objects.get(id=id)
    if request.method=="POST":
        form = ThirdPartyRegistrationForm(request.POST,instance= thirdparty)
        if form.is_valid():
            form.save()
            return redirect("thirdparty_profile", id=thirdparty.id)
    else:
        form = ThirdPartyRegistrationForm(instance=thirdparty)
        return render(request, "edit_thirdparty.html", {"form": form})


def register_notification(request):
    if request.method == "POST":
     form = NotificationRegistrationForm()
     if form.is_valid():
        form.save()
    else:
        form = NotificationRegistrationForm()
    return render(request,"notification.html",{"form": form})
def list_notifications(request):
    notifications = Notification.objects.all()
    return render(request, "notifications_list.html", {"notifications": notifications})

def notification_profile(request, id):
    notification = Notification.objects.get(id=id)
    return render(request, "notification_profile.html", {"notification": notification})

def edit_notification(request,id):
    notification = Notification.objects.get(id=id)
    if request.method=="POST":
        form = Notification(request.POST,instance= notification)
        if form.is_valid():
            form.save()
            return redirect("notification_profile", id=notification.id)
    else:
        form = NotificationRegistrationForm(instance=notification)
        return render(request, "edit_thirdparty.html", {"form": form})


def register_receipt(request):
    if request.method == "POST":
     form = ReceiptRegistrationForm()
     if form.is_valid():
        form.save()
    else:
        form = ReceiptRegistrationForm()
    return render(request,"receipt.html",{"form": form})
def list_receipts(request):
    receipts = Receipt.objects.all()
    return render(request, "receipts_list.html", {"receipts": receipts})


def receipt_profile(request, id):
    receipt = Receipt.objects.get(id=id)
    return render(request, "receipt_profile.html", {"receipt": receipt})

def edit_receipt(request,id):
    receipt = Receipt.objects.get(id=id)
    if request.method=="POST":
        form = Receipt(request.POST,instance= receipt)
        if form.is_valid():
            form.save()
            return redirect("receipt_profile", id=receipt.id)
    else:
        form = ReceiptRegistrationForm(instance=receipt)
        return render(request, "edit_receipt.html", {"form": form})


def register_loan(request):
    if request.method == "POST":
     form = LoanRegistrationForm()
    if form.is_valid():
        form.save()
    else:
      form = LoanRegistrationForm()
    return render(request,"loan.html",{"form": form})
def list_loans(request):
    loans = Loan.objects.all()
    return render(request, "loans_list.html", {"loans": loans})


def loan_profile(request, id):
    loan = Loan.objects.get(id=id)
    return render(request, "loan_profile.html", {"loan": loan})

def edit_loan(request,id):
    loan = Loan.objects.get(id=id)
    if request.method=="POST":
        form = LoanRegistrationForm(request.POST,instance= loan)
        if form.is_valid():
            form.save()
            return redirect("loan_profile", id=loan.id)
    else:
        form = LoanRegistrationForm(instance=loan)
        return render(request, "edit_loan.html", {"form": form})

def register_reward(request):
    if request.method == "POST":
     form = RewardRegistrationForm()
    if form.is_valid():
        form.save()
    else:
        form = LoanRegistrationForm()
    return render(request,"reward.html",{"form": form})
def list_rewards(request):
    rewards = Reward.objects.all()
    return render(request, "rewards_list.html", {"rewards": rewards})


def rewards_profile(request, id):
    reward = Reward.objects.get(id=id)
    return render(request, "reward_profile.html", {"reward": reward})

def edit_reward(request,id):
    reward = Reward.objects.get(id=id)
    if request.method=="POST":
        form = RewardRegistrationForm(request.POST,instance= reward)
        if form.is_valid():
            form.save()
            return redirect("reward_profile", id=reward.id)
    else:
        form = RewardRegistrationForm(instance=reward)
        return render(request, "edit_reward.html", {"form": form})













