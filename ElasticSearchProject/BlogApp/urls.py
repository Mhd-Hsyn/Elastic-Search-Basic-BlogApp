# urls.py
from django.urls import path
from .views import FakeDataAPIView, BlogSearchAPIView, BlogElasticSearch

urlpatterns = [
    path('fake-data/', FakeDataAPIView.as_view(), name='fake_data'),
    path('search/', BlogSearchAPIView.as_view(), name='blog-search'),
    path('search-elastic/', BlogElasticSearch.as_view({'get':'list'})),

]
