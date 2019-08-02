from django.shortcuts import render, redirect, reverse, resolve_url
from article.models import Article, Tag


def list_article(request):
    articles = Article.objects.all()
    data = {
        'articles': articles
    }
    return render(request, 'article/list_article.html', data)


def create_article(request):
    if request.method == 'POST':
        title = request.POST.get('title', None)
        content = request.POST.get('content', None)
        if title and content:
            ap = Article.objects.create(title=title, content=content)
            return redirect(reverse('article:detail', kwargs={'pk': ap.id}))
    else:
        return render(request, 'article/create_article.html')


def detail_article(request, pk):
    article = Article.objects.get(pk=pk)
    comments = article.comment_set.all()
    tags = article.tag_set.all()
    data = {'article': article, 'comments': comments, 'tags': tags}

    if request.method == "POST":
        author = request.POST.get('name', None)
        message = request.POST.get('contents', None)
        if author and message:
            article.comment_set.create(author=author, message=message)
        return redirect(resolve_url('article:detail', article.id))

    else:
        return render(request, 'article/detail_article.html', data)


def tags_article(request, pk):
    tags = Tag.objects.get(pk=pk)
    tag_article = Article.objects.filter(tag__name__exact=tags)
    context = {'tag_article': tag_article, 'tags': tags}
    return render(request, 'article/tag_article.html', context)


def update_article(request, pk):
    article = Article.objects.get(id=pk)

    if request.method == 'POST':
        title = request.POST.get('title', None)
        content = request.POST.get('content', None)
        if title and content:
            article.title = title
            article.content = content
            article.save()
            return redirect(resolve_url('article:detail', pk))

    else:
        return render(request, 'article/update_article.html', {'article': article})


def delete_article(request, pk):
    article = Article.objects.get(pk=pk)
    comments = article.comment_set.all()
    tags = article.tag_set.all()
    confirm = "진짜 삭제할거임? 삭제 한번 더 누르면 삭제해주지"
    data = {'article': article, 'comments': comments, 'tags': tags, 'confirm': confirm}

    if article.delo == 1:
        article.delo = 2
        article.save()
        return render(request, 'article/detail_article.html', data)

    elif article.delo == 2:
        article.delete()
        return redirect('article:list')