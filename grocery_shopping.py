# Task 2.1
"""
Используя список, прописать алгоритм покупки сметаны и дессерта к чаю.

Список продуктов от тёти Глаши, для Василия:

1. Сметану жирности 15%, но не Простоквашино.
2. Что-нибудь к чаю.

"""
import time

from engine_functions import (buy_something_for_tea, buy_sour_cream,
                              find_store_department)


# A function to find and buy sour cream and
# something for tea.
def buy_some_food():
    print('')
    time.sleep(1)
    product_name1 = 'Сметана'
    product_name2 = 'Что нибудь к чаю'
    need_fat_percentage = 15
    need_brand_name = 'Простоквашино'
    print('Здравствуйте, у нас намечается небольшой шопинг)')
    print('')
    time.sleep(1)
    print('Необходимо купить в магазине два пункта из списка:')
    print('')
    time.sleep(1)
    print(f'1. {product_name1} жирностью {need_fat_percentage}% '
          f'( НЕ "{need_brand_name}"! )')
    print('')
    time.sleep(1)
    print(f'2. {product_name2}.')
    print('')
    time.sleep(3)
    print('------------------------')
    print('')
    time.sleep(3)
    print('Если вы уже в магазине и готовы начать покупки,')
    print('')
    time.sleep(1)
    print('введите слово - "да",')
    print('')
    time.sleep(1)
    print('если не готовы - слово "нет".')
    ready_to_shop = (input('=> ')).lower()
    if ready_to_shop == 'да':
        print('')
        time.sleep(1)
        find_store_department(product_name1)
        buy_sour_cream(need_fat_percentage, need_brand_name)
        print('')
        time.sleep(3)
        print(f'Теперь второй пункт нашего '
              f'списка - {product_name2}')
        print('')
        time.sleep(1)
        print('Рекомендую выпечку или сладости)')
        print('')
        time.sleep(1)
        find_store_department(product_name2)
        buy_something_for_tea()
    elif ready_to_shop == 'нет':
        print('')
        time.sleep(1)
        print('Тогда начнём, когда будете готовы(')
        print('')
        time.sleep(1)
        exit()
    else:
        print('')
        time.sleep(1)
        print('Слова "да" или "нет" записаны не правильно.')
        print('')
        time.sleep(1)
        print('Повторите пожалуйста ввод.')
        time.sleep(1)
        buy_some_food()


buy_some_food()
