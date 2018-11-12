# snippets/views.py
from django.contrib.auth.models import User # new
from rest_framework import generics

from .models import Snippet , Category , Carousel , Service, Tags,Profile , Inquiry, Concept
from .serializers import SnippetSerializer, CategorySerializer,UserSerializer, CarouselSerializer ,ServiceSerializer, TagsSerializer,ProfileSerializer,ConceptSerializer,InquirySerializer# new
from rest_framework import generics, permissions # new
from .permissions import IsOwnerOrReadOnly # new
from .permissions import IsOwner
from rest_framework.decorators import api_view # new
from rest_framework.response import Response # new
from rest_framework.reverse import reverse # new
from passlib.hash import pbkdf2_sha256
from django.contrib.auth.hashers import make_password



@api_view(['GET']) # new
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format),
        'carousels': reverse('carousel-list', request=request, format=format),
        'categories': reverse('category-list', request=request, format=format),
        'services': reverse('service-list', request=request, format=format),
        'tags': reverse('tags-list', request=request, format=format),
        'profile': reverse('profile-create', request=request, format=format),
        'register':reverse('user-register', request=request, format=format),
        'concepts':reverse('inquiry-concept', request=request, format=format),
        'inquiries':reverse('inquiry-create',request=request,format=format)
    })


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,) # new


    def perform_create(self, serializer): # new
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)


class UserList(generics.ListCreateAPIView): # new
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView): # new
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRegister(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

    def perform_create(self, serializer):
    	username = self.request.POST.get('username', '')
    	email = self.request.POST.get('email', '')
    	password = self.request.POST.get('password', '')
    	user = User.objects.create_user(username, email, password)
	

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,) # new


    def perform_create(self, serializer): # new
        serializer.save(owner=self.request.user)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)




class CarouselList(generics.ListCreateAPIView):
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,) # new


    def perform_create(self, serializer): # new
        serializer.save(owner=self.request.user)


class CarouselDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)


class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,) # new


    def perform_create(self, serializer): # new
        serializer.save(owner=self.request.user)


class ServiceListByCategory(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,) # new


    def perform_create(self, serializer): # new
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """
        This view should return a list of all models by
        the maker passed in the URL
        """
        categoryparent = self.kwargs['category']
        return Service.objects.filter(category=categoryparent)




class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)


class ConceptCreate(generics.ListCreateAPIView):
    queryset = Concept.objects.all()
    serializer_class = ConceptSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwner) # new


    def perform_create(self, serializer): # new
        serializer.save(owner=self.request.user)

class ConceptDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Concept.objects.all()
    serializer_class = ConceptSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)

class InquiryCreate(generics.CreateAPIView):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwner) # new


    def perform_create(self, serializer): # new
        serializer.save(owner=self.request.user)

class InquiryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwner,) #add admin too!




class TagsList(generics.ListCreateAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,) # new


    def perform_create(self, serializer): # new
        serializer.save()


class TagsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)


class ProfileCreate(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwner,) # new


    def perform_create(self, serializer): # new
        serializer.save(owner=self.request.user)


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwner,)

	def perform_create(self, serializer): # new
		serializer.save(owner=self.request.user)





