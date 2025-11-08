from django.shortcuts import render
import requests


def get_dog_breed():
    '''
    Функция для получения списка пород собак
    :return: список пород собак
    '''
    dog_breeds = [item for item in requests.get('https://dog.ceo/api/breeds/list/all').json()['message']]
    return dog_breeds

def get_breed_input(breed_str):
    '''
    Функция для преобразования строки в список пород собак
    :param breed_str: строка с породами собак
    :return: список пород собак
    '''
    return breed_str.split(', ')

# Create your views here.
def dog_images_list(request):
    '''
    Функция для рендера страницы с списком изображений собак
    '''
    show_breeds = get_dog_breed()
    for breed in range(len(show_breeds)):
        print(f'{breed + 1}. {show_breeds[breed]}')
    breed_list_to_show = get_breed_input(input())
    image_list = [requests.get(f'https://dog.ceo/api/breed/{breed}/images/random').json()['message'] for breed in breed_list_to_show]
    
    return render(request, 'show_dogs/show_dogs.html', {'image_list': image_list})