from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Post


class PostViewSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'image', 'body', 'created_date']

    def validate(self, attrs):
        title = attrs.get("title", None)
        if title and title.islower():
            raise ValidationError({"title": 'First letter must be upper'})
        return attrs

