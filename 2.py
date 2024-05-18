  #Сложная сдача
task = 'Сложная сдача'
print(task)
name = 'товар: черешня'
print(name)
price = float (34)  #цена 1 кг черешни
weight = float (4.5)  #вес купленных ягод
amount = float (500)  #количество денег у покупателя
change = (amount - (price * weight))  #change = сдача
name = 'сдача (руб)'
print(name)
print(change)
print(   )

  #Сдача всем
task = 'Сдача всем'
goods = 'любой товар'
price = int (44)  #цена 1 кг товара
weight = float (7.8)  #вес купленного товара
amount = int (1000)  #количество денег у покупателя
change = int(amount - (price * weight))  #change = сдача
name = 'сдача (руб)'
print(task)
print(goods)
print(name)
print(change)
print(   )

  #Работаем с выводом данных
task = 'Работаем с выводом данных'
goods = 'Апельсины'
price = int (44)  #цена 1 кг товара
w_n = 'вес (кг)'
weight = float(7.8)  #вес купленного товара
amount = int (1000)  #количество денег у покупателя
change = int(amount - (price * weight))  #change = сдача
name = 'сдача (руб)'
print(task)
print('Чек ' + '<' + (goods)+'>')
print(w_n)
print(weight)
print('Цена (руб/кг)')
print(price)
print('Итого (руб):')
print(int(price*weight))
print('Внесено (руб):')
print(amount)
print('Сдача (руб):')
print(change)
print(   )

    #Самая простая задача на свете
task = 'Самая простая задача на свете'
print(task)
sentence = 'Купи конструктор! '
print(sentence*8)
print(   )

  #Автоматизируем простоту!
task = 'Автоматизируем простоту!'
naturalNumber = 4
hobby = '"Любимое дело" '
writing = 'Обожаю писать '
print(task)
print((writing + hobby) * naturalNumber)