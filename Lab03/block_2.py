import os
import subprocess
import platform

def open_file(filename):
    try:
        subprocess.call(["xdg-open", filename])
    except Exception as e:
        print(f"Ошибка при открытии файла: {e}")

def show_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            print(f.read())
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")

def list_directory(path):
    if os.path.isdir(path):
        print(f"Содержимое директории '{path}':")
        for item in os.listdir(path):
            print("📁" if os.path.isdir(os.path.join(path, item)) else "📄", item)
    else:
        print("Директория не найдена.")

def create_file(path):
    try:
        with open(path, 'w', encoding='utf-8') as f:
            pass
        print(f"Файл создан: {path}")
    except Exception as e:
        print(f"Ошибка при создании файла: {e}")

def create_directory(path):
    try:
        os.makedirs(path)
        print(f"Папка создана: {path}")
    except Exception as e:
        print(f"Ошибка при создании папки: {e}")


print("Файловый менеджер. Введите команду (или 'exit' для выхода):")
while True:
    command = input("> ").strip()
    if not command:
        continue

    parts = command.split(maxsplit=1)
    cmd = parts[0]

    if cmd == "exit":
        break
    elif cmd == "open" and len(parts) == 2:
        open_file(parts[1])
    elif cmd == "show" and len(parts) == 2:
        show_file(parts[1])
    elif cmd == "list" and len(parts) == 2:
        list_directory(parts[1])
    elif cmd == "create_file" and len(parts) == 2:
        create_file(parts[1])
    elif cmd == "create_dir" and len(parts) == 2:
        create_directory(parts[1])
    else:
        print("Неизвестная или неполная команда. Поддержка: open, show, list, create_file, create_dir, exit.")