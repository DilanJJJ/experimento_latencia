from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt

from .models import ArchivoMedico


from django.http import JsonResponse

@csrf_exempt
def subir_archivo(request):
    if request.method == 'POST':

        nombre = request.POST.get('nombre')
        archivo_id = request.POST.get('archivo_id')
        identificacion = request.POST.get('identificacion')
        sexo = request.POST.get('sexo')
        eps = request.POST.get('eps')
        telefono = request.POST.get('telefono')
        fecha_reporte = request.POST.get('fecha_reporte')
        prueba_realizada = request.POST.get('prueba_realizada')
        resultado = request.POST.get('resultado')

        # Verificamos si todos los parámetros necesarios están presentes
        if not all([nombre, archivo_id, identificacion, sexo, eps, telefono, fecha_reporte, prueba_realizada, resultado]):
            return JsonResponse({'error': 'Faltan parámetros en la solicitud'}, status=400)

        # Simulamos el almacenamiento de estos parámetros (no se guardará en la base de datos real aquí, pero se pueden guardar si se necesita)
        # En este caso, solo regresamos los datos como respuesta para hacer la prueba
        return JsonResponse({
            'mensaje': 'Datos recibidos',
            'datos': {
                'nombre': nombre,
                'archivo_id': archivo_id,
                'identificacion': identificacion,
                'sexo': sexo,
                'eps': eps,
                'telefono': telefono,
                'fecha_reporte': fecha_reporte,
                'prueba_realizada': prueba_realizada,
                'resultado': resultado
            }
        })

    return JsonResponse({'error': 'Método no permitido'}, status=405)

