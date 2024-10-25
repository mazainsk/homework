import fitz
# Если нужный модуль отсутствует, нужно установить в терминале: pip install PyMuPDF

pdf_document = 'd:\\!_Docs\\Учеба\\Python\\Большая_книга_проектов_Python_Свейгарт_Эл_Z_Library.pdf'
output_file = 'd:\\!_Docs\\Учеба\\Python\\output.txt'
text = {}
with fitz.open(pdf_document) as doc:
    for num, page in enumerate(doc.pages(25, 420)):
        text[num] = page.get_text()
p_count = 0
prog_text = {0: {}}
for i in text.values():
    page_ = str(i).split('\n')
    last_key = 0
    for line_ in page_:
        dot_pos = line_.find('.')
        if 1 < dot_pos <= 3:
            if line_[dot_pos - 1].isdecimal():      # с большой вероятностью найденный фрагмент - строка кода программы
                key_= int(line_[:dot_pos])
                if key_ in prog_text[p_count]:      # номер строки найден
                    if last_key == key_:            # повтор предыдущего номера!
                        key_ += 1
                    else:
                        p_count += 1
                        prog_text.update({p_count: {}})
                prog_text[p_count].update({key_: line_[dot_pos + 2:]})
                last_key = key_

with open(output_file, 'w', encoding='utf-8') as file:
    for i in range(len(prog_text)):
        file.writelines('# ' + '=' * 68 + '\n' + '# PROGRAM ' + str(i + 1) + '\n' + '# ' + '=' * 68 + '\n' * 2)
        for j in prog_text[i].values():
            file.writelines(str(j) + '\n')
        file.writelines('\n' * 2)
