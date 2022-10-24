# функция для создания файла
import os
import shutil
import zipfile


# функция создания папки
def create_folder(path, name="Новая папка"):
    print("Введите название папки: \n")
    name = input()
    try:
        os.mkdir(str(path + '\\' + name))
    except FileExistsError:
        print('Папка с таким названием уже существует!')


# Удаление файла или папки
def delete_file(path, name=None):
    if name == None:
        print("Введите название файла или папки, коорую нужно удалить.")
        name = input()
    if os.path.isdir(str(path + '\\' + name)):
        os.rmdir(str(path + '\\' + name))  # delete folder
    else:
        os.remove(str(path + '\\' + name))  # delete file


# Создание пустого файла
def create_file(path):
    text = None
    print("Введите название файла: \n")
    name = input()
    with open(str(path + '\\' + name), 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


# Запись в файл
def write_file(path):
    print("Введите название файла: \n")
    name = input()
    print("Введите текст: \n")
    text = input()
    with open(str(path + '\\' + name), 'w', encoding='utf-8') as f:
        f.write(text)


# просмотр содержимого файла
def open_file(path):
    print("Введите название файла: \n")
    name = input()
    f = open(str(path + '\\' + name))
    for line in f:
        print(line)

# переименовать файл
def rename_file(path):
    print("Введите старое название файла: \n")
    name = input()
    print("Введите новое название файла: \n")
    new_name = input()
    os.rename(str(path + '\\' + name), str(path + '\\' + new_name))


# Перемещение между папками (в пределах рабочей папки) -
# заход в папку по имени, выход на уровень вверх
def change_folder(root, path):
    print("Выберите, 1 - войти в папку или 2 - подняться на уровень вверх: \n")
    a = int(input())
    if a == 1:
        print("Введите название папки: \n")
        name = input()
        path = str(path + '/' + name)
        return path
    elif a == 2:
        if path.count('/') > root:
            ind = path.rfind('/')
            path = path[:ind]
            return path
        else:
            print('Нельзя выходить за пределы корневой директории')
            return path


# Просмотр списка файлов и папок
def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


# Копирование файла
def copy_file(path):
    print("Введите путь до файла, который необходимо скопировать: \n")
    path = input()
    print("Введите путь до папки, куда необходимо скопировать файл: \n")
    new_path = input()
    shutil.copy(path, new_path)
    '''if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Папка с таким названием уже существует!')
    else:
        shutil.copy(name, new_name)'''

# Перемещение файлов
def move_file(path):
    print("Введите название файла, который необходимо переместить: \n")
    name = input()
    path_moving = str(path + '/' + name)
    print("Введите путь до папки, куда необходимо переместить файл: \n")
    new_path = input()
    shutil.copy(path_moving, new_path)
    delete_file(path, name)

# Архивация файла и папки
def archive(path):
    print("Введите название файла или папки, который необходимо архивировать: \n")
    name = input()
    path = str(path + '/' + name)
    shutil.make_archive(path, format='zip')


# Разaрхивация файла и папки
'''def dearchive(path):
    print("Введите название файла или папки, который необходимо разархивировать: \n")
    name = input()
    path = str(path + '/' + name)
    shutil.unpack_archive(path)'''

def dearchive(path):
    print("Введите название файла или папки, который необходимо разархивировать: \n")
    name = input()
    path_name = str(path + '/' + name)
    if os.path.isdir(path_name):
        zipfile.ZipFile(path_name).extractall(path).close()
    else:
        zipfile.ZipFile(path_name).extract(name, path).close()

