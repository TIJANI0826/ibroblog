"""ibroblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^weblog/', include('zinnia.urls')),
    url(r'^comments/', include('django_comments.urls')),


]

# blog_urls = ([
#     url(r'^', include('zinnia.urls.capabilities')),
#     url(r'^search/', include('zinnia.urls.search')),
#     url(r'^sitemap/', include('zinnia.urls.sitemap')),
#     url(r'^trackback/', include('zinnia.urls.trackback')),
#     url(r'^blog/tags/', include('zinnia.urls.tags')),
#     url(r'^blog/feeds/', include('zinnia.urls.feeds')),
#     url(r'^blog/random/', include('zinnia.urls.random')),
#     url(r'^blog/authors/', include('zinnia.urls.authors')),
#     url(r'^blog/categories/', include('zinnia.urls.categories')),
#     url(r'^blog/comments/', include('zinnia.urls.comments')),
#     url(r'^blog/', include('zinnia.urls.entries')),
#     url(r'^blog/', include('zinnia.urls.archives')),
#     url(r'^blog/', include('zinnia.urls.shortlink')),
#     url(r'^blog/', include('zinnia.urls.quick_entry'))
# ], 'zinnia')

# url(r'^', include(blog_urls))

