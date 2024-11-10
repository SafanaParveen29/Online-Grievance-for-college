from django.db import models

class Student(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    RollNo = models.CharField(max_length=10, unique=True)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50, blank=True) 
    PhoneNumber = models.CharField(max_length=10)
    studentEmail = models.EmailField()
    studentPassword = models.CharField(max_length=50)
    ConfirmPassword = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return self.RollNo

class staff(models.Model):
    staffId = models.CharField(max_length=10)
    sName = models.CharField(max_length=50)
    Designation = models.CharField(max_length=50)
    Department = models.CharField(max_length=50)
    Email = models.EmailField()
    Number = models.CharField(max_length=10)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.sName

class CollegeGrievance(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
        ('Closed', 'Closed'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    IssueType = models.CharField(max_length=50)
    Location = models.CharField(max_length=50, blank=True,null=True)
    Issue = models.TextField()
    Impact = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending') 

class HostelGrievance(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
        ('Closed', 'Closed'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    IssueType = models.CharField(max_length=50)
    RoomNumber = models.CharField(max_length=10)
    Issue = models.TextField()
    Impact = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending') 

class Counseling(models.Model):
    CATEGORY_CHOICES = [
        ('Academic', 'Academic Counseling'),
        ('Emotional', 'Emotional Support'),
        ('Career', 'Career Guidance'),
        ('Other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
        ('Closed', 'Closed'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Other')   
    Problem = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending') 
    def __str__(self):
        return self.category

class Certificate(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Issued', 'Issued'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    certificate_type =  models.CharField(max_length=30)
    Purpose = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')










