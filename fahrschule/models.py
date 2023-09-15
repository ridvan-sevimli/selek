from django.db import models


# Create your models here.

class Person(models.Model):
    created = models.DateTimeField("date created", null=True)
    lastName = models.CharField(max_length=200)
    firstName = models.CharField(max_length=200)
    street = models.CharField(max_length=200,null=True)
    plz = models.CharField(max_length=200,null=True)
    ort = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    phoneNumber = models.CharField(max_length=200,null=True)
    birthDate = models.DateTimeField(max_length=200,null=True)
    faberNumber = models.IntegerField(default=0,null=True)

    def __str__(self):
        return self.firstName + " " + self.lastName


class CourseCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Course(models.Model):
    courseCategory = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    startDate = models.DateTimeField(max_length=200)
    endDate = models.DateTimeField(max_length=200)
    quota = models.IntegerField(default=0)

    def __str__(self):
        return self.name + " " + str(self.quota)


class Registered(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    enlistedCourse = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.person.firstName + " " + self.person.lastName
