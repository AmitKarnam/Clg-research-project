from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
from django.conf import settings

# Create your models here.

# class MyAccountManager is an Manger class used to manage the Custom User Model we have created.
# It contains 2 funtions : create_user and create_superuser which as their name sugests create user nad superuser respectively.
class MyAccountManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError("User must have an email address")
        if not username:
            raise ValueError("User should have an name")
        
    
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            

        )

        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self,email,username,password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            

        )


        user.is_admin     = True
        user.is_staff     = True
        user.is_superuser = True 

        user.save(using=self._db)
        return user


# This is the Custom User Model, it has to contain is_admin,is_active,is_staff,is_superuser otherwise Custom Model User dosent work.
# The User Model is named as Account
#  
class Account(AbstractBaseUser):


    Department = [

        ('ECE','ECE'),
        ('CSE','CSE'),
        ('ISE','ISE'),
        ('MECH','MECH'),
        ('IEM','IEM'),
        ('PHYSICS','PHYSICS'),
        ('CHEMISTRY','CHEMISTRY'),
        ('MATHS','MATHS'),
        ('CIVIL','CIVIL'),
        ('MBA','MBA'),
        ('EIE','EIE'),
        
    ]

    # Follwoing are all the fields that are stored about the user.

    email         = models.EmailField(verbose_name="email",max_length=75,unique=True)
    username      = models.CharField(max_length=100,)
    date_joined   = models.DateTimeField(verbose_name='date joined',auto_now_add=True)
    last_login    = models.DateTimeField(verbose_name='last login',auto_now=True)
    is_admin      = models.BooleanField(default=False)
    is_active     = models.BooleanField(default=True)
    is_staff      = models.BooleanField(default=False)
    is_superuser  = models.BooleanField(default=False)
    PF_number     = models.CharField(max_length=50)
    designation   = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    department    = models.CharField(max_length=20,choices=Department)

    # The attribute 'USERNAME_FIELD' is used for the authentication purpose. Here in our case email field is used as a unique identifier for the authentication purpose.
    # The attribute 'REQUIRED_FIELDS' defines a list of items that are required and cannot be left empty.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = MyAccountManager()


    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_Label):
        return True

# Models to store Research data :  In all the models that follows frm here email id of the teacher is used as the ForeignKey to store the details of the particular user.

# 1) publication model takes care of all the publication data regarding toa user.
class publication(models.Model):

    Publication_type = [
        ('National Web of Science Conference','National Web of Science Conference'),
        ('International Web of Science Conference','International Web of Science Conference'),
        ('Web of Science Journal','Web of Science Journal'),
        ('Scopus Indexed Conference','Scopus Indexed Conference'),
        ('Scopus Indexed Journal','Scopus Indexed Journal'),
        ('National Conference Paper','National Conference Paper'),
        ('International Conference Paper','International Conference Paper'),
        ('Journal Papers (other than WoS/SI/SCI)','Journal Papers (other than WoS/SI/SCI)'),
        ('Book Chapter','Book Chapter'),
    ]

    Publication_status = [
        ('Accepted and yet to be published','Accepted and yet to be published'),
        ('Accepted and published','Accepted and  published')
    ]

    teacher_email_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='publications')
    paper_title = models.CharField(max_length=50)
    paper_authors = models.TextField()
    issn_or_issbn = models.CharField(max_length=1000)
    journal_name_or_conference_name = models.CharField(max_length=100)
    publication_type = models.CharField(max_length=50,choices=Publication_type)
    date_of_publication = models.DateField()
    DOI = models.CharField(max_length=200)
    impact_factor = models.FloatField()
    publication_status = models.CharField(max_length=700,choices = Publication_status)


    def __str__(self):
        return self.teacher_email_id.username +" : " + self.paper_title

# 2) research_grant model is used to collect info on all the research_grant of a particular teacher.
class research_grant(models.Model):

   Research_grant_status = [
        ('Submitted and waiting for result','Submitted and waiting for result'),
        ('Approved and funds not released','Approved and funds not released'),
        ('Approved and fund granted','Approved and fund granted'),
        ('Work ongoing','Work ongoing'),
        ('Completed','Completed'),
    ]

   teacher_email_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='research_grants')
   project_title = models.CharField(max_length=100)
   principle_investigator_name = models.CharField(max_length=100) 
   co_principle_investigator_name = models.CharField(max_length=100)
   funding_agency = models.CharField(max_length=100)
   total_amount_granted = models.IntegerField()
   granted_amount = models.IntegerField()
   scheme = models.CharField(max_length=100)
   project_status = models.CharField(max_length=100,choices=Research_grant_status)
   granted_date  = models.DateField()
   submitted_date  = models.DateField()

   def __str__(self):
       return self.teacher_email_id.username +" : " + self.project_title


# 3) patent model is used to collect info on all the patent of a particular teacher.
class patent(models.Model):

    Patent_origin = [
        ('Indian Patent','Indian Patent'),
        ('Foreign Patent','Foreign Patent')
    ]

    Patent_status = [
        ('Filed','Filed'),
        ('Published','Published'),
        ('Granted','Granted')
    ]

    teacher_email_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='patents')
    authors = models.TextField()
    patent_application_number = models.CharField(max_length=200)
    patent_title = models.CharField(max_length=200)
    inventor = models.CharField(max_length=400)
    patent_origin = models.CharField(max_length=100,choices=Patent_origin)
    patent_status = models.CharField(max_length=100,choices=Patent_status)
    patent_filed_date = models.DateField()
    patent_published_date = models.DateField(blank=True,null=True)
    patent_granted_date = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.teacher_email_id.username +" : " + self.patent_title

# 4) consultancy model is used to collect info on all the consultancy of a particular teacher.
class consultancy(models.Model):

    Consultancy_status = [
        ('Ongoing','Ongoing'),
        ('Completed','Completed'),
        
    ]

    teacher_email_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='consultancies')
    name_of_consultancy = models.CharField(max_length=250)
    name_of_consultancy_project = models.CharField(max_length=250)
    sponsoring_agency = models.CharField(max_length=250)
    revenue_granted_date = models.DateField()
    revenue_generated = models.BigIntegerField()
    status_of_consultancy_work = models.CharField(max_length=100,choices=Consultancy_status)
    


    def __str__(self):
        return self.teacher_email_id.username +" : " + self.name_of_consultancy