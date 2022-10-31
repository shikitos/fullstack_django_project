from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    # Native path to access the django admin
    path('admin/', admin.site.urls),
    # Path to access the frontend page
    path('', views.frontend, name="frontend"),
    # Path to access the backend page
    path('backend/', views.backend, name="backend")
]
