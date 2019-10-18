from rest_framework import serializers
from .models import LANGUAGE_CHOICES, STYLE_CHOICES, Snippet

class SnippetSerializer(serializers.ModelSerializer):
    """
    Serialize and deserialize snippet instances into representations such as json.
    """

    class Meta:
        """
        Specify the model and fields.
        """
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']