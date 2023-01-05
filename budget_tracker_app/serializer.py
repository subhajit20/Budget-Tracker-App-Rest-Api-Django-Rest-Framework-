from rest_framework import serializers

class TransactionSerializer(serializers.Serializer):
    category = serializers.CharField()
    expensename = serializers.CharField()
    cost = serializers.CharField()

class CategorySerializer(serializers.Serializer):
    category = serializers.CharField()

class DateSerializer(serializers.Serializer):
    date = serializers.DateField()