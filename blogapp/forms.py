from django import forms
from blogapp.models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('auther', 'title', 'text')


        wedgets = {
            'title':forms.TextInput(attrs = {'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('auther', 'text')

        wedget = {
            'auther':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.TextInput(attrs={'class':'editable medium-editor-text'})
        }