import sys
from path import get_path
from creating_file import create_file, create_folder, write_file, \
    get_list, delete_file, copy_file, open_file, rename_file, change_folder, \
    move_file, archive, dearchive

#C:/Users/hrenz/Desktop
path = None
path = get_path()
root = path.count('/')
while True:
    #if path is None:
        #path = get_path()
    #root = path.count('/')
    print('Выберите действие. 0 - завершить работу, 1 - создать папку, 2 - удалить папку/файл, \n'
      '3 - создать файл, 4 - записать в файл, 5 - просмотр содержимого файла, \n'
          '6 - переименовать файл, 7 - перемещение между папками, 8 - скопировать файл, \n'
          '9 - переместить файл, 10 - архивировать файл или папку')
    action = int(input())
    if action == 0:
        break
    elif action == 1:
        create_folder(path)
    elif action == 2:
        delete_file(path)
    elif action == 3:
        create_file(path)
    elif action == 4:
        write_file(path)
    elif action == 5:
        open_file(path)
    elif action == 6:
        rename_file(path)
    elif action == 7:
        path = change_folder(root, path)
    elif action == 8:
        copy_file(path)
    elif action == 9:
        move_file(path)
    elif action == 10:
        archive(path)
    elif action == 11:
        dearchive(path)