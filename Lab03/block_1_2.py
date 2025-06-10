'''Отсортировать строки текстового файла (input.txt) по убыванию их длины
(количеству символов). Записать результат выполнения в другой текстовый
файл (output.txt)'''

with open('input.txt', 'r', encoding='utf-8') as f_in:
    lines = f_in.readlines()

lines.sort(key=lambda line: len(line.rstrip('\n')), reverse=True)

with open('output.txt', 'w', encoding='utf-8') as f_out:
    f_out.writelines(lines)
