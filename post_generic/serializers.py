from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'image', 'body', 'created_date']

    def validate(self, attrs):
        title = attrs.get("title", None)
        body = attrs.get("body", None)
        if title and title.islower():
            raise ValidationError({"title": 'First letter must be upper'})
        if body and len(body) < 10:
            raise ValidationError({"body": 'Body never some than 10 letters'})
        return attrs

