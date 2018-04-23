import datetime
from haystack import indexes
from .models import Version


class VersionIndex(indexes.SearchIndex, indexes.Indexable):
    version = indexes.CharField(document=True)
    summary = indexes.CharField(model_attr='summary')
    # created = indexes.DateTimeField(model_attr='created')

    def get_model(self):
        return Version

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()