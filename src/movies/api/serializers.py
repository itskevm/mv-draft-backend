from rest_framework import serializers

from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'author', 'content', 'created_on')
