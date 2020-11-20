from rest_framework.views import APIView
from rest_framework.response import Response

class TestView(APIView):
    """
    Test system
    """
    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        """
        Return a list of all users.
        """
        return Response({'status': True})