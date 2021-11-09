# import serializer from rest_framework
from rest_framework import serializers


# create a serializer


class CommentSerializer(serializers.Serializer):
	# initialize fields
	email = serializers.EmailField()
	content = serializers.CharField(null=False, max_length=200)
	created = serializers.DateTimeField()
