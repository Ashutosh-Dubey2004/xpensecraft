from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("transactions/", views.transaction_list, name="transaction_list"),
    path("transactions/add/", views.transaction_add, name="transaction_add"),
]
