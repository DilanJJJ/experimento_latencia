from django.db import models

class ArchivoMedico(models.Model):
    archivo_id = models.IntegerField(unique=True)  # Solo guardamos el id del archivo
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Archivo {self.archivo_id} - {self.fecha_subida}"