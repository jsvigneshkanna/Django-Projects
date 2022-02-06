from django.contrib import admin
from django.urls import path, include

# Main Project UrlsConfig
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('polls.urls')),  # This will be the starting point for poll App routing 🚀
]
