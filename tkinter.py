from tkinter import *


def btn_click_up():
    numbers_list = [88, 5, 7, 22, 54, 2, 11, 65, 4]
    numbers_list.sort()
    for i in range(len(numbers_list)):
        lbl_result = Label(text="Result")
        lbl_result.pack()
        lbl_result["text"] = str(numbers_list[i])


def btn_click_down():
    numbers_list = [88, 5, 7, 22, 54, 2, 11, 65, 4]
    numbers_list.sort(reverse=True)
    for i in range(len(numbers_list)):
        lbl_result = Label(text="Result")
        lbl_result.pack()
        lbl_result["text"] = str(numbers_list[i])



root = Tk()
root.title("Название")
root.geometry("200x630")
lbl_name = Label(text="Сортировка")
lbl_name.pack()


btn_change_label_sort_up=Button(text="По возрастанию", command=btn_click_up)
btn_change_label_sort_up.pack()

btn_change_label_sort_down=Button(text="По убыванию", command=btn_click_down)
btn_change_label_sort_down.pack()



root.mainloop()