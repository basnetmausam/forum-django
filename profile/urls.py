from django.urls import path
from profile.views import ProfileAddLike, EditPhotoProfile, ProfileView, ProfileEditView, UserListView, UserCreateView, ConfigView

app_name = "profile"
urlpatterns = [
    path('config/', ConfigView.as_view(), name="config"),
    path('edit-profile', ProfileEditView.as_view(), name="edit-profile"),
    path('<slug:username>', ProfileView.as_view(), name="user-profile"),
    path('profile/<int:pk>/like', ProfileAddLike.as_view(), name='like-profile'),
    path('<int:pk>/photo/', EditPhotoProfile.as_view(), name='photo-profile'),
    path('usuarios/', UserListView.as_view(), name='users-profile'),
    path('usernew/', UserCreateView.as_view(), name='usernew'),
]
