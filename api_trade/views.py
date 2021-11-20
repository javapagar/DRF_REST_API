from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from api_trade.models import Trade
from api_trade.serializers import TradeSerializer

class TradesApiView(APIView):
    """
    This view manage GET request and return one Trade Object by id.
    This view manage POST and DELETE request.
    """
    def post(self,request):
        trade_serializer = TradeSerializer(data = request.data)
        try:
            if trade_serializer.is_valid():
                trade = trade_serializer.save()
                return Response(TradeSerializer(trade).data, status=status.HTTP_201_CREATED)
            else:
                return Response(trade_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response('Error ' + str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def get(self,request,id):
        
        trade = self._get_trade_by_id(id)
        if trade:
            trade_serializer = TradeSerializer(trade)
            return Response(trade_serializer.data)
        else:
            return Response("Id "+str(id)+ " does not exist", status=status.HTTP_404_NOT_FOUND)
    

    def delete(self, request, id):

        trade = self._get_trade_by_id(id)

        if trade:
            trade.delete()
            return Response(status=status.HTTP_204_NO_CONTENT) 
        else:
            return Response("Id "+str(id)+ " does not exist", status=status.HTTP_404_NOT_FOUND)
    

    def _get_trade_by_id(self,id):
        """
        Check if a id exist in database
        """
        try:
            trade = Trade.objects.get(id=id)
            return trade
        except:
            return None


class TradesFilterListApiView(generics.ListCreateAPIView):
    """
    This view manage GET request and return a list of Trade Objects.
    This view manage filters by user_id and type
    """
    model = Trade
    serializer_class = TradeSerializer

    def get_queryset(self):
        queryset = Trade.objects.all()
        user_id = self.request.query_params.get('user_id')
        type_trade = self.request.query_params.get('type')
        print(user_id)
        if user_id:
            queryset = queryset.filter(user_id = user_id)
        print(type_trade)
        if type_trade:
            queryset = queryset.filter(type = type_trade)
        
        return queryset
