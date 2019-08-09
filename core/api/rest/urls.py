from django.urls import path

from . import views

urlpatterns = [
    path('currencies', views.CurrenciesListView.as_view()),
    path('rate/<int:pk>', views.RateRetrieveView.as_view()),
]