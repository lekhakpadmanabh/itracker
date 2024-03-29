from django.core.serializers import json 
from django.utils import simplejson 
from tastypie.serializers import Serializer
from tastypie.resources import ModelResource
from .models import Issue

class PrettyJSONSerializer(Serializer): 
    json_indent = 4 

    def to_json(self, data, options=None): 
        options = options or {} 
        data = self.to_simple(data, options) 
        return simplejson.dumps(data, cls=json.DjangoJSONEncoder, sort_keys=True, ensure_ascii=False, indent=self.json_indent) 


class IssueResource(ModelResource):
    class Meta:
        queryset = Issue.objects.all()
        resource_name = 'issues'
        serializer = PrettyJSONSerializer()
