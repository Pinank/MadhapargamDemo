"""MadhaparDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from snippets import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router = DefaultRouter(schema_title='Pastebin API')
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    # url(r'^snippets/', include('snippets.urls')),
    url(r'^category/', include('Category.urls')),
    url(r'^location/',include('Location.urls')),
    url(r'^gamuser/',include('gamuser.urls')),
    url(r'^event/',include('Events.urls')),
    url(r'^deviceInfo/',include('DeviceInfo.urls')),
    url(r'^newsFeed/',include('NewsFeed.urls')),
    url(r'^project/',include('Projects.urls')),
    url(r'^otp/',include('OTPInfo.urls')),
    url(r'^feedback/',include('Feedback.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]