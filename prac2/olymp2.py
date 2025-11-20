def quicksort(arr):
    '''
    Функция быстрой сортировки массива.
    Получает на вход массив, возвращает отсортированный массив. 
    '''
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)


def check_winners(scores, student_score):
    '''
    Функция, что проверяет, находится ли человек в тройке победителей.
    Получает на вход массив с кол-ом очков и количество очков конкретного человека, печатает строку.
    '''
    scores = quicksort(scores)
    if student_score == scores[-1] or student_score == scores[-2] or student_score == scores[-3]:
        print("Вы в тройке победителей!")
    else:
        print("Вы не попали в тройку победителей.")


list_scores = list(map(int, input().split()))
score_of_stas = int(input())
check_winners(list_scores, score_of_stas)
