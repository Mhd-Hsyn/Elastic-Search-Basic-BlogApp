from django_elasticsearch_dsl import Index, Document, fields
from elasticsearch_dsl import analyzer

from .models import Blog

# Define the Elasticsearch index
PUBLISHER_INDEX = Index('elastic_demo')

PUBLISHER_INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1
)

# Define the Elasticsearch document
@PUBLISHER_INDEX.doc_type
class BlogsDocument(Document):
    id = fields.IntegerField(attr='id')
    title = fields.TextField(
        fields={
            'raw': {
                'type': 'keyword'
            }
        }
    )
    content = fields.TextField(
        fields={
            'raw': {
                'type': 'keyword'
            }
        }
    )

    class Django:
        model = Blog

