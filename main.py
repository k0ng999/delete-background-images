import os
from rembg import remove

input_folder = 'IMG'
output_folder = 'OUTPUT_IMG'

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    input_path = os.path.join(input_folder, filename)

    if not os.path.isfile(input_path):
        continue

    with open(input_path, 'rb') as file:
        output_data = remove(file.read())

    # Формируем путь для сохранения файла с исходным расширением
    output_path = os.path.join(output_folder, filename)

    with open(output_path, 'wb') as output_file:
        output_file.write(output_data)

    print(f"Processed: {filename} -> {output_path}")
