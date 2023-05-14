from rest_framework.serializers import ModelSerializer
from ..models import Publication


class PubSerializer(ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'