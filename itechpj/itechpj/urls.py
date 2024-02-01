"""
URL configuration for itechpj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from itech import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('addPost', views.Apost, name='Apost'),
    path('viewPost/<int:pk>', views.view_post, name='viewpost'),
    path('profile',views.profile, name='profile'),
    path('editProfile', views.editprofile, name="eProfile"),
    path('editProfile/discription', views.editprofileD, name="eProfileD"),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('like', views.like_post, name='like_post'),
    path('add_comment/<int:id>', views.add_comment, name='add_comment'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)