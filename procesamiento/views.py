from django.http import JsonResponse
from .utils import simular_procesamiento
from ingesta_datos.models import ArchivoMedico

def procesar_archivo(request, archivo_id):
    try:
        archivo = ArchivoMedico.objects.get(id=archivo_id)
        resultado = simular_procesamiento(archivo.archivo)
        return JsonResponse({'resultado': resultado})
    except ArchivoMedico.DoesNotExist:
        return JsonResponse({'error': 'Archivo no encontrado'}, status=404)