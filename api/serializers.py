from api.models import Post
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ["post_title", "body", "date", "upvotes", "downvotes", "results", "boast_or_roast"]
