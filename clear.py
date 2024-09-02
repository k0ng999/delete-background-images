import os
import shutil

def clear_folder(folder_path):
    if os.path.exists(folder_path):
        # Удаляем все файлы в папке
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)  # Удаляем файл или символическую ссылку
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)  # Удаляем директорию и её содержимое
            except Exception as e:
                print(f'Не удалось удалить {file_path}. Причина: {e}')

# Пути к папкам
input_folder = 'IMG'
output_folder = 'OUTPUT_IMG'

# Очистка папок
clear_folder(input_folder)
clear_folder(output_folder)
