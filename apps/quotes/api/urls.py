from django.conf.urls import url
from .views import AuthorList, AuthorDetail, QuoteList, QuoteDetail


urlpatterns = [
    # Generic CBV
    # from .views import AuthorListAPIView, QuoteListAPIView
    # url(r'^authors/$', AuthorListAPIView.as_view()),
    # url(r'^quotes/$', QuotesListAPIView.as_view()),

    # CBV
    # Authors
    url(r'^authors/(?P<pk>\d+)/$', AuthorDetail.as_view()),
    url(r'^authors/$', AuthorList.as_view()),

    # Quotes
    url(r'^quotes/(?P<pk>\d+)/$', QuoteDetail.as_view()),
    url(r'^quotes/$', QuoteList.as_view()),

]
