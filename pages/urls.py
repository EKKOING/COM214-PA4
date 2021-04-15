from django.urls import path
from .views import AboutPageView, BootstraplessPageView, ContactPageView, HomePageView, PortfolioPageView, SocialsPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('porfolio/', PortfolioPageView.as_view(), name='portfolio'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('socials/', SocialsPageView.as_view(), name='socials'),
    path('socials/bootstrapless', BootstraplessPageView.as_view(), name='bootstrapless')
]
