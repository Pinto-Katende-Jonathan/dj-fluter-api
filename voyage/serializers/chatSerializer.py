from rest_framework.serializers import ModelSerializer
from ..models import Discussion


class ChatSerializer(ModelSerializer):
    class Meta:
        model = Discussion
        fields = '__all__'