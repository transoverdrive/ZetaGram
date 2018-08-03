from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers


class Feed(APIView):

    def get(self, request, format=None):

        user = request.user

        following_users = user.following.all()

        image_list = []

        for following_user in following_users:
            
            user.images = following_user.images.all()[:2]

            for image in user_images:
                
                image_list.append(image)
        
        sorted_list = sorted(image_list, key=get_key)

        print(sorted_list)
        
        return Response(status=200)

def get_key(image):
    return image.created_at