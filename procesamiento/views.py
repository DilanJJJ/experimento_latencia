from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .utils import simular_procesamiento
from ingesta_datos.models import ArchivoMedico

@csrf_exempt
def procesar_archivo(request, archivo_id):
    try:
        # Buscar el archivo_id en la base de datos (ya no necesitamos el archivo físico)
        archivo = ArchivoMedico.objects.get(archivo_id=archivo_id)
        resultado = simular_procesamiento(archivo.archivo_id)  # Simulamos el procesamiento con el archivo_id
        return JsonResponse({'resultado': resultado})
    except ArchivoMedico.DoesNotExist:
        return JsonResponse({'error': 'Archivo no encontrado'}, status=404)