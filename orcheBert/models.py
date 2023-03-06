from django.db import models


class orcheBert(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title

class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    email = models.CharField(unique=True, max_length=191, blank=True, null=True)
    password = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'

    def __str__(self):
        return str(self.id)

class Humming_MIDI(models.Model):
    id = models.BigAutoField(primary_key=True)
    hummingFile_path = models.CharField(max_length=191, blank=True, null=True)
    midiFile_path = models.CharField(max_length=191, blank=True, null=True)
    owner = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.id)

class OrchestraMIDI(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    file_path = models.CharField(max_length=191, blank=True, null=True)
    owner = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    humming_midi = models.ForeignKey(Humming_MIDI, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.id)

class Favorite(models.Model):
    id = models.BigAutoField(primary_key=True)
    orchestraMIDI = models.ForeignKey(OrchestraMIDI, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.id)
