from django.conf.urls import url
from views import RequestDemoView

urlpatterns = [
    url(r'^request-demo/$',RequestDemoView.as_view(), name="requestDemo"),
]
