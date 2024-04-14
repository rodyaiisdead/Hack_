from tkinter import *
from PIL import *

def but_check():
    print("Кнопка рабочая")
#----------------------------------------------------------------------

#Переход в меню, описание меню
def m_window():
    global root
    main_window = Toplevel(root)
    main_window.title("Режим Киоска")
    
    main_window.geometry("1400x743+55-61")
    main_window.resizable(False, False)

    #------------------------------------------------------------------
    
    main_window.image = PhotoImage(file = 'Bg/back_main.png')
    bg_frame = Frame(main_window)
    bg_frame.pack(fill = BOTH, expand = YES)
    
    bg_lable = Label(bg_frame, image = main_window.image)
    bg_lable.place(x=0, y = 0, relwidth =1, relheight = 1)
    
    #------------------------------------------------------------------
    
    #Кнопка Пользователи
    but_users_active = Button(main_window, text = "Пользователи", command = but_check, font = ('Times New Roman', 13))
    but_users_active.config(width = 53 , height = 5)
    but_users_active.place(x = 0, y = 0)
    
    #------------------------------------------------------------------

    #Кнопка История действий
    but_users_active = Button(main_window, text = "История действий", command = but_check, font = ('Times New Roman', 13))
    but_users_active.config(width = 53 , height = 5)
    but_users_active.place(x = 0, y = 108)
    
    #------------------------------------------------------------------

    #Кнопка Настройки
    but_users_active = Button(main_window, text = "Настройки", command = but_check, font = ('Times New Roman', 13))
    but_users_active.config(width = 53 , height = 5)
    but_users_active.place(x = 0, y = 216)
    
    #------------------------------------------------------------------

    #Кнопка_заглушка
    but_users_active = Button(main_window)
    but_users_active.config(width = 68 , height = 70)
    but_users_active.place(x = 0, y = 324)
    
#----------------------------------------------------------------------

root = Tk()

#Вызов окна первого меню
root.overrideredirect(True)
root.geometry("900x640+310+50")
root.resizable(False, False)

#---------------------------------------------------------------------

#Шапка
title_ = Frame(root, bg='#333333', relief='raised', bd=2)
title_.pack(expand=1, fill=X)
#Шапка. Кнопка закрыть
close_ = Button(title_, text='X', command = root.destroy)
close_.pack(side=RIGHT)

#----------------------------------------------------------------------

#Ввод изображения
user_icon = PhotoImage(file="Bg/user_icon.png")
label_image = Label(root, image=user_icon)
label_image.pack(pady=10)

#----------------------------------------------------------------------

#Ввод пароля и логина

#Поле ввода
entry_username = Entry(root, font=('Times New Roman', 16))
entry_password = Entry(root, font=('Times New Roman', 16), show="*")

entry_username.place(x = 336, y = 340)
entry_password.place(x = 336, y = 427)

#Надписи над формой
label_username = Label(root, text="Логин", font=("Times New Roman",18))
label_password = Label(root, text="Пароль", font=("Times New Roman",18))
label_username.place(x = 419, y = 300)
label_password.place(x = 410, y = 390)

#Кнопка входа
button_login = Button(root, text="Войти",font=("Times New Roman",11), command = m_window)
button_login.place(x = 420, y = 465)

#----------------------------------------------------------------------

root.mainloop
