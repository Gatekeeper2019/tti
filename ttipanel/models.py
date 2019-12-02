from django.db import models
from django_countries.fields import CountryField
from phone_field import PhoneField

# Create your models here.


class Paulapplication(models.Model):
    STATE_CHOICES =(("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))
    DISTRICT_CHOICES =(("Nicobar", "Nicobar"),("North Middle Andaman", "North Middle Andaman"),("South Andaman", "South Andaman"),("Anantapur","Anantapur"),("Chittoor", "Chittoor"),("East Godavari","East Godavari"))
    title_choice =(("Paul","Paul"), ("Timothy","Timothy"))
    ID_CHOICES= (("Aadhaar", "Aadhaar"),("Driving license","Driving license") )
    Marriage_CHOICES = (("Married", "Married"),("Unmarried","Unmarried") )
    Spouse_CHOICES = (("True", "Yes"),("False","No"), ("NA","NA")  )
    Physical_CHOICES = (("Good", "Good"),("Poor","Poor") )
    Education_CHOICES = (("Regular", "Regular"),("correspondence","correspondence") )
    theological_CHOICES = (("Regular", "Regular"),("correspondence","correspondence"), ("NA","NA") )
    email_CHOICES = (("True", "Yes"),("False","No") )
    internet_CHOICES = (("True", "Yes"),("False","No") )
    training_CHOICES = (("True", "Yes"),("False","No") )
    church_CHOICES = (("True", "Yes"),("False","No") )
    ordain_CHOICES = (("True", "Yes"),("False","No") )
    timothy_CHOICES = (("True", "Yes"),("False","No") )

    id = models.AutoField(primary_key=True)
    date_joined = models.DateField()
    title = models.CharField(max_length=100,  choices=title_choice)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    profile_pic = models.ImageField(upload_to ='media/profile_pic/', null=True, blank=True)
    summary = models.TextField(blank=True)
    country_of_Citizenship = CountryField(blank_label='(select country)')
    state = models.CharField(max_length=200,   choices = STATE_CHOICES)
    district = models.CharField(max_length=200,   choices = DISTRICT_CHOICES)
    pin_code = models.IntegerField()
    ID_Proof = models.CharField(max_length=200, choices = ID_CHOICES)
    Attach_ID_Proof = models.FileField(upload_to ='media/Attach_ID_Proof/', null=True, blank=True)
    Marital_Status = models.CharField(max_length=200,   choices = Marriage_CHOICES)
    Name_of_Spouse = models.CharField(max_length=100, null=True, blank=True)
    Years_of_Marriage = models.IntegerField()
    Is_Spouse_Christian = models.CharField(max_length=200,   choices = Spouse_CHOICES)
    No_of_Children = models.IntegerField()
    General_Physical_Health =  models.CharField(max_length=200, choices = Physical_CHOICES)
    If_Poor_please_explain  = models.TextField(blank=True)
    education_qualification_training = models.CharField(max_length=200,  choices = Education_CHOICES)
    theological_qualification = models.CharField(max_length=200, choices = theological_CHOICES)
    Name_of_the_college_Seminary = models.CharField(max_length=100, null=True, blank=True)
    Place = models.CharField(max_length=100, null=True, blank=True)
    year = models.IntegerField()
    Do_you_use_email = models.CharField(max_length=200,  choices = email_CHOICES)
    Do_you_have_regular_access_to_internet = models.CharField(max_length=200,  choices = internet_CHOICES)
    in_what_language_do_you_like_to_run_the_TTI_training = models.CharField(max_length=100, null=True, blank=True)
    are_you_already_engaged_in_any_other_training_program = models.CharField(max_length=200,  choices = training_CHOICES)
    If_yes_please_explain  = models.TextField(blank=True)
    are_you_involved_in_any_church_and_or_ministry_activity = models.CharField(max_length=200,  choices = church_CHOICES)
    If_yes_please_explain  = models.TextField(blank=True)
    are_you_ordained_or_licensed_pastor = models.CharField(max_length=200, choices = ordain_CHOICES)
    by_whom = models.CharField(max_length=100, null=True, blank=True)
    disqualification_based_on_1Timothy3_1_to_7_and_Titus_1_6_to_9 = models.CharField(max_length=200,choices = timothy_CHOICES)
    If_yes_please_explain  = models.TextField(blank=True)
    Church_or_Denominational_Membership = models.CharField(max_length=100, null=True, blank=True)
    Name_of_the_church = models.CharField(max_length=100, null=True, blank=True)
    Denomination = models.CharField(max_length=100, null=True, blank=True)
    Head_of_your_denomination_Mentor_name = models.CharField(max_length=100, null=True, blank=True)
    Briefly_describe_your_Salvation_experience = models.TextField(blank=True)
    Mention_the_languages_you_speak_Read_Write = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.first_name



class Timothyapplication(models.Model):
    STATE_CHOICES =(("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))
    DISTRICT_CHOICES =(("Nicobar", "Nicobar"),("North Middle Andaman", "North Middle Andaman"),("South Andaman", "South Andaman"),("Anantapur","Anantapur"),("Chittoor", "Chittoor"),("East Godavari","East Godavari"))
    timothy_CHOICES = (("True", "Yes"),("False","No") )
    title_choice =(("Paul","Paul"), ("Timothy","Timothy"))
    id = models.AutoField(primary_key=True)
    date_joined = models.DateField()
    title = models.CharField(max_length=100,  choices=title_choice)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    profile_pic = models.ImageField(upload_to ='media/profile_pic/', null=True, blank=True)
    country_of_Citizenship = CountryField(blank_label='(select country)')
    state = models.CharField(max_length=200,   choices = STATE_CHOICES)
    district = models.CharField(max_length=200,   choices = DISTRICT_CHOICES)
    pin_code = models.IntegerField()
    Mention_the_languages_you_speak_Read_Write = models.CharField(max_length=100, null=True, blank=True)
    Name_of_the_local_church = models.CharField(max_length=100, null=True, blank=True)
    do_have_approval_of_your_Pastor_to_join_TTI_training = models.CharField(max_length=200,choices = timothy_CHOICES)
    have_you_received_Jesus_Christ_as_your_Saviour_and_Lord = models.CharField(max_length=200,choices = timothy_CHOICES)
    Is_your_family_in_agreement_with_this_application = models.CharField(max_length=200,choices = timothy_CHOICES)
    do_you_understand_you_must_plant_church_before_graduation = models.CharField(max_length=200,choices = timothy_CHOICES)
    are_you_committed_to_also_training_others_to_plant_Churches= models.CharField(max_length=200,choices = timothy_CHOICES)

    def __str__(self):
        return self.first_name

#References
#Name
#Relationship
#Address
#City
#State
#Phone number
#Email


class Quarterly_Church_Planting_Update_Form(models.Model):
    DISTRICT_CHOICES =(("Nicobar", "Nicobar"),("North Middle Andaman", "North Middle Andaman"),("South Andaman", "South Andaman"),("Anantapur","Anantapur"),("Chittoor", "Chittoor"),("East Godavari","East Godavari"))
    timothy_CHOICES = (("True", "Yes"),("False","No") )
    id = models.AutoField(primary_key=True)
    Country = CountryField(blank_label='(select country)')
    National_Regional_Director_Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=255, unique=False,default='', verbose_name='Email')
    Mobile_Numbers =  PhoneField(blank=True, default='', help_text='Contact phone number')
    DATE_OF_REPORTING = models.DateField()
    Paul_Name = models.CharField(max_length=100, null=True, blank=True)
    District = models.CharField(max_length=200,   choices = DISTRICT_CHOICES)
    Mobile_Number =  PhoneField(blank=True, default='', help_text='Contact phone number')
    Current_Book = models.CharField(max_length=100, null=True, blank=True)
    Number_of_Timothys = models.IntegerField()
    First_Generation_Church_Plants_Timothy = models.IntegerField()
    Number_of_Titus = models.IntegerField()
    Second_Generation_Church_Plants_Titus_disciple = models.IntegerField()
    Third_Generation_Church_Plants_Titus_disciple  = models.IntegerField()
    No_of_new_believers = models.IntegerField()
    Any_Previous_batch_churches_planted = models.CharField(max_length=200,choices = timothy_CHOICES)
    Orphans_Being_Impacted = models.IntegerField()
    Baptisms = models.IntegerField()
    Widows_Being_Impacted = models.IntegerField()

    def __str__(self):
        return self.National_Regional_Director_Name
