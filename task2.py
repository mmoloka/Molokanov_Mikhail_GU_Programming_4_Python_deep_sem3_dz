# ✔ Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

input_list = [1, 1, 1, 3.14, 'hello', 'text', 3.14, 'text']
output_list = []

for i in set(input_list):
    if input_list.count(i) > 1:
        output_list.append(i)

print(output_list)
