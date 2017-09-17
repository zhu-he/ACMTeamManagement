from django.db import models

class OJ(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Contest(models.Model):
    name = models.CharField(max_length=128)
    oj = models.ForeignKey(OJ)

    class Meta:
        unique_together = (("oj", "name"),)

    def __str__(self):
        return self.name


class Problem(models.Model):
    name = models.CharField(max_length=16)
    contest = models.ForeignKey(Contest)

    def __str__(self):
        return '%s %s' % (self.contest.name, self.name)


class RankItem(models.Model):
    rank = models.IntegerField()
    name = models.CharField(max_length=64)
    contest = models.ForeignKey(Contest)
    score_sum = models.CharField(max_length=16, blank=True)

    def __str__(self):
        return '%s %d %s' % (self.contest.name, self.rank, self.name)


class ScoreItem(models.Model):
    score = models.CharField(max_length=16, blank=True)
    rank_item = models.ForeignKey(RankItem)
    problem = models.ForeignKey(Problem)

    class Meta:
        unique_together = (("rank_item", "problem"),)

    def __str__(self):
        return '%s %d %s' % (self.rank_item.contest.name, self.rank_item.name, self.problem.name)


class Alias(models.Model):
    name = models.CharField(max_length=64)
    member = models.ForeignKey('base.Member')
    oj = models.ForeignKey(OJ)

    class Meta:
        unique_together = (("name", "oj"),)

    def __str__(self):
        return '%s %s %s' % (self.oj.name, self.member.name, self.name)

