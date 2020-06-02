from tkinter import *

window = Tk()
window.title("Word Counter")
window.geometry("400x300+300+250")

clicks = 0

def click_button():
    global clicks
    clicks += 1
    window.title("Clicks {}".format(clicks))

btn = Button(text="Load file",          # текст кнопки
             background="#D3D3D3",     # фоновый цвет кнопки
             foreground="#000000",     # цвет текста
             padx="20",             # отступ от границ до содержимого по горизонтали
             pady="10",              # отступ от границ до содержимого по вертикали
             font="16",              # высота шрифта
             command=click_button
             )
btn.place(relx=.5, rely=.5, anchor="c", height=30, width=130, bordermode=OUTSIDE)

input = StringVar()

input_word = Entry(textvariable=input)
input_word.place(relx=.5, rely=.1, anchor="c")

window.mainloop()