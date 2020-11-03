from django.urls import path
from eventex.subscriptions.views import new, detail

app_name = 'subscriptions'

urlpatterns = [
    # Examples:
    # url(r'^$', 'eventex.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    path(r'', new, name='new'),
    path(r'<str:hashid>/', detail, name='detail'),
]