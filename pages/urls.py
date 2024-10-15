from django.urls import path

from pages.views import HomeView, ContactView, PageNotFoundView, AboutUsView

app_name = 'pages'

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('404/', PageNotFoundView.as_view(), name='404'),
    path('about-us/', AboutUsView.as_view(), name='about_us'),

    path('', HomeView.as_view(), name='home'),
]
