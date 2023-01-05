from django.urls import path

from .views import dump,CreateTransaction,GetAllTransation,GetTransation_by_Category,GetTransation_by_Date

urlpatterns = [
    path("d1/", dump),
    path("createtransaction/", CreateTransaction),
    path("gettransactions/",GetAllTransation),
    path("serachbycat",GetTransation_by_Category),
    path("serachbydate",GetTransation_by_Date)
]