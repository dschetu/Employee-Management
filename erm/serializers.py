from rest_framework import serializers
from erm.models import Users


class UsersSerializer(serializers.ModelSerializer):
    employee_id = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    age = serializers.CharField(required=False)

    class Meta:
        model = Users
        fields ='__all__'