from django.conf.urls import url, include
from calc_app import views

urlpatterns = [
    url('getInterestRate', views.calculateAmount, name="calc_amount")
]
