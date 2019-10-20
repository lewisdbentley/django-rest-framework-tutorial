from rest_framework import serializers
from .models import LANGUAGE_CHOICES, STYLE_CHOICES, Snippet
from django.contrib.auth.models import User


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serialize and deserialize snippet instances into representations such as json.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name="snippet-highlight", format="html")

    class Meta:
        """
        Specify the model and fields.
        """
        model = Snippet
        fields = ['url', 'id', 'title', 'code', 'linenos', 'language', 'style', 'owner', 'highlight']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name="detail-view", read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']