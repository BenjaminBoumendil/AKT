from django.conf.urls import url
from ex.views import ArtworkListView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', login_required(ArtworkListView.as_view()), name='index'),
]