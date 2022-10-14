# from django.urls import path, include
from django.urls import path,include
from rest_framework import routers
from .views import AccountViewset, CardViewset, CustomerViewSet, LoanViewset, NotificationViewset, ReceiptViewSet, RewardViewset, ThirdpartyViewset, TransactionViewset, WalletViewset

router = routers.DefaultRouter()
router.register(r"customers",CustomerViewSet)
router.register (r"wallets", WalletViewset)
router.register (r"accounts", AccountViewset)
router.register (r"cards", CardViewset)
router.register (r"loans", LoanViewset)
router.register (r"notifications", NotificationViewset)
router.register (r"receipts", ReceiptViewSet)
router.register (r"rewards", RewardViewset)
router.register (r"thirdparties", ThirdpartyViewset)
router.register (r"transactions", TransactionViewset)

urlpatterns=[
    path("",include(router.urls)),
]

