from django.db import models
from authentication.models import User
# Create your models here.


class Hackathon(models.Model):
    """A model representing a Hackathon"""
    title = models.CharField(default="No title provided",
                             max_length=100, unique=True)
    date = models.DateField(auto_now_add=False)
    time = models.TimeField(auto_now_add=False)
    image = models.CharField(null=True, blank=True, max_length=200)
    results_declared = models.BooleanField(default=False)
    max_team_size = models.IntegerField(default=10)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Team(models.Model):
    """A model representing a participating team."""
    name = models.CharField(blank=False, null=False, max_length=50)
    leader = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="teams_as_a_leader")
    hackathon = models.ForeignKey(
        Hackathon, on_delete=models.CASCADE, related_name="participating_teams")
    # to be decided for making unique team ids.
    team_id = models.CharField(blank=False, null=False, max_length=50)
    members = models.ManyToManyField(User, related_name="teams_as_a_member")

    def __str__(self):
        return self.name


class Link(models.Model):
    """A model to hold link for refrences and resources for a submission."""
    url = models.URLField(max_length=200)
    title = models.CharField(default="No title provided.", max_length=100)

    def __str__(self):
        return self.title


class Submission(models.Model):
    """ A model representing submission for a hackthon."""
    team = models.OneToOneField(Team, on_delete=models.CASCADE)
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    time = models.TimeField(auto_now=True)
    score = models.IntegerField()
    links = models.ManyToManyField(Link)
    description = models.TextField()

    def __str__(self):
        return f'{self.team.name}\'s Submission'
