from rest_framework import serializers
from books.models import Item
from users.models import Users

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model= Item
        fields= '__all__'

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model= Users
        fields= ('userId','favourites')