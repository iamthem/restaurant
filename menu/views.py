from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response 
from rest_framework.views import status
from json import dumps

from .models import MenuSections, Success
from .serializers import MenuSerializer, SuccessSerializer
from .decorator import validate_request_data

class CustomView(generics.CreateAPIView,
                 generics.RetrieveUpdateDestroyAPIView):
    pass

class ListMenuSections (generics.ListCreateAPIView):
    """
    GET /menusection
    POST /menusection 
    """

    queryset = MenuSections.objects.all()
    serializer_class = MenuSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = MenuSerializer(queryset, many=True)
        return Response(
                data = { "MenuSection" : serializer.data })

    @validate_request_data
    def post(self, request, *args, **kwargs): 
        menu_section = MenuSections.objects.create(
                name=request.data["name"]
                )
        success = SuccessSerializer(Success(True))
        return Response(
                data = { 
                        "success" : success.data["success"],
                        "MenuSection" : [MenuSerializer(menu_section).data]
                       },
                status=status.HTTP_201_CREATED
        )

class MenuDetailView (CustomView):
    """
    GET /menusection/:id/
    PUT /menusection/:id/
    POST /menusection/:id/
    DELETE /menusection/:id/
    """

    queryset = MenuSections.objects.all()
    serializer_class = MenuSerializer

    def get(self, request, *args, **kwargs):
        try:
            menu_section = self.queryset.get(pk=kwargs["pk"])
            return Response(data = { 
                            "MenuSection" : [MenuSerializer(menu_section).data]
                            })

        except MenuSections.DoesNotExist:
            return Response(
                data={
                    "message": "Menusection with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_request_data
    def post(self, request, *args, **kwargs): 
        try:
            menu_section = self.queryset.get(pk=kwargs["pk"])
            serializer = MenuSerializer()
            success = SuccessSerializer(Success(False))
            return Response(
                    data={
                        "success": success.data["success"],
                        "message": "Menusection with id: {} already exists".format(kwargs["pk"]) 
                        },
                    status=status.HTTP_409_CONFLICT
                    )

        except MenuSections.DoesNotExist:
            menu_section = MenuSections.objects.create(
                    id = kwargs["pk"],
                    name=request.data["name"]
                )
            success = SuccessSerializer(Success(True))
            return Response(
                    data = { 
                        "success" : success.data["success"],
                        "MenuSection" : [MenuSerializer(menu_section).data]
                       },
                    status=status.HTTP_201_CREATED
                )

    @validate_request_data
    def put(self, request, *args, **kwargs):
        try:
            menu_section = self.queryset.get(pk=kwargs["pk"])
            serializer = MenuSerializer()
            updated_menu = serializer.update(menu_section, request.data)
            success = SuccessSerializer(Success(True))
            return Response(data = { 
                            "success" : success.data["success"],
                            "MenuSection" : [MenuSerializer(menu_section).data]
                            })

        except MenuSections.DoesNotExist:
            success = SuccessSerializer(Success(False))
            return Response(
                data={
                    "success" : success.data["success"],
                    "message": "Menusection with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            menu_section = self.queryset.get(pk=kwargs["pk"])
            menu_section.delete()
            success = SuccessSerializer(Success(True))
            return Response(data = {"success" : success.data["success"]}) 

        except MenuSections.DoesNotExist:
            success = SuccessSerializer(Success(False))
            return Response(
                data={
                    "success" : success.data["success"], 
                    "message": "Menusection with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
