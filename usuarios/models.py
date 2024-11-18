from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)
    clave = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'Django'  # Aquí cambiamos el nombre de la tabla a 'Django'

    def __str__(self):
        return self.nombre