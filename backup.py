import os
import time

source = [r'C:\\Users\Nikolay\Pictures']  # Файлы и каталоги которые необходимо скопировать, собираются в список

target_dir = 'D:\\Backup'  # Указываем путь хранения резервных копий

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'  # Файлы помещаются в zip-архив,
# имя будет текущая дата и время
if not os.path.exists(target_dir):  # Создать целевой катало если он отсутствует
    os.mkdir(target_dir)  # Создать каталог

# Используем команду 'zip' для помещения файлов в zip-фрхив
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

# Запускаем создание резервной копии
print('Zip команда')
print(zip_command)
print('Выполняется...')

if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')
