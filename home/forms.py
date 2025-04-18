from django import forms
from .models import Article

class ValidateAddArticle(forms.Form):
    title = forms.CharField(label = "title", max_length=400)
    picture = forms.ImageField(label = "picture")
    content = forms.CharField(label = "content", min_length=4)
    author = forms.CharField(label = "author", min_length=4)
    slug = forms.CharField(label = "slug", min_length=4)


class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)

class Search(forms.Form):
    search = forms.CharField(label="Requête", min_length=1)


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'author', 'image']
        widgets = {
            'author': forms.Select(attrs={'class': 'form-control'}),
        }