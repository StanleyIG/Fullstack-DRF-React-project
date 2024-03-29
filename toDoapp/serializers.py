from rest_framework.serializers import ModelSerializer, CharField, URLField
from toDoapp.models import Project, ToDo


class ProjectModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ToDoModelSerializer(ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'

        
