from django.shortcuts import render
from rest_framework.views import APIView,Response
from .models import *
from rest_framework import status
from .serializers import *
from django.http import JsonResponse

# Create your views here.
# class RegesterUSer(APIView):
#     def post(self,request): 
#        try:    
#             count=User.objects.all().filter(email=request.data['email']).count() 
#             if count==0:
#                 User.objects.create(
#                 name=request.data['name'],
#                 email=request.data['email'],
#                 password=request.data['password'],
#                 image=request.FILES.get('image'),
#                 ).save()
#                 isCreated= (User.objects.all().filter(email=request.data['email']).count()==0)
#                 if not isCreated:
#                     return Response({"code":"200","message":"Registration succesfully"})
#                 else:
#                     return Response({"code":"200","message":"Registration failed !"})              
#             else:
#                 return Response({"code":"200","message":"user allready exist"})            
#        except Exception as e:
#            return Response({"error":e})



# add by a
# class RegisterUser(APIView):
#     def post(self, request):
#         try:
#             # Check if the user already exists
#             count = User.objects.filter(email=request.data['email']).count()
#             if count == 0:
#                 # Create a new user
#                 User.objects.create(
#                     full_name=request.data['full_name'],
#                     email=request.data['email'],
#                     mobile_number=request.data['mobile_number'],
#                     gender=request.data['gender'],
#                     state=request.data['state'],
#                     district=request.data['district'],
#                     city=request.data['city'],
#                     address=request.data['address'],
#                     pin_code=request.data['pin_code'],
#                     password=request.data['password'],
#                     image=request.FILES.get('image'),
#                     role=request.data['role']
#                 ).save()

#                 # Check if the user was successfully created
#                 isCreated = User.objects.filter(email=request.data['email']).count() == 1
#                 if isCreated:
#                     return Response({"code": "200", "message": "Registration successful"})
#                 else:
#                     return Response({"code": "200", "message": "Registration failed"})
#             else:
#                 return Response({"code": "200", "message": "User already exists"})
#         except Exception as e:
#             return Response({"error": str(e)})


class RegisterUserAPIView(APIView):
    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'code':'200', 'message':'Registrationn Successful'}, status=status.HTTP_201_CREATED)
            return Response({'code':'400', 'message':serializer.errors}, status=200)
        except Exception as e:
            return Response({'code':'500',"error": str(e)}, status=200)



# and by a 


class RegisterUserCreateView(APIView):
    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                # Save the validated data and create a new user
                serializer.save()
                return Response({"code": "201", "message": "Registration successful"}, status=status.HTTP_201_CREATED)
            # If serializer is not valid, return errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # Handle any other exceptions and return 500 error
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



#add by  a start
class LoginUser(APIView):
    def post(self, request):
        try:
            email = request.data.get('email')
            password = request.data.get('password')
            
            # Check if user with given email exists
            user = User.objects.filter(email=email).first()
            
            if user:
                # User exists, now check password
                if user.password == password:
                    # Password matches, prepare response
                    userData=User.objects.filter(email=email).values()
                    response_data = {
                        "code": "200",
                        "message": "Login successfully",
                        "user_details": userData
                    }
                    return Response(response_data)
                else:
                    # Password does not match
                    return Response({"code": "400", "message": "Incorrect password"})
            else:
                # User not registered
                return Response({"code": "401", "message": "User not registered"})
        except Exception as e:
            return Response({"code": "500", "message": "Exception occurred", "exception_details": str(e)})
#add by  a end 



# add by a

class ComplaintListCreateAPIView(APIView):
    def post(self, request):
        try:
            serializer = ComplaintSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'code':'200','message':'Complaint registered successful','complaint_details':serializer.data}, status=status.HTTP_201_CREATED)
            print(serializer.errors)
            return Response({'code':'400','error':serializer.errors}, status=400)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)       




class ComplaintDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            print(pk)
            cdd = Complaint.objects.get()
            print(cdd)
            return {"Complaint.objects.get(cid=pk)"}
        except Complaint.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        complaint = self.get_object(pk)
        serializer = ComplaintSerializer(complaint)
        return Response(serializer.data)

    def put(self, request, pk):
        complaint = self.get_object(pk)
        serializer = ComplaintSerializer(complaint, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        complaint = self.get_object(pk)
        complaint.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# add by a






def pending_complaints_view(request):
    pending_complaints = Complaint.objects.filter(status='Pending')
    complaints_list = list(pending_complaints.values())
    count = pending_complaints.count()
    return JsonResponse({'pending_complaints': complaints_list, 'cout':count})

def approved_complaints_view(request):
    approved_complaints = Complaint.objects.filter(status='Approved')
    complaints_list = list(approved_complaints.values())
    count = approved_complaints.count()
    return JsonResponse({'approved_complaints': complaints_list, 'cout':count})

def reject_complaints_view(request):
    rejected_complaints = Complaint.objects.filter(status='Reject')
    complaints_list = list(rejected_complaints.values())
    count = rejected_complaints.count()
    return JsonResponse({'rejected_complaints': complaints_list, 'cout':count})


def all_complaints_view(request):
    all_complaints = Complaint.objects.all()
    complaints_list = list(all_complaints.values())
    count = all_complaints.count()
    return JsonResponse({'all_complaints': complaints_list, 'cout':count})





class GetRegisteredComplaints(APIView):
    def post(self,request):
        registered_complaints = Complaint.objects.filter(uid=request.data.get('uid'))
        complaints_list = list(registered_complaints.values())
        count = registered_complaints.count()
        return JsonResponse({'registered_complaints': complaints_list, 'cout':count})
    
class GetAllRegisteredComplaints(APIView):
    def get(self,request):
        registered_complaints = Complaint.objects.all()
        complaints_list = list(registered_complaints.values())
        count = registered_complaints.count()
        return Response({'registered_complaints': complaints_list, 'cout':count})
    


    
class GetPendingComplaints(APIView):
    def post(self,request):
        registered_complaints = Complaint.objects.filter(status='Pending',uid=request.data.get('uid'))
        complaints_list = list(registered_complaints.values())
        count = registered_complaints.count()
        return JsonResponse({'registered_complaints': complaints_list, 'cout':count})
    
class GetAllPendingComplaints(APIView):
    def get(self,request):
        registered_complaints = Complaint.objects.filter(status='Pending')
        complaints_list = list(registered_complaints.values())  
        count = registered_complaints.count()
        return Response({'registered_complaints': complaints_list, 'cout':count})
    

    
class GetResolvedComplaints(APIView):
    def post(self,request):
        registered_complaints = Complaint.objects.filter(status='Approved',uid=request.data.get('uid'))
        complaints_list = list(registered_complaints.values())
        count = registered_complaints.count()
        return JsonResponse({'registered_complaints': complaints_list, 'cout':count})
class GetAllResolvedComplaints(APIView):
    def get(self,request):
        registered_complaints = Complaint.objects.filter(status='Approved')
        complaints_list = list(registered_complaints.values())
        count = registered_complaints.count()
        return Response({'registered_complaints': complaints_list, 'cout':count})
    

    
class GetRejectedComplaints(APIView):
    def post(self,request):
        registered_complaints = Complaint.objects.filter(status='Reject',uid=request.data.get('uid'))
        complaints_list = list(registered_complaints.values())
        count = registered_complaints.count()
        return JsonResponse({'registered_complaints': complaints_list, 'cout':count})
class GetAllRejectedComplaints(APIView):
    def get(self,request):
        registered_complaints = Complaint.objects.filter(status='Reject')
        complaints_list = list(registered_complaints.values())
        count = registered_complaints.count()
        return Response({'registered_complaints': complaints_list, 'cout':count})
    
class UpdateComplaintStatuse(APIView):
    def post(self,request):
        complaint = Complaint.objects.get(cid=request.data.get('cid'))
        if not complaint:
            return JsonResponse({'code':'400','message':'Complaint not found'})
        complaint.status = request.data.get('status')
        complaint.save()
        return JsonResponse({'code':'200','message':'Complaint status successfully changed'})
    

class GetComplaintDetails(APIView):
    def post(self,request):
        complaint = Complaint.objects.all().filter(uid=request.data['uid'],cid=request.data['cid']).values()
        if not complaint:
            return Response({'code':'400','message':'Complaint not found'})
        # complaint_details = complaint.values()
        print(complaint)
        return Response({'code':'200','complaint_details':complaint})



# class LoginUser(APIView):
#     def post(self,request):
#         try:
#             count = User.objects.all().filter(email=request.data['email']).count()
#             if(count==1):
#                 count2=User.objects.all().filter(password=request.data['password'],email=request.data['email']).count()
#                 if count2==1:
#                     user=User.objects.all().filter(password=request.data['password'],email=request.data['email']).values()
#                     return Response({"code":"200","message":"Login succesfully","User detials": user})
#                 else:
#                     return Response({"code":"400","message":"Given password is incorrect"})
#             else:
#                 return Response({"code":"401","message":"User not registered"})
#         except Exception as e:
#             Response({"Exception ":e})




class DeleteUser(APIView):
    def delete(self,request):
        try:
            User.objects.all().filter(id=request.data['id'],email=request.data['email']).delete()
            isDeleted=(User.objects.all().filter(id=request.data['id']).count!=0)
            if isDeleted:
                return Response({"code":"200","message":"User succesfully deleted"})
            else:
                return Response({"code":"500","message":"Something went wrong account is not deleted."})    
        except Exception as e:
            print("error",e)

class UpdatePassword(APIView):
    def post(self, request):
        try:            
            user=User.objects.all().filter(id=request.data['id'],email=request.data['email']).values()
            if not user:
                return Response({"code":"404","message":"User not found",})
            User.objects.all().filter(id=request.data['id'],email=request.data['email']).update(password=request.data['password'])
            return Response({"code":"200","message":"Password succesfully changed"})
        except Exception as e:
            print('error ',e)
            return Response({"code":"500","message":"Some thing went wrong"})


# class UpdateProfileImage(APIView):
#     def post(self, request):
#         try:            
#             user=User.objects.all().filter(id=request.data['id'],email=request.data['email']).values()
#             if not user:
#                 return Response({"code":"404","message":"User not found",})
#             User.objects.all().filter(id=request.data['id'],email=request.data['email']).update(image=request.FILES.get('image'))
#             user =User.objects.all().filter(id=request.data['id'],email=request.data['email']).values()
#             return Response({"code":"200","message":"Profile succesfully changed","userDetails":user})
#         except Exception as e:
#             print('error ',e)
#             return Response({"code":"500","message":"Some thing went wrong"})


class UpdateProfileImage(APIView):
    def post(self, request):
        try:

            try:
                user = User.objects.get(id=request.data['id'], email=request.data['email'])
            except User.DoesNotExist:
                return Response({"code": "404", "message": "User not found"})

            if 'image' in request.FILES:
                user.image = request.FILES['image']
                user.save()
                user1 = User.objects.all().filter(id=request.data['id'], email=request.data['email']).values()
                return Response({"code": "200", "message": "Profile successfully changed", "userDetails": user1})
            else:
                return Response({"code": "400", "message": "Image file is missing"})
        
        except Exception as e:
            print('error', e)
            return Response({"code": "500", "message": "Something went wrong"})