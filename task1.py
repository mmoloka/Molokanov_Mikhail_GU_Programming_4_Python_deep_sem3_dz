# ✔ Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

number_of_friends = 3                        # Иван : рюкзак спальник спички компас
my_dict = {}                                 # Саша : рюкзак нож компас спальник
my_set = set()                               # Леша : стул котелок рюкзак спальник
unique_set = set()  
count = 1                                

for i in range(number_of_friends):
    name = input('Введите имя друга: ')
    things = tuple(input('Ведите через пробел вещи, которые он взял в поход: ').split())
    
    my_dict[name] = things
    things_set = set(things)
    common_set = my_set.intersection(things_set)
    unique_set = unique_set.union(things_set).difference(common_set)

    my_set = things_set

my_set = set()
for i in my_dict:
    things_set = set(my_dict[i])
    not_common_set = my_set.intersection(things_set).difference(common_set)
    if not_common_set != set():
        count += 1
        exept_one = not_common_set
    else:
        name = i  

    my_set = things_set      
 

print(my_dict)
print(f'У всех есть: {common_set}')
print(f'Уникальные вещи (только у одного): {unique_set}')
if number_of_friends - count == 1:
    print(f'У двух друзей есть {exept_one}, имя, у которого нет - {name}')


 


    
