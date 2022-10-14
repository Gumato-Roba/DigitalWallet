from django.urls import path
from .views import card_profile, customer_profile, edit_account, edit_card, edit_notification, edit_profile, edit_thirdparty, edit_transaction, notification_profile, thirdparty_profile, transaction_profile, wallet_profile, account_profile,edit_wallet, list_accounts, list_cards, list_customers, list_loans, list_notifications, list_receipts, list_rewards, list_thirdpartys, list_transactions, list_wallets, register_account, register_card, register_customer, register_loan, register_notification, register_receipt, register_reward, register_thirdparty, register_transaction, register_wallet

urlpatterns = [

#registering 
    path("register/", register_customer, name="registration"),
    path("wallet/", register_wallet, name="wallet"),
    path("account/", register_account, name="account"),
    path("transaction/", register_transaction, name="transaction"),
    path("card/", register_card, name="card"),
    path("thirdparty/", register_thirdparty, name="thirdparty"),
    path("notification/", register_notification, name="notification"),
    path("receipt/", register_receipt, name="receipt"),
    path("loan/", register_loan, name="loan"),
    path("reward/", register_reward, name="reward"),

#creating lists
    path("customers/", list_customers, name="customers_list"),
    path("wallets/", list_wallets, name="wallets_list"),
    path("accounts/", list_accounts, name="accounts_list"),
    path("transactions/", list_transactions, name="transactions_list"),
    path("cards/", list_cards, name="cards_list"),
    path("thirdpartys/", list_thirdpartys, name="thirdpartys_list"),
    path("notifications/", list_notifications, name="notifications_list"),
    path("receipts/", list_receipts, name="receipts_list"),
    path("loans/", list_loans, name="loans_list"),
    path("rewards/", list_rewards, name="rewards_list"),

#editing data
    path("customerss/<int:id>/", customer_profile, name="customer_profile"),
    path("wallets/<int:id>/", wallet_profile, name="wallet_profile"),
    path("accounts/<int:id>/", account_profile, name="account_profile"),
    path("transactions/<int:id>/", transaction_profile, name="transaction_profile"),
    path("cards/<int:id>/", card_profile, name="card_profile"),
    path("thirdparty/<int:id>/", thirdparty_profile, name="thirdparty_profile"),
    path("notification/<int:id>/", notification_profile, name="notification_profile"),



    path("customers/edit/<int:id>/", edit_profile, name="edit_profile"),
    path("wallet/edit/<int:id>/", edit_wallet, name="edit_wallet"),
    path("account/edit/<int:id>/", edit_account, name="edit_account"),
    path("transaction/edit/<int:id>/", edit_transaction, name="edit_transaction"),
    path("card/edit/<int:id>/", edit_card, name="edit_card"),
    path("thirdparty/edit/<int:id>/", edit_thirdparty, name="edit_thirdparty"),
    path("notification/edit/<int:id>/", edit_notification, name="edit_notification"),









]
