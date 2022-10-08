from django.urls import path

from api.cpanel.book_ride import order_ride
from api.cpanel.login_user import MyTokenObtainPairView, get_user_profile, get_users, update_user_profile
from api.cpanel.marketing_controller import marketing
from api.cpanel.myfeedback import register_comment, detail_feedback, delete_feedback
from api.cpanel.register_boda import register_boda
from api.cpanel.register_driver import register_driver
from api.cpanel.register_passenger import register_passenger
from api.cpanel.research_controller import research

urlpatterns = [
    # authenticate users
    path('users/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register_passenger/', register_passenger, name='register_passenger'),
    path('register_driver/', register_driver, name='register_driver'),
    path('register_boda/', register_boda, name='register_boda'),

    #     Profiles
    path('users/profile/', get_user_profile, name='users-profile'),
    path('users/profile/update/', update_user_profile, name='users-profile-update'),

    # admin urls
    path('users/', get_users, name='users'),

    #     Feedbacks
    path('add_feedback/', register_comment, name='add_feedback'),
    path('feedback/detail/<str:pk>', detail_feedback, name='feedback-detail'),
    path('feedback/delete/<str:pk>', delete_feedback, name='feedback-delete'),
    #     Marketing & Research
    path('marketing/', marketing, name='marketing'),
    #     Research
    path('research/', research, name='research'),
    #     Order Rides
    path('order_ride/', order_ride, name='order_ride'),
]
