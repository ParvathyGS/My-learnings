from django.db import models

class TeamModel(models.Model):

	TeamName =  models.CharField(max_length=100)
	Player1 = models.CharField(max_length=100)
	Player2 = models.CharField(max_length=100)
	Player3 = models.CharField(max_length=100)
	Player4 = models.CharField(max_length=100)
	Player5 = models.CharField(max_length=100)
	Player6 = models.CharField(max_length=100)
	Player7 = models.CharField(max_length=100)
	Player8 = models.CharField(max_length=100)
	Player9 = models.CharField(max_length=100)
	Player10 = models.CharField(max_length=100)
	Player11 = models.CharField(max_length=100)
	Coach = models.CharField(max_length=100)
	Manager1 = models.CharField(max_length=100)
	Manager2 = models.CharField(max_length=100)

class Schedules(models.Model):

	TeamName1 =  models.CharField(max_length=100)
	Date = models.DateField()
	Time = models.DateTimeField()
	Venue = models.CharField(max_length=100)
	Goalscore = models.CharField(max_length=255)

# class Fixtures(models.Model):

# 	TeamName1 =  models.CharField(max_length=100)
# 	TeamName1 = models.CharField(max_length=100)
# 	Date = models.DateField()
# 	Time = models.DateTimeField()
# 	Venue = models.CharField(max_length=100)

	
