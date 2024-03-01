from django.shortcuts import render
from django.db import connection
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Blog
from .serializers import *
from .document import *
from faker import Faker
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    CompoundSearchFilterBackend
)

# Create your views here.


class FakeDataAPIView(APIView):
    def post(self, request):
        # fake = Faker()
        # num_blogs = int(request.data.get('num_blogs', 100000))  # default number of blogs to create is 10

        # for _ in range(num_blogs):
        #     title = fake.sentence(nb_words=4, variable_nb_words=True)
        #     content = fake.paragraph(nb_sentences=5, variable_nb_sentences=True, ext_word_list=None)

        #     Blog.objects.create(title=title, content=content)

        # return Response({'message': f'{num_blogs} fake blogs created successfully'})


        ############  duplicate database  #################


        # # Retrieve all instances of the Blog model
        # blogs = Blog.objects.all()

        # # Create a list to hold duplicated blog instances
        # duplicated_blogs = []

        # # Iterate over each blog instance and create a new instance for each one
        # for blog in blogs:
        #     # Create a new instance with the same attributes as the current blog
        #     duplicated_blog = Blog(title=blog.title, content=blog.content)
        #     duplicated_blogs.append(duplicated_blog)

        # # Bulk create the duplicated blog instances
        # Blog.objects.bulk_create(duplicated_blogs)
        # return Response({'message': f' fake blogs created successfully'})


        ##  DELETE Retrieve half of the data 
        # Calculate the total number of blogs
        total_blogs = Blog.objects.count()
        half_count = total_blogs // 2  # Calculate half of the total count
        
        # Get the IDs of all blogs
        all_blog_ids = Blog.objects.values_list('id', flat=True)
        
        # Delete in batches of 1000 to avoid memory issues
        batch_size = 1000
        for i in range(0, half_count, batch_size):
            print(i)
            batch_ids = all_blog_ids[i:i+batch_size]
            Blog.objects.filter(id__in=batch_ids).delete()


        return Response({"message": f" blogs deleted."})
        


class BlogSearchAPIView(APIView):
    def get(self, request):
        query = request.query_params.get('query', '')
        # Perform case-insensitive search on both title and content fields
        blogs = Blog.objects.filter(title__icontains=query)[:10] | Blog.objects.filter(content__icontains=query)[:10]
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)
    



class BlogElasticSearch(DocumentViewSet):
    document = BlogsDocument
    serializer_class = BlogDocumentSerializer
    filter_backends = [
        FilteringFilterBackend,
        CompoundSearchFilterBackend
    ]
    search_fields = (
        'title',
        'content'
    )
    multi_match_search_field = ('title', 'content')
    filter_fields = {
        'title': 'title',
        'content': 'content'
    }







