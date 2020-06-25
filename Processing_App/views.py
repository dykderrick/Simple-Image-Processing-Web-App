import os

from django.shortcuts import render

from Simple_Image_Processing_Web_App import settings
from .forms import ImageForm
from .models import UserUploadPhoto
from .processing_scripts import retrieve_image_info, padding, histogram_equalization, gray_scale, laplacian_derivative, smoothing, resize, rotate


def _get_form(request):
    if request.method == 'POST':  # user click confirm
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
    else:
        form = ImageForm()

    return {'form': form}


def _get_padded_image():
    img = UserUploadPhoto.objects.all().last()  # the last uploaded photo

    image_path = img.image.path
    image_name = os.path.splitext(image_path)[0].split("/")[-1]
    image_type = os.path.splitext(image_path)[-1]  # include "."  e.g. "IMG.jpeg" -> ".jpeg"

    is_saved, padded_image_url = padding.PaddedImage(image_path).save_processed_image()
    if is_saved:
        return {
            'last_image_path': image_path,
            'last_image_name': image_name,
            'last_image_type': image_type,
            'padded_image_url': padded_image_url
        }
    else:
        return None


def _get_image_info(image_path, is_gray_image=False):
    # current_img_path = _get_padded_image()['img'].image.path

    return retrieve_image_info.ImageInfo(image_path, is_gray_image).info_getter()


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
    image_info_context = _get_image_info(image_context['last_image_path'])

    # Merge dicts
    context = {**image_context, **form_context, **image_info_context}

    return render(request, 'Processing_App/index.html', context)


def _get_equalized_padded_image():
    padded_is_saved, padded_image_url = (False, None)  # init

    img = UserUploadPhoto.objects.all().last()  # the last uploaded photo

    image_path = img.image.path

    equalized_is_saved, equalized_save_path = histogram_equalization.HistogramEqualizeImage(image_path).save_processed_image()
    if equalized_is_saved:
        padded_is_saved, padded_image_url = padding.PaddedImage(equalized_save_path).save_processed_image()

    if padded_is_saved:
        return {
            'unpad_img_path': equalized_save_path,
            'padded_image_url': padded_image_url
        }
    else:
        return None


def equalized_image_index(request):
    # Construct the image uploading form
    form_context = _get_form(request)

    # Get equalized version of last upload image in context for rendering to the page
    image_context = _get_equalized_padded_image()

    # Get image info context to be inserted
    image_info_context = _get_image_info(image_context['unpad_img_path'], is_gray_image=True)

    # Merge dicts
    context = {**image_context, **form_context, **image_info_context}

    return render(request, 'Processing_App/index.html', context)


def _get_grayed_padded_image(gray_scale_value):
    padded_is_saved, padded_image_url = (False, None)  # init

    img = UserUploadPhoto.objects.all().last()  # the last uploaded photo

    image_path = img.image.path

    grayed_is_saved, grayed_save_path = gray_scale.GrayImage(image_path, gray_scale_value).save_processed_image()
    if grayed_is_saved:
        padded_is_saved, padded_image_url = padding.PaddedImage(grayed_save_path).save_processed_image()

    if padded_is_saved:
        return {
            'unpad_img_path': grayed_save_path,
            'padded_image_url': padded_image_url
        }
    else:
        return None


def grayed_image_index(request):
    # Construct the image uploading form
    form_context = _get_form(request)

    # Get grayed last upload image in context for rendering to the page
    image_context = _get_grayed_padded_image(request.GET.get('gray_input'))

    # Get image info context to be inserted
    image_info_context = _get_image_info(image_context['unpad_img_path'], is_gray_image=True)

    # Merge dicts
    context = {**image_context, **form_context, **image_info_context}

    return render(request, 'Processing_App/index.html', context)


def _get_laplacian_padded_image():
    padded_is_saved, padded_image_url = (False, None)  # init

    img = UserUploadPhoto.objects.all().last()  # the last uploaded photo

    image_path = img.image.path

    laplacian_is_saved, laplacian_save_path = laplacian_derivative.LaplacianImage(image_path).save_processed_image()
    if laplacian_is_saved:
        padded_is_saved, padded_image_url = padding.PaddedImage(laplacian_save_path).save_processed_image()

    if padded_is_saved:
        return {
            'unpad_img_path': laplacian_save_path,
            'padded_image_url': padded_image_url
        }
    else:
        return None


