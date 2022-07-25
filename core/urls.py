from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.loginView, name="login"),
    path('logout/', views.logoutView, name="logout"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('register', views.registerForm, name="reg_form"),
    path('reg', views.registerUser, name="reg"),
    path('cv-detail/<id>', views.view_PDF, name='cv-detail'),
    path('cv-download/<id>', views.generate_PDF, name='cv-download')

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
