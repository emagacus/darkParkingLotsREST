# snippets/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetail.as_view(), name='category-detail'),
    path('carousels/', views.CarouselList.as_view(), name='carousel-list'),
    path('carousels/<int:pk>/', views.CarouselDetail.as_view(), name='carousel-detail'),
    path('services/', views.ServiceList.as_view(), name='service-list'),
    path('services/<int:pk>/', views.ServiceDetail.as_view(), name='service-detail'),
    path('categories/<category>/services', views.ServiceListByCategory.as_view(),name='services-bycategory'),
    path('tags/', views.TagsList.as_view(), name='tags-list'),
    path('tags/<int:pk>/', views.TagsDetail.as_view(), name='tags-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('users/<int:pk>/profile', views.ProfileDetail.as_view(), name='user-profile'),
    path('profile/', views.ProfileCreate.as_view(), name='profile-create'),
    path('register/', views.UserRegister.as_view(), name='user-register'),
    path('concept/', views.ConceptCreate.as_view(), name='inquiry-concept'),
    path('concept/<int:pk>/', views.ConceptDetail.as_view(), name='inquiry-concepts'),
    path('inquiry/', views.InquiryCreate.as_view(), name='inquiry-create'),
    path('inquiry/<int:pk>/', views.InquiryDetail.as_view(), name='inquiry-detail'),
    path('parkings/new', views.ParkingCreate.as_view(), name='parking-create'),
    path('parkings/', views.ParkingsList.as_view(), name='parking-list'),
    path('status/', views.StatusList.as_view(), name='status-list'),
    path('status/<int:pk>/', views.StatusDetail.as_view(), name='status-detail'),
    path('predict', views.CustomGet.as_view(), name='predict'),
    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)