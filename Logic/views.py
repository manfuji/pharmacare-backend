
from django.http import HttpResponse
from rest_framework import viewsets, generics, views
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from Allmodels.models import Categories, Order, Product, Profile
from Logic.serializers import CategorySerializer, GetOrderSerializer, ListProductSerializer, OrderSerializer, ProductSerializer
from Accounts.serializers import ProfileSerializers
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from knox.auth import TokenAuthentication
import requests


class Products(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ListProductSerializer

    def post(self, request):
        pass
    # permission_classes = [IsAuthenticatedOrReadOnly, ]


class ProductsCategory(generics.GenericAPIView):
    # queryset = Product.objects.all()
    serializer_class = ListProductSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly, ]

    def post(self, request):
        category = request.data["category"]
        queryset = Product.objects.all().filter(category__iexact=category)
        if not queryset:
            return Response({
                "message": "Please this category has no products Yet"
            })
        serializer = ListProductSerializer(queryset, many=True)

        return Response(serializer.data)


class ProductApi(generics.GenericAPIView):
    queryset = Product.objects.all()
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, ]
    authentication_classes = (TokenAuthentication,)

    def post(self, request):
        # print(request.user, request.data["category"])
        productName = request.data["productName"]
        productPrice = request.data["productPrice"]
        status = request.data["status"]
        description = request.data["description"]
        category = request.data["category"]
        image = request.data["image"]
        print(category)
        Product.objects.create(productPrice=productPrice, productName=productName,
                               category=category, image=image, status=status, description=description, owner=request.user)
        return Response({
            "message": "Product Created Successfully"
        })


class OrderApi(generics.GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # url = "https://gsdfsms.pythonanywhere.com/api/callbacks/"
    # response = requests.get(url)
    # permission_classes = [IsAuthenticated, ]
    authentication_classes = (TokenAuthentication,)

    def post(self, request):
        for items in request.data:
            product = Product.objects.get(id=items["id"])
            Order.objects.create(productId=product, owner=request.user,
                                 amount=items["productPrice"], quantity=items["qty"])
            # print(items["productPrice"], items["id"],
            #       items["productName"], items["qty"])

        # product = request.data["productId"]
        # productId = Product.objects.get(id=product)
        # amount = request.data["amount"]
        # owner = request.user
        # quantity = request.data["quantity"]
        # payment = request.data["payment"]
        # orderComplete = request.data["orderComplete"]
        # print(items)

        return Response({
            "message": "items added to cart succesfully"
        })


class GetOrder(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    authentication_classes = (TokenAuthentication,)
    serializer_class = OrderSerializer

    def get(self, request):
        try:
            query = Order.objects.filter(owner=request.user.id)
            qt = GetOrderSerializer(query, many=True).data
            # print(data)
            data = {
                "data": qt
            }
        except:
            data = {"message": "Something went wrong"}

        print(data)
        return Response(data)

    # permission_classes = [IsAuthenticated, ]
    # authentication_classes = (TokenAuthentication,)
        return Response({"hello": "hello"})


class CategoryApi(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Categories.objects.all()
    # permission_classes = [IsAuthenticated, ]


class ProfileApiView(views.APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = (TokenAuthentication,)

    def put(self, request):
        user = request.user
        data = request.data
        try:
            print(data)
            query = Profile.objects.get(profileUser=user)
            serializer = ProfileSerializers(
                query, data=data, context={"request": request})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                user_response = {"message": "Profile has been updated"}
            else:
                user_response = {"message": "Please check the data well"}

        except:
            user_response = {"message": "Something went wrong..Try again"}

        return Response(user_response)


class GetProfileApi(views.APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = (TokenAuthentication,)

    def get(self, request):
        try:
            user = request.user
            query = Profile.objects.get(profileUser=user)
            body = ProfileSerializers(query).data
            user_details = {"data": body}

        except:
            user_details = {"data": "User data doesn't exist"}

        return Response(user_details)
