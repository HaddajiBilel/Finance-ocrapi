from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer
from rest_framework.permissions import IsAuthenticated
from .models import File
import json
from .tableExtractor import tabExtract
from django.http import HttpResponse
# Create your views here.


class TableView(APIView):
    def get(self, request, fileID):

        fileMeta = File.objects.get(id=fileID)
        tabExtract(str(fileMeta.file))
        fileMeta.tabPath = 'output/'+str(fileMeta.file)
        fileMeta.save()
        return Response({'data': str(fileMeta.tabPath)}, status=status.HTTP_201_CREATED)


class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            # save the new file
            file_serializer.save()
            # save the extracted tables
            try:
                fileMeta = File.objects.get(id=file_serializer.data['id'])
                tabExtract(str(fileMeta.file))
                fileMeta.tabPath = 'media/output/' + \
                    str(fileMeta.file)[:-4]+'.xlsx'
                fileMeta.save()
            except:
                return HttpResponse({'error : bad file structure/type'}, status=status.HTTP_400_BAD_REQUEST)
            with open(fileMeta.tabPath, 'rb')as fh:
                response = HttpResponse(
                    fh.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
                response['Content-Disposition'] = "attachment; filename=" + \
                    fileMeta.tabPath
                return response
            # return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):

        fileNames = File.objects.all()
        serializer = FileSerializer(fileNames, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
