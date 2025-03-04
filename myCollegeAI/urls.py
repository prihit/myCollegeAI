from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from base import views as base_views
from base.views import PsychoView, CompareView

from leads.views.public import ContactUs, ReferView

from profiles.views.authentication import (
    LoginView,
    LogoutView,
    RegisterView
)

from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site

handler404 = 'base.views.custom_not_found_error'
handler500 = 'base.views.custom_internal_error'
handler403 = 'base.views.custom_not_found_error'
handler400 = 'base.views.custom_not_found_error'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base_views.home, name='home'),
    path('college/', include(('college.urls', 'college'), namespace='college')),
    path('profile/', include(('profiles.urls', 'profile'), namespace='profile')),
    path('login/', LoginView.as_view(), name='login'),
    path('accounts/', include('allauth.urls')),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('logout/', LogoutView.as_view(), name='logout'),
    #   path('social-auth/', include('social_django.urls', namespace="social")),
    path('register/', RegisterView.as_view(), name='register'),
    path('contact/', ContactUs.as_view(), name='contact'),
    path('refer', ReferView.as_view(), name='refer'),
    path('about', base_views.about, name='about'),
    path('contact', base_views.contact, name='contact'),
    path('career', base_views.career, name='career'),
    path('advertising', base_views.advertising, name='advertising'),
    path('terms', base_views.terms, name='terms'),
    path('privacy',  base_views.privacy, name='privacy'),
    path('social', include('social_django.urls', namespace='social')),
    path('psychometric', PsychoView.as_view(), name='psycho'),
    path('compare', CompareView.as_view(), name='compare'),
    path('robots.txt', TemplateView.as_view(template_name="v2/seo/robots.txt", content_type="text/plain"), name='robots'),
    path('sitemap.xml', TemplateView.as_view(template_name="v2/seo/sitemap.xml", content_type="text/plain"), name='sitemap')
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    ) + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
