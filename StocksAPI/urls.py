# -*- coding: utf-8 -*-
from django.urls import path, include

from StocksAPI.views import index

from api_trade.views import TradesApiView

urlpatterns = [
    path('',include('api_trade.urls')),

]
