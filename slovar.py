def update_dictionary(d, key, value):
    # put your python code here
    if key in d:
        d[key].append(value)
        #print('ключ есть')
    elif key is not d:
        #d[2*key]=[]
        if 2*key is d:
            d[2*key].append(value)
            #print('ключ 2*key уже есть')
        elif (2*key is not d) and d.get(2*key)==None:
            d[2*key]=[]
            d[2*key].append(value)
            #print('создание ключа и + новое значение списка')
        elif (2*key is not d) and d.get(2*key)!=None:
            d[2*key].append(value)
            #print('создание ключа и + значение списка')
    return


#Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь dd и два числа: keykey и valuevalue.

#Если ключ keykey есть в словаре dd, то добавьте значение valuevalue в список, который хранится по этому ключу.
#Если ключа keykey нет в словаре, то нужно добавить значение в список по ключу 2 * key2∗key. Если и ключа 2 * key2∗key нет, то нужно добавить ключ 2 * key2∗key в словарь и сопоставить ему список из переданного элемента [value][value].

#Требуется реализовать только эту функцию, кода вне неё не должно быть.
#Функция не должна вызывать внутри себя функции input и print.