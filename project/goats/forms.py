from django.forms import ModelForm
from .models import Comment


class CommentCreateForm(ModelForm):
    """A form to create comments"""

    class Meta:
        model = Comment
        fields = ('comment',)