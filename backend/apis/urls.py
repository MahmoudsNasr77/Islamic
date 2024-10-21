app_name='apis'
from django.urls import path
from .views import HadithAPIView,HadithCreateAPIView,HadithUpdateAPIView,HadithRetrieveAPIView
urlpatterns = [
path("", HadithAPIView.as_view(), name="Hadith_list"),
path("create", HadithCreateAPIView.as_view(), name="Hadith_create"),
path("update/<int:id>/", HadithUpdateAPIView.as_view(), name="Hadith_update"),
path("retrieve/<int:id>/", HadithRetrieveAPIView.as_view(), name="Hadith_retrieve"),



]