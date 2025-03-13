from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from .models import ArchivoMedico


def subir_archivo(request):
    if request.method == 'POST':
        archivo = request.FILES.get('archivo')
        if not archivo:
            return JsonResponse({'error': 'No se recibió archivo'}, status=400)

        # Guardamos el archivo usando Django FileSystemStorage (sin modelos si no es necesario)
        fs = FileSystemStorage()
        archivo_guardado = fs.save(archivo.name, archivo)
        archivo_url = fs.url(archivo_guardado)

        # Puedes almacenar la URL del archivo si es necesario
        nuevo_archivo = ArchivoMedico.objects.create(archivo=archivo_url)

        return JsonResponse({'mensaje': 'Archivo recibido', 'archivo_id': nuevo_archivo.id})
    return JsonResponse({'error': 'Método no permitido'}, status=405)


