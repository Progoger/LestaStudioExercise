def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        smaller = [i for i in arr[1:] if i <= pivot]
        larger = [i for i in arr[1:] if i > pivot]
        return quick_sort(smaller)+[arr[0]]+quick_sort(larger)


"""
Во-первых, быстрая сортировка прекрасно подходит по названию)
Во-вторых, при лучшем и среднем случае скорость выполнения O(nlogn), 
единственной проблемой является худший случай - O(n*n).
Можно было бы сделать сортировкой деревом, у которой везде O(nlogn), но при расчёте скорости О большое не учитываются
константы и по сути в лучшем и среднем случае быстрая сортировка отработает быстрее( прошу прощения за тафтологию), чем
сортировка деревом.
"""
