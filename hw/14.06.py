import hashlib
import tkinter as tk
from tkinter import messagebox

# глобальная область видимости
login_entry = None
password_entry = None

def admission():
    #локальная область видимости
    global login_entry, password_entry

    login = login_entry.get()
    password = password_entry.get()

    if login == "" or password == "":
        messagebox.showerror("Ошибка")
        return

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    with open('admission.txt', 'a') as file:
        file.write(f"{login} | {hashed_password}\n")

    messagebox.showinfo("Сохранено")

def interface():
    global login_entry, password_entry

    window = tk.Tk()

    #настройки окна
    window.title("Сохранение данных")
    window.geometry("300x150")


    login_label = tk.Label(window, text="Логин:")
    login_label.pack()

    login_entry = tk.Entry(window)
    login_entry.pack()

    password_label = tk.Label(window, text="Пароль:")
    password_label.pack()

    password_entry = tk.Entry(window, show="*")
    password_entry.pack()

    button = tk.Button(window, text="Сохранить", command=admission)
    button.pack()

    #отрисовка окна
    window.mainloop()

if __name__ == "__main__":
    interface()



