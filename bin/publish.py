from tkinter import messagebox as mb
def upload(file_name: str, dirfile: str):
    rsp_file = open(dirfile, "r", encoding='utf-8')
    raspis = rsp_file.read()
    rsp_file.close()

    html_file = open(f"uploaded/{file_name}.htm", "w", encoding='utf-8')
    html_file.write(raspis.replace("<отмена>", "<s><font color='red'>").replace("</отмена>", "</font></s>").replace("<будет>", "").replace("</будет>", "").replace("<замена>", "<font color='red'>").replace("</замена>", "</font>").replace("<учитель>", "(").replace("</учитель>", ")").replace("<кодировка>", "<meta charset='utf-8'>").replace("<след_урок>", "<br>").replace("<время>", "<font color='blue'>").replace("</время>", "</font>").replace("<номер>", "").replace("</номер>", "").replace("<класс>", "<font color='gray' size='5'>").replace("</класс>", "</font>").replace("<доп_урок>", "<font style='background-color:#f97778;'").replace("</доп_урок>", "</font>").replace("<шрифт", "<font").replace("</шрифт>", "</font>").replace("<день_недели>", "<h4>").replace("</день_недели>", "</h4>").replace("<группа>", "<font color='blue'>").replace("</группа>", "</font>").replace("<пусто>", "<h4><font color='gray'>Нет уроков</font></h4>").replace("<кабинет>", "<font>(").replace("</кабинет>", ")</font>").\
    replace("<нет_урока>", "<font color='gray'>Нет урока</font>").replace("<подсказка", "<abbr").replace("</подсказка>", "</abbr>"))
    html_file.close()
    mb.showinfo("Опубликовано", "Ваше расписание сохранено в .htm файле! Его можно открыть в браузере")