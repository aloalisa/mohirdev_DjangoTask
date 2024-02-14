from django.urls import path
from .views import news_list, news_detail, ContactPageView, homePageView, LocalNewsView,\
    ForeignNewsView, SportNewsView, TechnologyNewsView
# from.views import HomePageView

urlpatterns = [
    path('', homePageView, name='home_page'),
    path('all/', news_list, name='all_news_list'),
    path('news/<slug:news>/', news_detail, name='news_detail_page'),
    path('contact-us/', ContactPageView.as_view(), name='contact_page'),
    # path('', HomePageView.as_view(), name='home_page')
    path('local/', LocalNewsView.as_view(), name='local_news_page'),
    path('sport/', SportNewsView.as_view(), name='sport_news_page'),
    path('technology/' , TechnologyNewsView.as_view(), name='technology_news_page'),
    path('foreign/', ForeignNewsView.as_view(), name='foreign_news_page')
]

# path('contact-us/', ContactPageView.as_view(), name='contact_page') bu qismni klass uchun yozdim, as_view(), funksiya yordamida yaratilganda contactpageview uzi boladi

