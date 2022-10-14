from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from wallet.models import Account, Card, Customer, Loan, Notification, Receipt, Reward, ThirdParty, Transaction, Wallet

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("first_name","last_name","email","age")
        

class  WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model= Wallet
        fields=("isActive","balance","customer","pin","currency","date_created")


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model= Account
        fields=("account_number","account_name","account_type","balance","wallet")

class  CardSerializer(serializers.ModelSerializer):
    class Meta:
        model= Card
        fields=("card_number","card_name","date_issued","expiry_date","account","issuer")   

class  LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model= Loan
        fields=("amount","Wallet","payment_due_date","Loan_balance","interest_rate","purpose")      


class  NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model= Notification
        fields=("name","message")

class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model= Receipt
        fields=("amount","dateTime","receipt_type")


class  RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model= Reward
        fields=("name","points","customer_id")  



class  ThirdpartySerializer(serializers.ModelSerializer):
    class Meta:
        model= ThirdParty
        fields=("account","currency","transaction_cost","third_party_name") 

class  TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Transaction
        fields=("transaction_code","transaction_type","transaction_charge","transaction_number")        