"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from complaint import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('registerUser/',views.RegisterUser().as_view()),
    path('register/', views.RegisterUserAPIView.as_view(), name='register-user'),
    path('deleteUser/',views.DeleteUser().as_view()),
    path('updateUserPassword/',views.UpdatePassword().as_view()),
    path('loginUser/',views.LoginUser().as_view()),
    path('updateUserProfile/',views.UpdateProfileImage().as_view()),
    
    
    
    path('complaints/', views.ComplaintListCreateAPIView.as_view(), name='complaint-list-create'),
    path('complaints/<str:pk>/', views.ComplaintDetailAPIView.as_view(), name='complaint-detail'),
    
    path('pending-complaints/', views.pending_complaints_view, name='pending_complaints'),
    path('approved-complaints/', views.approved_complaints_view, name='approved_complaints'),
    path('reject-complaints/', views.reject_complaints_view, name='reject_complaints'),
    
    
    path('all_Complaints/', views.all_complaints_view, name='all_complaints'),
    path('get_registered_Complaints/', views.GetRegisteredComplaints.as_view(), name='get_registered_complaints'),    
    path('get_all_registered_Complaints/', views.GetAllRegisteredComplaints.as_view(), name='get_all_registered_complaints'),

    path('get_pending_Complaints/', views.GetPendingComplaints.as_view(), name='get_pending_Complaints'),
    path('get_all_pending_Complaints/', views.GetAllPendingComplaints.as_view(), name='get_all_pending_Complaints'),

    path('get_resolved_Complaints/', views.GetResolvedComplaints.as_view(), name='get_resolved_Complaints'),
    path('get_all_resolved_Complaints/', views.GetAllResolvedComplaints.as_view(), name='get_all_resolved_Complaints'),

    path('get_rejected_Complaints/', views.GetRejectedComplaints.as_view(), name='get_rejected_Complaints'),
    path('get_all_rejected_Complaints/', views.GetAllRejectedComplaints.as_view(), name='get_all_rejected_Complaints'),

    path('update_complaint_status/', views.UpdateComplaintStatuse.as_view(), name='update_complaint_status'),
    path('search_complaints/', views.GetComplaintDetails.as_view(), name='search_complaints'),
    



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


 