from .import views
from django.urls import path
app_name='app1'

urlpatterns = [
    path('',views.allProduct,name='allProduct'),
    path('<slug:c_slug>/',views.allProduct,name='product_by_category'),
    path('<slug:c_slug>/<slug:p_slug>/',views.proDetails,name='procatdetails'),

    ]
