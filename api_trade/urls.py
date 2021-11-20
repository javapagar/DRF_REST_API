from django.urls import path 
from api_trade.views import TradesApiView, TradesFilterListApiView

urlpatterns = [
    path('trades/',TradesFilterListApiView.as_view()),
    path('trades/<id>',TradesApiView.as_view()),

]