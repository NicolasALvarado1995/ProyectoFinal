from operator import index
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.authtoken.views import obtain_auth_token
from proyecto_final.muestro.views import  HomeView, EditarView,borrarview,Registerview,LoginView,EntradaView,MensajeriaView,UsuariosViews,editarv2,AvatarViews,RecibeMensajeView
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("index/",TemplateView.as_view(template_name="index/index.html"), name="template"),
    path("users/", include("proyecto_final.users.urls", namespace="users")),
    #path("accounts/", include("allauth.urls")),
    path("accounts/login", LoginView.as_view(), name= 'account_login'),# direccion para acceder al login 
    path("editar/<int:pk>", EditarView.as_view(), name='editar'),# direccion para editar usuarios 
    path("borrar/<int:pk>", borrarview.as_view(), name='borrar'),# direccion para borrar usuarios
    path("registro/",Registerview.as_view(), name='registro'),#este es para el administrador de django
    path("login/",LoginView.as_view(), name='login'),# direccion para acceder al login 
    path("logout",LogoutView.as_view(), name='logout'),# direccion para acceder al logout
    path("entrada", EntradaView.as_view(), name='entrada'),# direccion para acceder a la vista de crear post
    path("usuarios", UsuariosViews.as_view(), name='usuario'),# direccion para acceder a una lista de usuario 
    path("editarv2", editarv2.as_view(), name='editarv2'),# direccion para acceder a editar usuario por django
    path("avatar", AvatarViews.as_view(), name='avatar'),# direccion para acceder al avatar y su informacion
    path("mensajeria", MensajeriaView.as_view(), name='mensajeria'),# direccion para acceder a a la mensajeria
    path("mensajes", RecibeMensajeView.as_view(), name='mensajes'),#
    
    
    

    
    
    # Your stuff: custom urls includes go here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# API URLS
urlpatterns += [
    # API base url
    path("api/", include("config.api_router")),
    # DRF auth token
    path("auth-token/", obtain_auth_token),
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
