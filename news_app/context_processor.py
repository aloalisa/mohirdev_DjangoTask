from .models import News


def latest_news(request):
    latest_news = News.objects.all()

    context = {
        'latest_news': latest_news
    }

    return context


