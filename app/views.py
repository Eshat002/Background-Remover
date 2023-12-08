from django.http import JsonResponse
from rembg import remove
from django.core.files.base import ContentFile
from .models import Image
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def remove_bg(request):
    print(request.POST)
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        print("image",image)
        # Process the image using rembg
        image_data = image.read()
        processed_data = remove(image_data)
        processed_image = ContentFile(processed_data)

        # Save the processed image in the database
        instance = Image(original_image=image)
        instance.processed_image.save('processed_' + image.name, processed_image)

        # Return success response
        return JsonResponse({'status': 'success', 'processed_image': instance.processed_image.url})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request'})
