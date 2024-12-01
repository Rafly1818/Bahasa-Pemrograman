# Langkah-langkah Instalasi Python di WSL dan Setup di Visual Studio Code

Panduan ini akan membantu Anda menginstal Python di WSL (Windows Subsystem for Linux) dan menghubungkannya dengan Visual Studio Code (VS Code) untuk mengembangkan dan menjalankan program Python.

## 1. Setup Ubuntu di WSL
Langsung buka WSL Ubuntu dan ikuti langkah-langkah berikut:

1. **Update sistem paket**:  
   Setelah login ke terminal Ubuntu, jalankan:
   ```bash
   sudo apt update && sudo apt upgrade
   ```

2. **Instal Python**:  
   Untuk mengembangkan program Python di WSL, instal Python dengan perintah berikut:
   ```bash
   sudo apt install python3 python3-pip
   ```

3. **Verifikasi Instalasi**:  
   Pastikan Python terinstal dengan benar dengan menjalankan:
   ```bash
   python3 --version
   ```
Anda harus melihat informasi versi Python yang terinstal.



## 2. Instalasi Visual Studio Code

1. **Download dan Instal VS Code**:
   Jika Anda belum memiliki Visual Studio Code, unduh dan instal dari situs resmi [Visual Studio Code](https://code.visualstudio.com/).

2. **Instal Extension WSL di VS Code**:
   - Buka Visual Studio Code.
   - Buka **Extensions** dengan menekan `Ctrl + Shift + X`.
   - Cari extension **Remote - WSL** oleh Microsoft.
   - Klik **Install** untuk menginstal extension ini.

3. **Buka VS Code dengan WSL**:
   - Buka terminal WSL, kemudian navigasi ke folder proyek Anda:
      ```bash
      cd /path/to/your/project
      ```
   - Jalankan perintah berikut untuk membuka folder di VS Code:
      ```bash
      code .
      ```
   - VS Code akan terbuka dalam mode WSL.



## 3. Konfigurasi Visual Studio Code untuk C++

1. **Instal Extension Python**:
   - Buka **Extensions** di Visual Studio Code dengan menekan `Ctrl + Shift + X`.
   - Cari extension **Python** oleh Microsoft.
   - Klik **Install**.

2. **Instalasi Code Runner (Opsional)**:
   Code Runner memudahkan untuk menjalankan kode dengan cepat di VS Code.
   - Cari **Code Runner** di panel Extensions.
   - Klik **Install** untuk menginstalnya.

3. **Pilih Interpreter Python**:
   Setelah Python terinstal, Anda perlu memilih interpreter Python di VS Code.
   - Tekan `Ctrl + Shift + P`, ketik **Python**: **Select Interpreter**, lalu pilih interpreter Python yang diinstal di WSL (biasanya `/usr/bin/python3`).



## 4. Menjalankan Program C++

1. Kompilasi Manual melalui Terminal  
   Untuk menjalankan program secara manual melalui terminal, lakukan langkah-langkah berikut:
   - Buka terminal di Visual Studio Code atau WSL.
   - Navigasikan ke direktori proyek Anda jika belum berada di sana:
   ```bash
   cd /path/to/your/project
   ```
   - Jalankan program Python dengan perintah berikut:
   ```bash
   python3 nama_program.py
   ```

2. Menjalankan Program Menggunakan Code Runner (Opsional):  
   Jika Anda sudah menginstal **Code Runner**, Anda bisa menjalankan file Python dengan cepat:  
   - Buka file `.py` yang ingin dijalankan di VS Code.
   - Klik ikon Run di pojok kanan atas, atau tekan `Ctrl + Alt + N`.
   - Output akan muncul di bagian terminal VS Code.



## 5. Troubleshooting  
Jika Anda mengalami masalah saat menjalankan program Python, berikut beberapa langkah yang dapat membantu:

1. **Periksa Instalasi Python**:
    Pastikan Python sudah terinstal dengan benar dengan menjalankan:
    ```bash
    python3 --version
    ```
    Jika tidak melihat informasi versi Python, ulangi proses instalasi menggunakan perintah:
    ```bash
    sudo apt install python3 python3-pip
    ```

2. **Periksa Path Program**:  
    Pastikan Anda berada di direktori yang benar saat menjalankan perintah eksekusi Python. Gunakan perintah berikut untuk memverifikasi bahwa file `.py` Anda ada di direktori saat ini:
    ```bash
    ls
    ```

3. **Masalah dengan Interpreter VS Code**:  
    Jika terjadi masalah saat neniilih interpreter di VS Code :
    - Tekan `Ctrl + Shift + P`, lalu pilih `Python: Select Interpreter` dan pastikan Anda memilih Python versi WSL.
    - Restart VS Code setelah memilih interpreter untuk memastikan pengaturan ditetapkan.

4. **Error pada Terminal WSL**:  
    Jika ada pesan error di terminal saat menjalankan program:
    - **File tidak ditemukan**: Periksa kembali nama file atau path. Pastikan Anda berada di direktori yang benar.
    - **Permission denied**: Jika Anda tidak memiliki izin untuk menjalankan file, berikan izin dengan perintah:
    ```bash
    chmod +x nama_program.py
    ```

5. **Masalah dengan Code Runner**:  
    Jika Anda tidak dapat menjalankan program menggunakan Code Runner:
    - Pastikan Code Runner sudah terinstal dan aktif.
    - Coba restart VS Code setelah install extension.



## 6. Dokumentasi Tambahan
Jika Anda ingin mempelajari lebih lanjut tentang penggunaan Python di WSL atau bagaimana mengoptimalkan penggunaan VS Code untuk pengembangan, berikut beberapa dokumentasi yang berguna:

1. [Dokumentasi resmi WSL di Microsoft]()
2. [Dokumentasi Python]()
3. [Dokumentasi resmi Visual Studio Code]()
4. [Remote Development menggunakan VS Code]()

Dengan mengikuti langkah-langkah di atas, Anda seharusnya dapat memulai pengembangan Python di WSL menggunakan Visual Studio Code dengan lancar. Semoga panduan ini bermanfaat!

---

<h3 align="left">Socials</h3>
<p align="center"> 
  <a href="https://www.github.com/Rafly1818" target="_blank" rel="noreferrer"> 
    <picture> 
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/github-dark.svg" /> 
      <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/github.svg" /> 
      <img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/github.svg" width="32" height="32" alt="GitHub" /> 
    </picture> 
  </a> 
  <a href="http://www.instagram.com/flyyr_" target="_blank" rel="noreferrer"> 
    <picture> 
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/instagram-dark.svg" /> 
      <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/instagram.svg" /> 
      <img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/instagram.svg" width="32" height="32" alt="Instagram" /> 
    </picture> 
  </a>
</p>