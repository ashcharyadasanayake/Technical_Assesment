from django.db import models
from django.utils.translation import gettext_lazy as _

class student_1 (models.Model):
    school_name = models.CharField(_("School Name"), max_length=255)
   
    StudentID = models.CharField(_("Student ID"), max_length=255)
    
  
     
     
    
class student_2 (models.Model): 
    school_name = models.CharField(_("School Name"), max_length=255)
   
    StudentID = models.CharField(_("Student ID"), max_length=255)
    Firstname = models.CharField(_("First Name"), max_length=255)
    Lastname = models.CharField(_("Last Name"), max_length=255)
    
class student_3 (models.Model):
    
    StudentID = models.CharField(_("Student ID"), max_length=255)
    
    Answer = models.CharField(_("Answer"), max_length=255)
   
      
      
      
class student_4 (models.Model):
    school_name = models.CharField(_("School Name"), max_length=255)
    
    Subject = models.CharField(_("Subject"), max_length=255)
    
            
            
class student_5 (models.Model):
    school_name = models.CharField(_("School Name"), max_length=255)
    
    Class = models.CharField(_("Class"), max_length=255)
   
                  
class student_6 (models.Model):
    school_name = models.CharField(_("School Name"), max_length=255)
   
    Subject = models.CharField(_("Subject"), max_length=255)
    
    Creditcount = models.IntegerField(_("Credit Count"))
    Participantcount = models.IntegerField(_("Participant Count"))
    Awardistintion = models.CharField(_("Award Distinction"), max_length=255)
