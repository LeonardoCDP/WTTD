from django.contrib import admin
from django.urls import path

from eventex.core.views import home
from eventex.subscriptions.views import subscribe

urlpatterns = [
    # Examples:
    # url(r'^$', 'eventex.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    path(r'', home),
    path(r'inscricao/', subscribe),
    path(r'^admin/', admin.site.urls),
]
