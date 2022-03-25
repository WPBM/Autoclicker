import tkinter
import main


def clicked1():
    main.attack()
def clicked2():
    main.clantime(txt.get())
def clicked3():
    exit()

window = tkinter.Tk()
window.title("Автобои")
window.geometry("470x160")

startxt = tkinter.Label(window, text ='Вас приветствует автокликер для игры "Метро 2033".\n Для стабильной работы приложения, раскройте окно игры на полный экран.', font=("Arial Bold", 10))
startxt.grid(column=1, row=0)

starbtn = tkinter.Button(window, text="Начать", font=("Arial Bold", 10), command = clicked1)
starbtn.grid(column=1, row=1)

txt = tkinter.Entry(window, width=20)
txt.grid(column=1, row=3)

startime = tkinter.Button(window, text="Назначить время", font=("Arial Bold", 10), command = clicked2)
startime.grid(column=1, row=2)

starstop = tkinter.Button(window, text="Выйти", font=("Arial Bold", 10), command = clicked3)
starstop.grid(column=1, row=4)

window.mainloop()
