from rest_framework import status, viewsets
from rest_framework.response import Response

from core.models import UserPlan

from .pagination import UserPagination
from .serializers import AllUserSerializers, NewUsersSerializer


class NewUserViewSet(viewsets.ModelViewSet):
    queryset = UserPlan.objects.all().order_by("-start_date")
    serializer_class = NewUsersSerializer
    pagination_class = UserPagination


class AllUserViewSet(viewsets.ModelViewSet):
    queryset = UserPlan.objects.filter(is_active=True)
    serializer_class = AllUserSerializers

    def list(self, request, *args, **kwargs):
        # Get the count of active plans
        active_plan_count = self.queryset.count()

        # Create an appropriate response object
        response = {
            "count": active_plan_count,
        }

        return Response(response, status=status.HTTP_200_OK)
