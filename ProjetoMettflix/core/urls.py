from django.urls import path
from .views import *

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("like/<int:id>", put_like, name="like"),
    path("dislike/<int:id>", put_deslike, name="dislike"),
    path("download/<int:id>", put_download, name="download"),
    path("loginconta/", LoginView.as_view(), name="loginconta"),
    path("fazerlogin/", login_request, name="fazerlogin"),
    path("obra/<slug:slug>", ObraView.as_view(), name="obra"),
    path("cadastro/", RegisterView.as_view(), name="cadastro"),
    path("fazercasdastro/", register_request, name="fazercasdastro"),
    
]

