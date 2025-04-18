from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Article

from .forms import ValidateAddArticle
from .forms import NameForm
from .forms import Search

def index(request):
    articles = Article.objects.all()
    data = {"articles" : articles, "message" : "Les articles"}
    return render(request, "home/index.html", data)

def single_article(request, slug):
    article = Article.objects.get(slug=slug)
    data = {'article' : article}
    return render(request, "home/article.html", data)

def add_article(request):
    return render(request, "home/add.html")



def validate_add_article(request):
   if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ValidateAddArticle(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            title = form.cleaned_data['title']
            picture = form.cleaned_data['picture']
            content = form.cleaned_data['content']
            author = form.cleaned_data['author']
            slug = form.cleaned_data['slug']

            # form.save()
            Article.objects.create(title=title, body=content, author=author, image=picture, slug=slug)

            return HttpResponseRedirect(f"/blog/article/{slug}")
        else:
            form = ValidateAddArticle()

        return render(request, "home/index.html", {"form": form})
   
def search(request):
    if request.method == "POST":
        form = Search(request.POST)

        if form.is_valid():
            req = form.cleaned_data['search']
            response = Article.objects.filter(body__contains=req)
            message = f"Voici les articles qui contient : {req}"
            data = {"searchs" : response, "message" : message}
        else:
            data = {"message" : "Aucun article trouvé"}
            
    return render(request, "home/index.html", data)
    
def contact(request):
    return render(request, "home/contact.html")

def apropos(request):
    return render(request, "home/a-propos.html")