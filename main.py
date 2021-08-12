import os

voice = os.listdir('content')

timer = 1
fol = 0
array = []

for i in range(len(voice)):
    path = os.listdir('content/' + voice[i])
    for j in range(len(path)):
        for f in range(len(voice)):
            if i != f:
                pathfile = os.listdir('content/' + voice[f])
                for g in range(len(pathfile)):
                    if timer == 1:
                        fol = path[j]
                        timer = 0
                    if fol != path[j]:
                        # расскоментируй 22 строку если хочешь увидеть проверямый файл в реалтайме,
                        # внимание на HDD вам наступит пизда так что не рекомендую
                        # print(fol)
                        fol = path[j]
                    if path[j] == pathfile[g]:
                        delete = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                              'content/' + voice[f] + '/' + pathfile[g])
                        os.remove(delete)
                        print('Дубликат удален', pathfile[g])
                        array.append(pathfile[g])
print('Список дубликатов:', '\n', '├──', '\n ├──'.join(array))