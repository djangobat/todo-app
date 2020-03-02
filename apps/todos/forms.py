from django import forms

from .models import Topic, Task


class CreateTopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ('title', 'description',)


