from django.urls import path

from .views import *

urlpatterns = [
    path("", AdvertList.as_view(), name="advert-list"),
    path("create/", AdvertCreate.as_view(), name="advert-create"),
    path("response/", UserResponseList.as_view(), name="advert-response"),
    path("response/search", SearchUserResponseList.as_view(), name="advert-response-search"),
    path("response/create/", UserResponseCreate.as_view(), name="advert-create-response"),
    path("update/<int:pk>/", AdvertUpdate.as_view(), name="advert-update"),
    path("delete/<int:pk>/", AdvertDelete.as_view(), name="advert-delete"),
    path("<slug:category>/<slug:slug>/", AdvertDetail.as_view(), name="advert-detail"),
]