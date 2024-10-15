from django.urls import path

from common.views import ContactCreateView

app_name = 'common'

urlpatterns = [
    path('contact/create/', ContactCreateView.as_view(), name='contact'),
]
