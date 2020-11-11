from django.contrib import admin
from django.urls import path, include
from eventex.core.views import home, speaker_detail


urlpatterns = [
    # Examples:
    # url(r'^$', 'eventex.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    path(r'', home, name='home'),
    path('inscricao/', include('eventex.subscriptions.urls')),
    path('palestrantes/<slug:slug>/', speaker_detail, name='speaker_detail'),
    path(r'admin/', admin.site.urls),
]
