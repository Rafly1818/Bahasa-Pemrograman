import tkinter as tk
from tkinter import ttk

class HotelRaflesiaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel RAFLESIA")
        self.root.geometry("500x600")
        self.root.configure(bg="#ffffff")

        # Data harga kamar
        self.kamar_dict = {
            "Melati": 650000,
            "Sakura": 550000,
            "Lily": 400000,
            "Anggrek": 350000
        }

        self.create_widgets()

    def create_widgets(self):
        # Title
        title_label = ttk.Label(self.root, text="Hotel \"RAFLESIA\"", font=("Arial", 14, "bold"), background="#ffffff")
        title_label.pack(pady=10)

        # Frame untuk input
        frame_input = ttk.Frame(self.root, padding="10", style='TFrame')
        frame_input.pack(padx=10, pady=10, fill=tk.X)

        # Nama Petugas
        ttk.Label(frame_input, text="Input Nama Petugas:", background="#ffffff").grid(row=0, column=0, sticky="w", pady=2)
        self.entry_nama_petugas = ttk.Entry(frame_input, width=30)
        self.entry_nama_petugas.grid(row=0, column=1, pady=2)

        # Nama Customer
        ttk.Label(frame_input, text="Input Nama Customer:", background="#ffffff").grid(row=1, column=0, sticky="w", pady=2)
        self.entry_nama_customer = ttk.Entry(frame_input, width=30)
        self.entry_nama_customer.grid(row=1, column=1, pady=2)

        # Tanggal Check-in
        ttk.Label(frame_input, text="Input tanggal check in:", background="#ffffff").grid(row=2, column=0, sticky="w", pady=2)
        self.entry_tanggal_checkin = ttk.Entry(frame_input, width=30)
        self.entry_tanggal_checkin.grid(row=2, column=1, pady=2)

        # Garis
        ttk.Separator(frame_input, orient="horizontal").grid(row=3, columnspan=2, sticky="ew", pady=10)

        # Pilih Tipe Kamar
        ttk.Label(frame_input, text="Pilih Tipe Kamar:", background="#ffffff").grid(row=4, column=0, sticky="w", pady=2)
        self.combobox_kode_kamar = ttk.Combobox(frame_input, values=list(self.kamar_dict.keys()), width=27)
        self.combobox_kode_kamar.grid(row=4, column=1, pady=2)

        # Lama Sewa
        ttk.Label(frame_input, text="Input Lama Sewa:", background="#ffffff").grid(row=5, column=0, sticky="w", pady=2)
        self.entry_lama_sewa = ttk.Entry(frame_input, width=30)
        self.entry_lama_sewa.grid(row=5, column=1, pady=2)

        # Display price list
        ttk.Label(frame_input, text="Daftar Harga Kamar:", background="#ffffff", font=("Arial", 10, "bold")).grid(row=6, column=0, sticky="w", pady=2)

        price_list_frame = ttk.Frame(frame_input, relief="solid", padding="10")
        price_list_frame.grid(row=6, column=1, pady=2)

        price_list_text = "\n".join([f"{k}: Rp {v:,.0f}" for k, v in self.kamar_dict.items()])
        price_list_label = tk.Label(price_list_frame, text=price_list_text, font=("Arial", 10), bg="#ffffff", justify="left")
        price_list_label.pack()

        # Tombol Proses
        btn_proses = ttk.Button(self.root, text="Proses", command=self.proses)
        btn_proses.pack(pady=20)

        # Frame untuk output
        frame_output = ttk.Frame(self.root, padding="10", style='TFrame')
        frame_output.pack(padx=10, pady=10, fill=tk.X)

        self.text_output = tk.Text(frame_output, height=15, width=55, bg="#f8f8f8", fg="#000000", font=("Arial", 10))
        self.text_output.grid(row=0, column=0, padx=5, pady=5)
        self.text_output.config(state=tk.DISABLED)

    def proses(self):
        # Dapatkan nilai dari semua input
        nama_petugas = self.entry_nama_petugas.get()
        nama_customer = self.entry_nama_customer.get()
        tanggal_checkin = self.entry_tanggal_checkin.get()
        tipe_kamar = self.combobox_kode_kamar.get()
        lama_sewa = self.entry_lama_sewa.get()

        # Validasi input
        if not (nama_petugas and nama_customer and tanggal_checkin and tipe_kamar and lama_sewa):
            self.show_message("Semua bidang harus diisi!")
            return

        if tipe_kamar not in self.kamar_dict:
            self.show_message("Tipe kamar tidak valid! Pilih dari menu.")
            return

        try:
            lama_sewa = int(lama_sewa)
            if lama_sewa <= 0:
                raise ValueError
        except ValueError:
            self.show_message("Lama sewa harus berupa angka positif.")
            return

        # Menghitung biaya
        harga_per_malam = self.kamar_dict[tipe_kamar]
        jumlah_bayar = harga_per_malam * lama_sewa

        # Menghitung diskon
        if lama_sewa > 5:
            diskon = 0.10 * jumlah_bayar
        elif lama_sewa > 3:
            diskon = 0.05 * jumlah_bayar
        else:
            diskon = 0

        total_bayar = jumlah_bayar - diskon

        # Tampilkan hasil
        self.text_output.config(state=tk.NORMAL)
        self.text_output.delete("1.0", tk.END)

        hasil_text = (
            f"Bukti Pemesanan Kamar\n"
            f"Hotel \"RAFLESIA\"\n"
            f"=====================\n"
            f"Nama Petugas: {nama_petugas}\n"
            f"Nama Customer: {nama_customer}\n"
            f"Tanggal Check-in: {tanggal_checkin}\n"
            f"=====================\n"
            f"Tipe Kamar yang dipesan: {tipe_kamar}\n"
            f"Harga Sewa per malam: Rp {harga_per_malam:,.0f}\n"
            f"Lama Sewa: {lama_sewa} malam\n"
            f"Diskon: Rp {diskon:,.0f}\n"
            f"Jumlah Bayar: Rp {jumlah_bayar:,.0f}\n"
            f"Total Bayar: Rp {total_bayar:,.0f}\n"
            f"=====================\n"
        )

        self.text_output.insert(tk.END, hasil_text)
        self.text_output.config(state=tk.DISABLED)

    def show_message(self, message):
        self.text_output.config(state=tk.NORMAL)
        self.text_output.delete("1.0", tk.END)
        self.text_output.insert(tk.END, message)
        self.text_output.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = HotelRaflesiaApp(root)
    root.mainloop()