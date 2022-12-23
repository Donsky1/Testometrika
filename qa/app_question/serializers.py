from  rest_framework import serializers

from .models import NameTest, GroupTest


class NameTestSerializer(serializers.ModelSerializer):

    class Meta:
        model = NameTest
        fields = '__all__'


class GroupTestSerializer(serializers.ModelSerializer):

    class Meta:
        model = GroupTest
        fields = '__all__'