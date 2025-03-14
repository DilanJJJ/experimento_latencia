from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .utils import simular_procesamiento
from ingesta_datos.models import ArchivoMedico

@csrf_exempt
def procesar_archivo(request, archivo_id):
    try:
        archivo = ArchivoMedico.objects.get(id=archivo_id)
        resultado = simular_procesamiento(archivo.archivo)
        return JsonResponse({'resultado': resultado})
    except ArchivoMedico.DoesNotExist:
        return JsonResponse({'error': 'Archivo no encontrado'}, status=404)