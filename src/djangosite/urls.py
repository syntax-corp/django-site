"""djangosite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages import views as pageview
from products import views as prodview

urlpatterns = [
    path('', pageview.home_view),
    path('about/', pageview.about_view),
    path('contact/', pageview.contact_view),
    path('discord/', pageview.discord_view),
    path('youtube/', pageview.youtube_view),
    path('github/', pageview.github_view),
    path('product/', prodview.product_detail_view),
    path('create/', prodview.product_create_view),
    path('admin/', admin.site.urls),
]
