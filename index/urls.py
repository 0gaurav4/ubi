from django.urls import path
from .import views

urlpatterns=[
    path("",views.index, name="index"),
    path("about-us",views.about_us,name="about-us"),
    path("author-detail",views.profile,name="author-detail"),
    path("service/<int:cid>",views.service,name="service"),
    path("search",views.search,name="search"),
    path("service1",views.service_1,name="service1"),
    path("cart",views.Cart,name="cart"),
    path("change_quan",views.change_quan,name="change_quan"),
    path("get_cart_data",views.get_cart_data,name="get_cart_data"),
    path("payment_done",views.payment_done,name="payment_done"),
    path("payment_cancelled",views.payment_cancelled,name="payment_cancelled"),
    # path("process_payment",views.process_payment,name="process_payment"),ye
    path("video_l",views.video_l,name="video_l"),

]