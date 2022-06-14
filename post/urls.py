from django.urls import path
from .views import blogpage, createpost, detailview

app_name = "post"

urlpatterns = [
    path("", blogpage, name="blogpage"),
    path("createpost/", createpost, name = "create_post"),
    path("detail/<int:ID>", detailview, name="detailview")
]
