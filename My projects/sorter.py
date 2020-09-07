#Данная программа сортирует все файлы из папки "Загрузки".
#Нам потребуется библиотека watchdog



# Подключаем все модули
from watchdog.observers import Observer
import os
import time
# FileSystemEventHandler - это класс по отслеживанию изменений
from watchdog.events import FileSystemEventHandler


# Создаем класс-наследник, через него можно отслеживать изменения в папках
class Handler(FileSystemEventHandler):
    # При любых изменениях в папке, мы перемещаем файлы в ней
    def on_modified(self, event):
        # Перебираем все файлы в папке folder_track
        for filename in os.listdir(folder_track):
            # Проверяем расширение файла
            extension = filename.split(".")
            # Если это фотография,
            if len(extension) > 1 and (extension[1].lower() == "jpg" or extension[1].lower() == "png" or extension[1].lower() == "svg"):
                # Перемещаем в папку с фотками
                file = folder_track + "/" + filename
                new_path = folder_dest + "/Photos/" + filename
                os.rename(file, new_path)
            # Если файл видео, то в папку с видео
            # Такое же можно прописать и для других расширений файлов, например, музыки
            elif len(extension) > 1 and extension[1].lower() == "mp4":
                file = folder_track + "/" + filename
                new_path = folder_dest + "/Videos/" + filename
                os.rename(file, new_path)


# Отслеживаемая папка, в данном случае прописываем путь к "загрузкам"
folder_track = '/путь к Downloads'
# Папка для перемещения
folder_dest = '/путь к папке, где будут храниться фото, видео или текстовые файлы'

# Запуск всего на отслеживание
handle = Handler()
observer = Observer()
observer.schedule(handle, folder_track, recursive=True)
observer.start()

# Программа будет срабатывать каждые 50 милисекунд 
try:
    while(True):
        time.sleep(50)
except KeyboardInterrupt:
    observer.stop()

observer.join()