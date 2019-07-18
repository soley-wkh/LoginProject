from django.shortcuts import render, HttpResponse
from Article import models
from django.core.paginator import Paginator  # 分页


# Create your views here.
def index(request):
    return render(request, 'index.html')


def listpic(request):
    return render(request, 'listpic.html')


def about(request):
    return render(request, 'about.html')


def newslistpic(request):
    return render(request, 'newslistpic.html')


# def add_article(request):
#     for i in range(1, 100):
#         article = models.Article()
#         article.title = '斗破苍穹%s' % i
#         article.content = '%s 玄天宝录上记载的武功只有六种，分别是内功心法玄天功，练手之法玄玉手，练眼之法紫极魔瞳，擒拿之法控鹤擒龙，轻身之法鬼影迷踪，以及暗器使用之法，暗器百解。' % i
#         article.description = '%s 一岁多开始修炼玄天功，现在的唐三已经快要六岁了，他依旧在打基础。' % i
#
#         article.author = models.Author.objects.get(id=2)
#         article.save()
#         article.type.add(
#             models.Type.objects.get(id=2)
#         )
#         article.save()
#
#     return HttpResponse('添加成功')


def article_list(request, p=1):
    p = int(p)
    articles = models.Article.objects.order_by('-id')
    paginator = Paginator(articles, 10)
    per_page_articles = paginator.page(p)  # 获取具体页的数据
    # 获取页码
    start = p - 3
    end = p + 2
    if start <= 0:
        start = 0

    page_range = paginator.page_range[start:end]

    return render(request, 'article_list.html', locals())


def article_detail(request, id):
    id = int(id)
    article = models.Article.objects.get(id=id)
    return render(request, 'article_detail.html', {'article': article})
