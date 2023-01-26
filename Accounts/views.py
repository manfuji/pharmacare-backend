# from django.shortcuts import render
# from rest_framework import viewsets, mixins, permissions, generics, views
# from django.contrib.auth.models import User
# # from AllModels.models import Profile
# from .serializers import UserSerializer, ProfileSerializers, ChangePasswordSerializer
# # ,ProfileSerializer

# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
# from Allmodels.models import Profile
# from knox.auth import TokenAuthentication
# from rest_framework import status


# class ChangePasswordView(generics.UpdateAPIView):
#     """
#     An endpoint for changing password.
#     """
#     serializer_class = ChangePasswordSerializer
#     model = User
#     authentication_classes = [TokenAuthentication, ]

#     # permission_classes = (IsAuthenticated,)

#     def get_object(self, queryset=None):
#         obj = self.request.user
#         return obj

#     def update(self, request, *args, **kwargs):
#         print(request.data)
#         self.object = self.get_object()
#         serializer = self.get_serializer(data=request.data)

#         if serializer.is_valid():
#             # Check old password
#             if not self.object.check_password(serializer.data.get("old_password")):
#                 return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
#             # set_password also hashes the password that the user will get
#             self.object.set_password(serializer.data.get("new_password"))
#             self.object.save()
#             response = {
#                 'status': 'success',
#                 'code': status.HTTP_200_OK,
#                 'message': 'Password updated successfully',
#                 'data': []
#             }

#             return Response(response)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ProfileView(views.APIView):
#     permission_classes = [IsAuthenticated, ]
#     authentication_classes = [TokenAuthentication, ]

#     def get(self, request):
#         print(request.user)
#         try:
#             query = Profile.objects.get(prouser=request.user)
#             serializer = ProfileSerializers(query)
#             response_message = {"error": False, "data": serializer.data}
#         except:
#             response_message = {"error": True, "message": "Somthing is Wrong"}
#         return Response(response_message)


# class Updateprofile(views.APIView):
#     permission_classes = [IsAuthenticated, ]
#     authentication_classes = [TokenAuthentication, ]

#     def put(self, request):
#         try:
#             user = request.user
#             query = Profile.objects.get(prouser=user)
#             data = request.data
#             serializers = ProfileSerializers(
#                 query, data=data, context={"request": request})
#             serializers.is_valid(raise_exception=True)
#             serializers.save()
#             return_res = {"message": "Profile is Updated"}
#         except:
#             return_res = {"message": "Somthing is Wrong Try Again !"}
#         return Response(return_res)