def laplacian_image_index(request):
    # Construct the image uploading form
    form_context = _get_form(request)

    # Get laplacian version of last upload image in context for rendering to the page
    image_context = _get_laplacian_padded_image()

    # Get image info context to be inserted
    image_info_context = _get_image_info(image_context['unpad_img_path'], is_gray_image=True)

    # Merge dicts
    context = {**image_context, **form_context, **image_info_context}

    return render(request, 'Processing_App/index.html', context)


def _get_smoothed_padded_image():
    padded_is_saved, padded_image_url = (False, None)  # init

    img = UserUploadPhoto.objects.all().last()  # the last uploaded photo

    image_path = img.image.path

    smoothed_is_saved, smoothed_save_path = smoothing.SmoothedImage(image_path).save_processed_image()
    if smoothed_is_saved:
        padded_is_saved, padded_image_url = padding.PaddedImage(smoothed_save_path).save_processed_image()

    if padded_is_saved:
        return {
            'unpad_img_path': smoothed_save_path,
            'padded_image_url': padded_image_url
        }
    else:
        return None


def smoothed_image_index(request):
    # Construct the image uploading form
    form_context = _get_form(request)

    # Get smoothed version of last upload image in context for rendering to the page
    image_context = _get_smoothed_padded_image()

    # Get image info context to be inserted
    image_info_context = _get_image_info(image_context['unpad_img_path'])

    # Merge dicts
    context = {**image_context, **form_context, **image_info_context}

    return render(request, 'Processing_App/index.html', context)


def _get_resized_padded_image(scale_percent):
    padded_is_saved, padded_image_url = (False, None)  # init

    img = UserUploadPhoto.objects.all().last()  # the last uploaded photo

    image_path = img.image.path

    resized_is_saved, resized_save_path = resize.ResizedImage(image_path, scale_percent).save_processed_image()
    if resized_is_saved:
        padded_is_saved, padded_image_url = padding.PaddedImage(resized_save_path).save_processed_image()

    if padded_is_saved:
        return {
            'unpad_img_path': resized_save_path,
            'padded_image_url': padded_image_url
        }
    else:
        return None


def resized_image_index(request, resize_input):
    # Construct the image uploading form
    form_context = _get_form(request)

    # Get resized version of last upload image in context for rendering to the page
    image_context = _get_resized_padded_image(resize_input)

    # Get image info context to be inserted
    image_info_context = _get_image_info(image_context['unpad_img_path'])

    # Merge dicts
    context = {**image_context, **form_context, **image_info_context}

    return render(request, 'Processing_App/index.html', context)


def _get_90rotated_padded_image(last_image_path, rotate_k):
    padded_is_saved, padded_image_url = (False, None)  # init

    rotated90_is_saved, rotated90_save_path = rotate.RotatedImage(last_image_path, rotate_k).save_processed_image()
    if rotated90_is_saved:
        padded_is_saved, padded_image_url = padding.PaddedImage(rotated90_save_path).save_processed_image()

    if padded_is_saved:
        image_name = os.path.splitext(rotated90_save_path)[0].split("/")[-1]
        image_type = os.path.splitext(rotated90_save_path)[-1]  # include "."  e.g. "IMG.jpeg" -> ".jpeg"
        return {
            'last_image_path': rotated90_save_path,
            'last_image_name': image_name,
            'last_image_type': image_type,
            'unpad_img_path': rotated90_save_path,
            'padded_image_url': padded_image_url
        }
    else:
        return None


def rotate90_image_index(request, last_image_name, last_image_type, rotate_type):
    if str(rotate_type) == 'left90':
        rotate_k = 1  # left rotate 90 degree
    else:
        rotate_k = 3  # left rotate 270 degree (right 90 degree)

    # Construct the image uploading form
    form_context = _get_form(request)

    last_image_path = settings.MEDIA_ROOT + '/user_upload_images/' + last_image_name + last_image_type

    image_context = _get_90rotated_padded_image(last_image_path, rotate_k)

    # Get image info context to be inserted
    image_info_context = _get_image_info(image_context['unpad_img_path'])

    # Merge dicts
    context = {**image_context, **form_context, **image_info_context}

    return render(request, 'Processing_App/index.html', context)
