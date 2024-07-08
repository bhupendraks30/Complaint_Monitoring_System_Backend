from django.db import models
from django.utils import timezone

# Create your models here.
# class User(models.Model):
#     name=models.CharField(max_length=100)
#     email=models.EmailField(max_length=254)
#     password=models.CharField(max_length=30)
#     image=models.ImageField(upload_to='images/profile_Images/',null=True,blank=True)
#     def __str__(self):
#         return str(self.name)
    
    


# add by anil
class User(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    
    ROLE_CHOICES = [
        (0, 'User'),
        (1, 'Admin'),
        # Add more roles if needed
    ]
    
    uid = models.CharField(max_length=12, unique=True, null=False, editable=False)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.TextField(max_length=1000)
    pin_code = models.CharField(max_length=10)
    password = models.CharField(max_length=255)
    
    image = models.ImageField(upload_to='images/profile_Images/', null=True, blank=True)
    role = models.IntegerField(choices=ROLE_CHOICES, default=0)  # Default role set to 0 (User)

    def save(self, *args, **kwargs):
        if not self.uid:
            today = timezone.now().strftime('%y%m%d')
            last_user = User.objects.last()  # Get the last user by creation order
            if last_user:
                last_uid = last_user.uid[-2:]
                new_uid = f'NIC{today}{int(last_uid) + 1:02}'
            else:
                new_uid = f'NIC{today}01'
            self.uid = new_uid
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name 
    
    
# add by a



# add by a


# add by a
class Complaint(models.Model):
    CATEGORY_CHOICES = [
        ('technical', 'Technical Issues'),
        ('service_quality', 'Service Quality'),
        ('data_security', 'Data Security'),
        ('training_support', 'Training and Support'),
        ('feedback_suggestions', 'Feedback and Suggestions'),
        ('general_inquiries', 'General Inquiries'),
        ('Land Records', 'Land Records'),
        ('Public Distribution System', 'Public Distribution System'),
        ('Election', 'Election'),
        ('Social Welfare', 'Social Welfare'),
        ('Health Services', 'Health Services'),
        ('Taxation', 'Taxation'),
        ('Law and Order', 'Law and Order'),
        ('Education', 'Education'),
        ('Public Transport', 'Public Transport'),
        ('Water Transport', 'Water Transport'),
        ('Water Supply', 'Water Supply'),
        ('Electricity', 'Electricity'),
        ('Sanitation', 'Sanitation'),
        ('Environmental Issues', 'Environmental Issues'),
        ('Infrastructure', 'Infrastructure'),
        ('Public', 'Public'),
        ('Visitor', 'Visitor'),
    ]
    
    Status = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Reject', 'Reject'),
        # Add more roles if needed
    ]
    

    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.TextField(max_length=1000)
    pin_code = models.CharField(max_length=10)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name='Category')
    description = models.TextField(verbose_name='Description')
    date_submitted = models.DateTimeField(auto_now_add=True, verbose_name='Date Submitted')
    status = models.CharField(max_length=50, default='Pending', choices=Status)
    cid = models.CharField(max_length=12, unique=True, null=False, editable=False)  # Unique complaint ID
    
    def save(self, *args, **kwargs):
        if not self.cid:
            today = timezone.now().strftime('%y%m%d')
            last_complaint = Complaint.objects.filter(date_submitted__date=timezone.now().date()).order_by('-id').first()
            if last_complaint:
                last_cid = last_complaint.cid[-2:]
                new_cid = f'COM{today}{int(last_cid) + 1:02}'
            else:
                new_cid = f'COM{today}01'
            self.cid = new_cid
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.cid} - {self.category}'

    class Meta:
        verbose_name = 'Complaint'
        verbose_name_plural = 'Complaints'


# add by a 

# add by a  
    
    
    
    
    
    
    
    

class Category(models.Model):    
    name = models.CharField(max_length=250,null=True, blank=True)

class TourPlace(models.Model):
    name = models.CharField(max_length=250,null=True, blank=True)
    description = models.CharField(max_length=250,null=True, blank=True)
    categoty_name =models.ForeignKey(to=Category,on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to="Images/Dam/",null=True,blank=True)
    image2 = models.ImageField(upload_to="Images/Dam/",null=True,blank=True)
    image3 = models.ImageField(upload_to="Images/Dam/",null=True,blank=True)
    video1_link = models.CharField(max_length=1200,null=True, blank=True)
    video2_link = models.CharField(max_length=1200,null=True, blank=True)
    video3_link = models.CharField(max_length=1200,null=True, blank=True)
    video4_link = models.CharField(max_length=1200,null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    popular = models.BooleanField()
    popular = models.BooleanField()