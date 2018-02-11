from tkinter import *
import pickle

WIDTH = 300
HEIGHT = 480
BG_COLOUR = 'white'
TEXT_COLOUR = 'white'
WARNING = 'red'

okno = Tk()
okno.title('Калькулятор амфа')
okno.resizable(False,False)
canvas = Canvas(okno, width=WIDTH, height=HEIGHT, bg = BG_COLOUR)
canvas.pack()



text = Label(okno, text = 'Приветствую, уважаемый наркоман!', bg = TEXT_COLOUR, font = 'arial 12')
text.place(x=15, y=15)

text2 = Label(okno, text = 'Сколько же амфетамина тебе купить?!', bg = TEXT_COLOUR, font = 'arial 11')
text2.place(x=16, y=37)

# окна ввода

text_age = Label(okno, text = 'Введи свой возраст:', bg = TEXT_COLOUR, font = 'arial 10')
text_age.place(x=10, y=70)
okno_age = Entry(okno, bd = 2, width = 4)
okno_age.place(x=150, y=70)

text_ves = Label(okno, text = 'Введи свой вес:', bg = TEXT_COLOUR, font = 'arial 10')
text_ves.place(x=10, y=100)
okno_ves = Entry(okno, bd = 2, width = 4)
okno_ves.place(x=150, y=100)

text_days = Label(okno, text = 'Сколько дней будешь юзать:', bg = TEXT_COLOUR, font = 'arial 10')
text_days.place(x=10, y=130)
okno_days = Entry(okno, bd = 2, width = 4)
okno_days.place(x=200, y=130)

# окна с галочками

check1=Checkbutton(okno, text='Есть толерантность', bg = TEXT_COLOUR, font = 'arial 10')
check1.place(relx = 0.09, rely = 0.33)

check2=Checkbutton(okno, text='Буду марафонить как сука!', bg = TEXT_COLOUR, font = 'arial 10')
check2.place(relx = 0.09, rely = 0.4)

check3=Checkbutton(okno, text='Хочу чтоб каждый раз в щи вообще!', bg = TEXT_COLOUR, font = 'arial 10')
check3.place(relx = 0.09, rely = 0.47)

# кнопка получения результата

button_enter = Button(okno, text = 'Получить результат', font = 'arial 12')
button_enter.bind('<Button-1>', lambda event: save(okno_age.get()))
button_enter.place(relx = 0.24, rely = 0.55)


# работа с вводом

def save(text_age):
    text_age_save = int(text_age)
    f = open('age.txt', 'wb')
    pickle.dump(text_age_save, f)
    if text_age_save < 16:
        too_small = Label(okno, text = 'Ты слишком мал, \nпиздуй в школу!', fg = WARNING, bg = BG_COLOUR, font = 'arial 21')
        too_small.place(relx = 0.1, rely = 0.7)
        print('Ты слишком мал, \nпиздуй в школу!')
    elif text_age_save == None:
        vvedi_age = Label(okno, text = 'Введи возраст, \nне еби мне мозг', fg = WARNING, bg = BG_COLOUR, font = 'arial 21')
        vvedi_age.place(relx = 0.1, rely = 0.7)
        print('Введи возраст')
    else:
        norm = Label(okno, text = 'Хватит на всех, \nебучий шакал!', fg = WARNING, bg = BG_COLOUR, font = 'arial 21')
        norm.place(relx = 0.13, rely = 0.7)
        print('Хорошо, ебашь')
        
    f.close()
    

'''def pizduk():
    if text_age < 18:'''
    

'''text.pack()
text_age.pack()
okno_age.pack()
text_ves.pack()
okno_ves.pack()
button_enter.pack()'''


okno.mainloop()


# root = tkinter.Tk()
# root.title("Balls")
# canvas = tkinter.Canvas(root, width=Width, height=Height, bg = Bg_colour)
# canvas.pack()
# canvas.bind('<Button-1>', mouse_click)
# canvas.bind('<Button-3>', mouse_click, '+')

# main()
# root.mainloop()