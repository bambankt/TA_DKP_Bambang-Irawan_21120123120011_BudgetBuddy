import tkinter as tk
import tkinter.messagebox as mb

class BudgetBuddy:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Budget Buddy")
        self.window.geometry("320x420")
        self.window.resizable(width=0, height=0)
        self.window.configure(bg='#fbaed2')

        self.balance = 0
        self.income = 0
        self.expenses = 0
        self.starting_balance = 0
        self.final_balance = 0
        self.history = []
        self.update_count = 0
        self.create_widgets()

    def create_widgets(self):
        # Tampilan 
        label_font = ('Consolas', 11)
        entry_font = ('Consolas', 11)
        button_font = ('Consolas', 11)
        label_bg = '#fbaed2'
        entry_bg = '#ffffff'
        button_bg = '#87cefa'
        button_fg = '#000000'
        stop_fg = '#e0115f'
        info_label_bg = '#d7bfdc'

        # Membuat Frame Halaman 1 dan 2
        self.page1 = tk.Frame(self.window, bg=label_bg)
        self.page2 = tk.Frame(self.window, bg=label_bg)
        
        # Halaman 1
        tk.Label(self.page1, text="Masukkan Saldo Awal:", font=label_font, bg=info_label_bg).pack(pady=5)
        self.starting_balance_entry = tk.Entry(self.page1, font=entry_font, bg=entry_bg)
        self.starting_balance_entry.pack(pady=5)

        #tk.Label(self.page1, text="Saldo Awal:", font=label_font, bg=info_label_bg).pack(pady=5)
        #self.starting_balance_label = tk.Label(self.page1, text="Rp 0", font=label_font, bg=info_label_bg)
        #self.starting_balance_label.pack(pady=5)

        #tk.Label(self.page1, text="Saldo Akhir:", font=label_font, bg=info_label_bg).pack(pady=5)
        #self.final_balance_label = tk.Label(self.page1, text="Rp 0", font=label_font, bg=info_label_bg)
        #self.final_balance_label.pack(pady=5)

        tk.Label(self.page1, text="Pemasukan:", font=label_font, bg=info_label_bg).pack(pady=5)
        self.income_entry = tk.Entry(self.page1, font=entry_font, bg=entry_bg)
        self.income_entry.pack(pady=5)

        tk.Label(self.page1, text="Pengeluaran:", font=label_font, bg=info_label_bg).pack(pady=5)
        self.expenses_entry = tk.Entry(self.page1, font=entry_font, bg=entry_bg)
        self.expenses_entry.pack(pady=5)

        tk.Button(self.page1, text="Update", font=button_font, bg=button_bg, fg=button_fg, command=self.update_balance).pack(pady=10)
        tk.Button(self.page1, text="Lihat Riwayat", font=button_font, bg=button_bg, fg=button_fg, command=self.show_page2).pack(pady=10)
        tk.Button(self.page1, text="Berhenti", font=button_font, bg=stop_fg, fg=button_fg, command=self.window.quit).pack(pady=10)
        
        # Halaman 2
        self.history_label = tk.Label(self.page2, text="Riwayat Saldo:", font=label_font, bg=info_label_bg)
        self.history_label.pack(pady=5)

        self.history_text = tk.Text(self.page2, font=label_font, width=40, height=15, bg=entry_bg)
        self.history_text.pack(pady=5)
        self.history_text.tag_configure("bold", font=(label_font[0], label_font[1], 'bold'))

        tk.Button(self.page2, text="Kembali", font=button_font, bg=button_bg, fg=button_fg, command=self.show_page1).pack(pady=10)

        self.page1.pack()

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
            self.balance = (self.starting_balance + self.income) - self.expenses


            self.update_count += 1
            history_entry = (f"Update ke-{self.update_count}: "
                             f"Saldo Awal: Rp {self.format_number(self.starting_balance)}, "
                             f"Pemasukan: Rp {self.format_number(self.income)}, "
                             f"Pengeluaran: Rp {self.format_number(self.expenses)}, "
                             f"Saldo Akhir: Rp {self.format_number(self.balance)}")
            self.history.append(history_entry)

            self.update_history()

            if self.balance < 0:
                mb.showwarning("Peringatan", "Saldo bernilai minus, harap mengurangi pengeluaran anda")

            self.income_entry.delete(0, tk.END)
            self.expenses_entry.delete(0, tk.END)

        except ValueError as e:
            mb.showerror("Error", str(e))

    def format_number(self, num):
        return int(num) if num.is_integer() else num

    def update_history(self):
        self.history_text.delete(1.0, tk.END)
        for entry in self.history:
            self.history_text.insert(tk.END, entry + "\n\n")  
            start_idx = self.history_text.index(tk.END + "-3l")
            end_idx = self.history_text.index(tk.END + "-1l")
            self.history_text.tag_add("bold", start_idx, start_idx + "+10c")

    def show_page1(self):
        self.page2.pack_forget()
        self.page1.pack()

    def show_page2(self):
        self.page1.pack_forget()
        self.page2.pack()

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

       
       
