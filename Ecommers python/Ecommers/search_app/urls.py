from .import views
from django.urls import path

app_name='search_app'

urlpatterns = [

    path('',views.search_result,name='search_result'),

]
