from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .forms import ImageForm
from .models import UserUploadPhoto
from .processing_scripts import retrieve_image_info, padding


def index(request):
    # Little Trick here:
    # the form context getter should be invoked prior to
    # image context getter, because when the page tries to
    # post a form submission, images should be firstly saved
    # to database, and then the image (last upload one) will be
    # conveyed through image_context to the page.

    # Construct the image uploading form
    form_context = _get_form(request)

    # Get last upload image in context for rendering to the page
    image_context = _get_padded_image()

    # Get image info context to be inserted
    image_info_context = _get_image_info()

    # Merge dicts
    context = {**image_context, **form_context, **image_info_context}

    return render(request, 'Processing_App/index.html', context)


def _get_form(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
    else:
        form = ImageForm()

    return {'form': form}


def _get_padded_image():
    img = UserUploadPhoto.objects.all().last()  # the last uploaded photo

    image_path = img.image.path

    is_saved, padded_image_url = padding.ImagePadding(image_path, pad_w=700, pad_h=520).save_padded_image()
    if is_saved:
        return {'img': img,
                'padded_image_url': padded_image_url
                }
    else:
        return None


def _get_image_info():
    current_img_path = _get_padded_image()['img'].image.path

    return retrieve_image_info.ImageInfo(current_img_path).info_getter()