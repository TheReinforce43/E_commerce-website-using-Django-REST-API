from django.urls import path 


# import user related api view url 

from User.View.user_create_api import (
    UserSignUpView,
    UserLoginView,
    UserLogoutView,
    GetuserList_api
)


from User.View.group_permission_api import ( 
    # group api url 
    CreateGroupAPI,
    ListGroupsAPI,
    UpdateGroupAPI,
    RetrieveDestroyGroupAPI,

    # permission api url 
    CreateListPermissionAPI, 
    UpdateRetrieveDestroyPermissionAPI
)


urlpatterns = [

    # user related api url 
    path('signup/',UserSignUpView.as_view(),name='user_signup'),
    path('login/',UserLoginView.as_view(),name='user_login'),
    path('logout/',UserLogoutView.as_view(),name='user_logout'),
    path('list/',GetuserList_api.as_view(),name='user_list'),

    # group related api url 
    path('group/create/', CreateGroupAPI.as_view(), name='group_create'),
    path('group/list/', ListGroupsAPI.as_view(), name='group_list'),
    path('group/update/<int:pk>/', UpdateGroupAPI.as_view(), name='group_update'),
    path('group/delete/<int:pk>/', RetrieveDestroyGroupAPI.as_view(), name='group_delete'),
    path('group/retrieve/<int:pk>/', RetrieveDestroyGroupAPI.as_view(), name='group_retrieve'),

    # permission related api url 
    path('permission/create/', CreateListPermissionAPI.as_view(), name='permission_create'),
    path('permission/list/', CreateListPermissionAPI.as_view(), name='permission_create'),
    path('permission/update/<int:pk>/', UpdateRetrieveDestroyPermissionAPI.as_view(), name='permission_update'),
    path('permission/retrieve/<int:pk>/', UpdateRetrieveDestroyPermissionAPI.as_view(), name='permission_retrieve'),
    path('permission/delete/<int:pk>/', UpdateRetrieveDestroyPermissionAPI.as_view(), name='permission_delete'),
]
