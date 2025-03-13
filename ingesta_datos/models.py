from django.db import models

class ArchivoMedico(models.Model):
    archivo = models.URLField()  # Usamos URLField para almacenar la ubicación del archivo
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Archivo {self.id} - {self.fecha_subida}"