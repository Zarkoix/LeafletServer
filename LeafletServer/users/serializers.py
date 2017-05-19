"""
This module contains the API serializers for the User app
"""

from LeafletServer.users.models import User
from LeafletServer.leaves.models import Leaf
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for users
    """
    leaves = serializers.PrimaryKeyRelatedField(many=True,
                                                queryset=Leaf.objects.all())

    class Meta:
        """
        Metadata Class for Django
        """
        model = User
        fields = ('id', 'created', 'username', 'email', 'password', 'plan')
