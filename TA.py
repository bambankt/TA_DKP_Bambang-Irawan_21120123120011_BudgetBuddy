import tkinter as tk
import tkinter.messagebox as mb

class BudgetBuddy:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Budget Buddy")
        self.create_widgets()
        self.window.geometry("320x420")
        self.window.resizable(width = 0, height = 0)

        self.balance = 0
        self.income = 0
        self.expenses = 0
        self.starting_balance = 0
        self.final_balance = 0
        self.balance_label = tk.Label(self.window)
        self.balance_label.pack()

    def create_widgets(self):
        tk.Label(self.window, text="Masukkan Saldo Awal:").pack()
        self.starting_balance_entry = tk.Entry(self.window)
        self.starting_balance_entry.pack()

        tk.Label(self.window, text="Saldo Awal:").pack()
        self.starting_balance_label = tk.Label(self.window, text="Rp 0")
        self.starting_balance_label.pack()

        tk.Label(self.window, text="Saldo Akhir:").pack()
        self.final_balance_label = tk.Label(self.window, text="Rp 0")
        self.final_balance_label.pack()

        tk.Label(self.window, text="Pemasukan:").pack()
        self.income_entry = tk.Entry(self.window)
        self.income_entry.pack()

        tk.Label(self.window, text="Pengeluaran:").pack()
        self.expenses_entry = tk.Entry(self.window)
        self.expenses_entry.pack()

        tk.Button(self.window, text="Update", command=self.update_balance).pack()

        tk.Button(self.window, text="Berhenti", command=self.window.quit).pack()

    def update_balance(self):
        try:
            self.starting_balance = float(self.starting_balance_entry.get())
            income = float(self.income_entry.get())
            expenses = float(self.expenses_entry.get())

            if income < 0:
                raise ValueError("Pemasukan tidak boleh negatif")

            if expenses < 0:
                raise ValueError("Pengeluaran tidak boleh negatif")

            self.income += income
            self.expenses += expenses
            self.balance = ( self.starting_balance + self.income ) - self.expenses
            #self.balance_label.config(text="Rp {self.balance}")
            self.starting_balance_label.config(text=f"Rp {self.starting_balance}")
            self.final_balance_label.config(text=f"Rp {self.balance}")

            if self.balance < self.balance * 0.1:
                mb.showwarning("Peringatan", "Saldo bernilai minus, harap mengurangi pengeluaran anda")

            self.income_entry.delete(0, tk.END)
            self.expenses_entry.delete(0, tk.END)

        except ValueError as e:
            mb.showerror("Error", str(e))

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = BudgetBuddy()
    while True:
        app.run()
        if mb.askyesno("Budget Buddy", "Apakah anda ingin melanjutkan?"):
            continue
        else:
            break
       