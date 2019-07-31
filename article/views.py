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
        title = request.POST.get('title', None) # 없으면 논을 준다
        content = request.POST.get('content', None)
        if title and content:
            ap = Article.objects.create(title=title, content=content)
        # 객체할당- 오브젝트는 만들었으나(쿼리셋) 디비에는 넣지 않겠다
            return redirect(reverse('article:detail', kwargs={'pk': ap.id}))
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