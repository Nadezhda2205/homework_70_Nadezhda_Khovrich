from rest_framework.response import Response
from rest_framework.views import APIView

from issue.models import Project
from api.serializers import ProjectSerializer


class ProjectAPIView(APIView):

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method GET not allowed'})

        try:
            project = Project.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = ProjectSerializer(instance=project)
        return Response({'project': serializer.data})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            return Response({'error': 'Method POST not allowed'})
        serializer = ProjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'project': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            return Response({'error': 'Method PUT not allowed'})

        try:
            project = Project.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})
        serializer = ProjectSerializer(data=request.data, instance=project)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'project': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            return Response({'error': 'Method DELETE not allowed'})
            
        try:
            project = Project.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})
        
        try:
            project.delete()
        except:
            return Response({'error': 'Cannot delete'})

        return Response({'project': 'delete project ' + str(pk)})
