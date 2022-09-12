from django.shortcuts import render
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


def register_receipt(request):
    if request.method == "POST":
     form = ReceiptRegistrationForm()
     if form.is_Valid():
        form.save()
    else:
        form = ReceiptRegistrationForm()
    return render(request,"receipt.html",{"form": form})
def list_receipts(request):
    receipts = Receipt.objects.all()
    return render(request, "receipts_list.html", {"receipts": receipts})


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













