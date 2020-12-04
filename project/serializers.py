from project.models import Pizza
from rest_framework import serializers


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields =('id','Type_of_pizza','Size_of_pizza','Topping_of_pizza')
