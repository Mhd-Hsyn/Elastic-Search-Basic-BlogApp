from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .models import Blog
from .document import *
from rest_framework import serializers


class BlogDocumentSerializer(DocumentSerializer):
    class Meta:
        model = Blog
        document = BlogsDocument
        fields = ['title', 'content']


        def get_location(self, obj):
            try:
                return obj.location.to_dict()
            except:
                return {}
            
            
            


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'