from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = Product
        fields = ['id', 'title', 'description','price','summary','verified','created_at']
      



class UserSerializer(serializers.ModelSerializer):
    # products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
    products = ProductSerializer(many=True)
    class Meta:
        model = User
        fields = ['username', 'products']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        # If the request method is POST, remove the 'username' field from the response
        if self.context['request'].method == 'POST':
            data.pop('username', None)

        return data

    def create(self, validated_data):
        hostels_data = validated_data.pop('products', [])
        user_instance = User.objects.create_user(**validated_data)

        for hostel_data in hostels_data:
            Product.objects.create(owner=user_instance, **hostel_data)

        return user_instance

# class UserSerializer(serializers.ModelSerializer):
#     products = ProductSerializer(many=True, read_only=True)

#     class Meta:
#         model = User
#         fields = ['username', 'products']

#     def to_representation(self, instance):
#         data = super().to_representation(instance)

#         # If the request method is POST, remove the 'username' field from the response
#         if self.context['request'].method == 'POST':
#             data.pop('username', None)

#         return data

#     def create(self, validated_data):
#         hostels_data = validated_data.pop('products', [])
#         user_instance = User.objects.create_user(**validated_data)

#         for hostel_data in hostels_data:
#             Product.objects.create(owner=user_instance, **hostel_data)

#         return user_instance


