from django.urls import path

from .views import registration,customLOgin,listview,Delete,Update,TransactionCreate,get_history,feedback,user_history,ReservationCreateView,ListReservations,DeleteReservation,listreserve,Deleteone,post_feedback
from django.contrib.auth.views import LogoutView


urlpatterns=[
   path('register/', registration, name='registration'),
   path('',customLOgin.as_view(),name='login'),
   path('logout/', LogoutView.as_view(), name='logout'),
   path('allocated_laptops/', listview.as_view(), name='allocated_laptops'),
   path('delete/<int:pk>/',Delete.as_view(),name='deleteadmin'),
   path('update/<int:pk>/',Update.as_view(),name='updatee'),
   path('transaction/',TransactionCreate.as_view(),name='create'),
   path('history_list/', get_history, name='history_list'),
   path('user/',user_history,name='userpage'),
   path('reservation/', ReservationCreateView.as_view(), name='reservation'),
   path('view/',ListReservations.as_view(),name='listreser'),
   path('dlt/<int:pk>/',DeleteReservation.as_view(), name='deletereservation'),
   path('deleet/<int:pk>/',Deleteone.as_view(), name='delete'),
   path('list',listreserve.as_view(),name='adminreservation'),
   path('postfeedback/', post_feedback, name='post_feedback'),
   
 
 
]