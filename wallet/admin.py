from atexit import register
from django.contrib import admin
from .models import Customer,Wallet,Account,Receipt,Card,ThirdParty,Loan,Reward,Transaction,Notification

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "address","email","age")
    search_fields = ("first_name", "last_name","address","email","age")
admin.site.register(Customer, CustomerAdmin)

class WalletAdmin(admin.ModelAdmin):
    list_display = ("customer","currency","pin","date_created","isActive","balance")
    search_fields = ("customer","currency","pin","date_created","isActive","balance")
admin.site.register(Wallet,WalletAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display =("account_name","wallet","account_type","balance","account_number")
    search_fields = ("account_type","balance","balance","wallet")
admin.site.register(Account, AccountAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ("transaction_code","transaction_type","transaction_charge","transaction_number","wallet","amount")
    search_fields = ("transaction_code","transaction_type","transaction_number","wallet","amount")
admin.site.register(Transaction, TransactionAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display = ("card_name","card_number","issuer","account","issuer") 
    search_fields = ("card_name","card_number","issuer","account","issuer")
admin.site.register(Card, CardAdmin)

class ThirdPartyAdmin(admin.ModelAdmin):
    list_display = ("third_party_name","transaction_cost","currency","account")
    search_fields = ("third_party_name","transaction_cost","currency","account")
admin.site.register(ThirdParty, ThirdPartyAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display = ("name","message","dateandTime","date_sent","status")
    search_fields = ("name","message","dateandTime","date_sent","status")
admin.site.register(Notification,NotificationAdmin)

class ReceiptAdmin(admin.ModelAdmin):
    list_display = ("transaction","receipt_type","amount","dateTime")
    search_fields = ("transaction","receipt_type","amount","dateTime")
admin.site.register(Receipt,ReceiptAdmin)

class LoanAdmin(admin.ModelAdmin):
    list_display = ("Loan_balance","purpose","LoanTerm","interest_rate")
    search_fields = ("Loan_balance","purpose","LoanTerm","interest_rate")
admin.site.register(Loan,LoanAdmin)

class RewardAdmin(admin.ModelAdmin):
    list_display = ("name","points","customer_id")
    search_fields = ("name","points","customer_id")
admin.site.register(Reward, RewardAdmin)

