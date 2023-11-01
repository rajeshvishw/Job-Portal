from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path("",views.homeView,name= "index"),
    path("signup/",views.signupView,name="signup"),
    path("register/",views.register,name="Register"),
    path("otppage/",views.otpveryfyView,name="otp"),
    path("",views.login,name="login"),
    path("profile/<int:pk>/",views.profile,name="profile"),
    path("updateProfile/",views.updateProfile,name="updateProfile"),
    path("updateProfile/<int:pk>/",views.updateProfile,name="updateProfile"),
    path("company/",views.companyView,name="companyView"),
    path("profileecompany/<int:pk>/",views.profileView,name="profileecompany")
]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
