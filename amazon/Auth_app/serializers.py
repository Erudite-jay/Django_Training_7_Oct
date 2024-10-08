from rest_framework import serializers
from .models import Contact

#normal serializer
# class ContactSerializer(serializers.Serializer):
#     name= serializers.CharField(max_length=100)
#     email = serializers.EmailField()
#     phone_number = serializers.CharField(max_length=10)


#model serializers
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'