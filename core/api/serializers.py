from rest_framework import serializers

from core.models import UserPlan


class NewUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPlan
        fields = ["user", "start_date"]


class AllUserSerializers(serializers.ModelSerializer):
    count = serializers.IntegerField()

    class Meta:
        model = UserPlan
        fields = ["count"]
