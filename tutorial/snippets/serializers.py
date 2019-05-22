from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES, Category, Carousel , Service ,Tags ,Profile ,Inquiry ,Concept,Parking,Status
from django.contrib.auth.models import User













class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username') # new

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos',
                  'language', 'style', 'owner',) # new




class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'email','snippets','password',)


class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username') # new
    class Meta:
        model = Category
        fields = ('id', 'title','description','cost','minPeople','maxPeople','isEnabled','owner',)


class CarouselSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username') # new
    category = serializers.PrimaryKeyRelatedField(many=False, queryset=Category.objects.all())
    
    class Meta:
        model = Carousel
        fields = ( 'title','imgSrc','category','isEnabled','owner','category',)

class ServiceSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username') # new
    category = serializers.PrimaryKeyRelatedField(many=False, queryset=Category.objects.all())
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tags.objects.all())

    class Meta:
        model = Service
        fields = ( 'id','description','title','category','differential','isEnabled','owner','category','minPeople','maxPeople','imgsrc','isAvailable','tags',)


class ConceptSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username') # new
    service = serializers.PrimaryKeyRelatedField(many=False, queryset=Service.objects.all())
    inquiry = serializers.PrimaryKeyRelatedField(many=False, queryset=Inquiry.objects.all())

    class Meta:
        model = Concept
        fields = ( 'inquiry','quantity','service','owner','subtotal',)

class InquirySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username') # new
    
    class Meta:
        model = Inquiry
        fields = ( 'created','details','total','owner',)


class InquiryDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username') # new
    
    class Meta:
        model = Inquiry
        fields = ( 'created','details','total','owner',)


class TagsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tags
        fields = ( 'name','relatedname1','relatedname2',)

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username') # new

    class Meta:
        model = Profile
        fields = ( 'name','email','phonenumber','phonenumber2','owner',)

class ParkingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username') # new

    class Meta:
        model = Parking
        fields = ( 'created','title','coordinates','address','capacity','owner')

class StatusSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username') # new
    parking = serializers.PrimaryKeyRelatedField(many=False, queryset=Parking.objects.all())
    class Meta:
        model = Status
        fields = ( 'created','freespaces','occupied','parking','owner')
