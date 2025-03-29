# Приложение "Калькулятор расходов" с функцией сохранения списка при закрытии приложения
# и восстановления его при очередном запуске программы.



import tkinter as tk
from tkinter import messagebox

# Функция для добавления расхода
def add_expense():
    category = category_entry.get()
    amount = amount_entry.get()
    if category and amount:
        try:
            amount = float(amount)
            expense_listbox.insert(tk.END, f"{category}: {amount}")
            category_entry.delete(0, tk.END)
            amount_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Ошибка", "Сумма должна быть числом.")
    else:
        messagebox.showwarning("Внимание", "Заполните все поля.")

# Функция для удаления расхода
def delete_expense():
    selected = expense_listbox.curselection()
    if selected:
        expense_listbox.delete(selected)

# Функция для вычисления общей суммы
def calculate_total():
    total = 0
    for i in range(expense_listbox.size()):
        item = expense_listbox.get(i)
        amount = float(item.split(": ")[1])
        total += amount
    messagebox.showinfo("Общая сумма", f"Общая сумма расходов: {total:.2f} руб.")

# Функция для очистки всех данных
def clear_all():
    expense_listbox.delete(0, tk.END)

# Функция для сохранения данных в файл
def save_data():
    """Сохраняет данные из списка расходов в файл expenses.txt."""
    with open("expenses.txt", "w", encoding="utf-8") as file:
        for i in range(expense_listbox.size()):
            file.write(expense_listbox.get(i) + "\n")

# Функция для загрузки данных из файла
def load_data():
    """Загружает данные из файла expenses.txt в список расходов."""
    try:
        with open("expenses.txt", "r", encoding="utf-8") as file:
            for line in file:
                expense_listbox.insert(tk.END, line.strip())
    except FileNotFoundError:
        # Если файл не существует, просто пропускаем загрузку
        pass

# Создание главного окна
root = tk.Tk()
root.title("Калькулятор расходов")
root.configure(background="aquamarine")

# Элементы интерфейса
tk.Label(root, text="Категория:", bg="aquamarine").pack(pady=5)
category_entry = tk.Entry(root, width=30)
category_entry.pack(pady=5)

tk.Label(root, text="Сумма:", bg="aquamarine").pack(pady=5)
amount_entry = tk.Entry(root, width=30)
amount_entry.pack(pady=5)

add_button = tk.Button(root, text="Добавить расход", command=add_expense)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Удалить расход", command=delete_expense)
delete_button.pack(pady=5)

total_button = tk.Button(root, text="Показать общую сумму", command=calculate_total)
total_button.pack(pady=5)

clear_button = tk.Button(root, text="Очистить все данные", command=clear_all)
clear_button.pack(pady=5)

expense_listbox = tk.Listbox(root, height=10, width=50)
expense_listbox.pack(pady=10)

# Загрузка данных из файла при запуске программы
load_data()

# Привязываем функцию save_data к событию закрытия окна
root.protocol("WM_DELETE_WINDOW", lambda: (save_data(), root.destroy()))

# Запуск главного цикла
root.mainloop()