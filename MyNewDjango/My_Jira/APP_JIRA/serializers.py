from rest_framework import serializers
from .models import MyClass



class MyClassSerializer(serializers.ModelSerializer):

    class Meta:

        model = MyClass
        fields = '__all__'



