from rest_framework import serializers
from api_trade.models import Trade

class TradeSerializer(serializers.ModelSerializer):

    class Meta():
        model = Trade
        fields ='__all__'

    def validate_shares(self, value):
        """
        Validator for shares value.

        """
        if value < 1 or value > 100:
            raise serializers.ValidationError('Shares value has to be between 1 and 100.')
        return value