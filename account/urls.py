from django.urls import path
from .import views

urlpatterns=[
    path("",views.index,name="index"),
    path("register",views.register,name="register"),
    path("login",views.login,name="login"),
    path("profile",views.cprofile,name="profile"),
    path("logout",views.logout,name="logout"),
    path("update",views.update,name="update"),
    path("abt",views.about,name="about"),
    path("authdet",views.authordetail,name="author_detail"),
    path("auth",views.authors,name="authors"),
    path("blgdet",views.blogdetail,name="blog_detail"),
    path("blgfl",views.blogfull,name="blogfull"),
    path("blg",views.blog,name="blog"),
    path("bkdet",views.bookdetail,name="bookdetail"),
    path("blside1",views.blside1,name="book_listing_1_w_sidebar"),
    path("blist",views.blisting,name="book_listing_1"),
    path("blside2",views.blside2,name="book_listing_2_w_sidebar"),
    path("cart",views.cart,name="cart"),
    path("cnt",views.contact,name="contact"),
    path("payf",views.payfailed,name="payfailed"),
    path("pays",views.paysucess,name="paysucess"),
    path("proc",views.processpay,name="processpay"),
]