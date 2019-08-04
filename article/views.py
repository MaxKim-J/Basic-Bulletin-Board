from django.shortcuts import render, redirect, reverse, resolve_url
from django.urls import reverse_lazy
# 이 숏컷 함수는 인자로 url패턴명을 받으며, url패턴명을 인식하기 위해서는 urls.py 모듈이 메모리에 로딩되어야 하는데
# 지금 작성하고 있는  views.py 모듈이 로딩되고 처리되는 시점에 urls가 로딩되지 않을수도 있어서(?) reverse_lazy()
from django.views.generic.edit import CreateView
# 테이블 레코드를 생성하기 위해 필요한 폼을 보여주고, 폼의 입력을 받아서 테이블의 레코드를 생성해줌
from django.views.generic.base import TemplateView
from django.contrib.auth.forms import UserCreationForm
# 유저 모델의 인스턴스를 생성하기 위해 보여주는 폼. 장고에서 기본 제공하는 뷰
from article.models import Article, Tag


class HomeView(TemplateView):
    template_name = 'article/home.html'


class UserCreateView(CreateView):
    # accounts/register/url을 처리하는 뷰
    # 적절한 회원가입 폼을 보여주고 폼에 입력된 내용에서 에러 여부를 체크한 후 에러가 없으면 (유저)레코드 생성
    template_name = 'registration/register.html'    # 로그인 상황에서 쓰는 템플릿
    form_class = UserCreationForm   # 템플릿에서 사용할 폼 - 이건 장고의 기본 폼, 직접 폼 작성하고 써도 됨(좀잇다 해보자)
    success_url = reverse_lazy('register_done')     # 폼이 valid하고 테이블 레코드 생성이 완료되면 이동할 url을 지정


class UserCreationDoneTV(TemplateView):
    template_name = 'registration/register_done.html'   # /accounts/register/done/ URL을 처리해준다
    # 가입 처리가 완료된 후에 사용자에게 보여줄 템플릿의 파일명을 지정한다.


def profile(request):
    return render(request, 'registration/profile.html')


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
            # messages.success(request, '새 포스팅 만들었다')
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
            # messages.success(request, '포스트가 수정됐다')
            article.save()
            return redirect(resolve_url('article:detail', pk))

    else:
        return render(request, 'article/update_article.html', {'article': article})


def delete_article(request, pk):
    article = Article.objects.get(pk=pk)
    comments = article.comment_set.all()
    tags = article.tag_set.all()
    confirm = "진짜 삭제할거임? 삭제 한번 더 누르면 삭제 ㄱ"
    data = {'article': article, 'comments': comments, 'tags': tags, 'confirm': confirm}

    if article.delo == 1:
        article.delo = 2
        article.save()
        return render(request, 'article/detail_article.html', data)

    else:
        article.delete()
        return redirect('article:list')



