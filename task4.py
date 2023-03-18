# ✔ Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
#   Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
#   Достаточно вернуть один допустимый вариант.
# ✔ *Верните все возможные варианты комплектации рюкзака.

things_dict = {'спальник' : 3, 'стул' : 2, 'котелок' : 4, 'плитка' : 5, 'палатка' : 8, 'посуда' : 7, 'топор' : 2}
max_carrying = 20
weight = 0
backpack_list = []
for i in things_dict:
    if weight + things_dict[i] <= max_carrying:
        backpack_list.append(i)
        weight += things_dict[i]      
print(backpack_list)

# Задание со * не осилил даже на бумаге, если есть подсказка - было бы интересно.