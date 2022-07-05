from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="Home"),
    path('allCategories/', views.categories, name="Categories"),
    path('startDiscussion/<str:name>/', views.startDiscussion.as_view(), name="startDiscussion"),
    path('startDiscussion/<str:name>/<str:slug>/', views.questionReply.as_view(), name="questionReply"),
    path('handleSignUp/', views.handleSignUp, name="handleSignUp"),
    path('handleLogIn/', views.handleLogIn, name="handleLogIn"),
    path('handleLogOut/', views.handleLogOut, name="handleLogOut"),
    path('user_profile/<str:user>/', views.userProfile, name="userProfile"),
    path('contactToiDiscuss/', views.Contact.as_view(), name="Contact"),
    path('AboutTheDeveloper/', views.About, name="About"),
    path('set_as_default_pic/<str:user>/', views.set_default_pic, name="DefaultPicUploader"),
    path('update_pic/', views.update_pic, name="UpdateUserPic"),
    path('update_question/<str:name>/<str:slug>', views.update_question, name="UpdateQuestion"),
    path('update_reply/<int:r_id>/<str:name>/<str:slug>', views.update_reply, name="UpdateReply"),
    path('search-results/', views.search, name="Search"),
    path('update_private_profile/<str:user>/', views.privateProfile, name="privateProfile")
]
