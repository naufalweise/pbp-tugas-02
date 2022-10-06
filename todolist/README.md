
# Link
Heroku <https://naufalweise-pbp-tugas-02.herokuapp.com/todolist>

# CSRF Token
CSRF token berfungsi untuk menghindari serangan CSRF. Cross Site Requst Forgeries adalah attack yang membuat user melakukan aksi yang tak diinginkan dalam suatu website. Attack yang memanfaatkan privilage user yang sudah terautentikasi ini, terjadi ketika user membuka link malicious yang membuat user mengirim request pada website tanpa sepengetahuan user.

CSRF token adalah kode yang digenerate oleh django dan disisipkan di field hidden di form POST. Token ini unik antar user dan antar tiap request form. Saat django menerima form post, django akan memvalidasi token yang dikirim beserta form tersebut. Token ini menjamin bahwa form yang disent ke django adalah form yang dibuat oleh django itu sendiri, bukan yang dibuat attacker.

Tanpa CSRF Token, site kita tidak terproteksi dari serangan CSRF. Attacker bisa saja membuat form yang dapat melakukan aksi malicious ke website kita.

# Membuat Form Tanpa Generator
Membuat form bisa saja secara manual, tak harus menggunakan generator. Caranya dengan menggunakan atribut-atribut pada form. Di dalam object form, terdapat atribut tiap field, di dalam objek tiap field, terdapat atribut-atribut form seperti input element, error message, label, dan lain-lain.
Berikut contohnya: 
```html
<div class="form-field">
    <label for="{{ form.title.id_for_label}}">Title</label>
    {{ form.title }}
    <div class="error">{{ form.title.errors }}</div>
</div>
```

# Alur Data
Alur data dalam create-task:
- User mengisi form dengan field title & description
- User melakukan submisi. Data form dikirim dalam request POST ke web aplikasi django.
- Django melakukan validasi data form. Jika data tak lolos validasi, django akan mengirimkan response berisi error message ke user. Jika lolos, django melakukan cleaning data form, data diubah menjadi object python yang sesuai.
- Django memangil model Task untuk menyimpan data dari form ke database.
- Django mengirimkan response redirect ke halaman task list
- User akan mendapat laman task list dengan task yang baru ditambahkan

# Step - step
- Buat aplikasi dengan menggunakan `python manage.py startapp todolist`
- Tambahkan aplikasi tersebut ke included apps di setting project
- Buatlah urls di aplikasi, include url aplikasi ke url project
- Buatlah model Task, setelah itu lakukan makemigrations dan migrate.
- Buatlah kelas form TaskForm yang merupakan model form dari Task.
- Buatlah view register, login dan logout beserta templatenya
- Buatlah view index untuk melihat todolist user, dan create-task untuk membuat task. Buat juga templatenya.
- Tambahkan routing view-view yang sudah dibuat ke urls.py aplikasi.
- Untuk membuat data dummy, registrer dua user yang berbeda. Di tiap user, buat tiga task. Setelah itu, lakukan dumpdata, dan ekstrak record user & task ke json file. Taruh json file ini kedalam fixture.

# User
user dan pass ada di [sini](./user.txt)

# Tugas 5

## Perbedaan Inline, Internal, External Style

### Inline CSS
Style inline berada pada atribut suatu elemen html.
#### Kelebihan
- Lebih cepat untuk ditulis. Cocok untuk quickfix. Tak perlu mencari file css nya.
- Disupport aplikasi pembuka email. Terkadang aplikasi email memblock penggunaan external css untuk menghindari spam.
### Kelemahan
- Style yang panjang menjadi sulit dibaca oleh programmer, dan lebih susah di mantain.
- Tidak bisa di reuse
- Meningkatkan size page html

### Internal CSS
Syle pada internal css berada pada elemen style pada suatu page html.

#### Kelebihan
- Lebih clean, karena terpisah antara style dan elemen html.
- Bisa di reuse antar elemen, tapi hanya untuk satu page.
#### Kelemahan
- Tidak bisa di reuse untuk page yang lain
- Meningkatkan size page html

### External CSS
Style pada external css berada pada file terpisah dari html
#### Kelebihan
- Paling clean, karena file styling terpisah dari file html.
- Dapat direuse antar page html
- Dapat dicache 
#### Kelemahan
- Style tidak terapply ke page sampai file external css terload sepenuhnya.


## Tag HTML
1. h1, h2, h3, ...:
Heading, digunakan untuk menulis judul.
2. button:
Tombol, digunakan untuk membuat tombol yang bisa diklik dan merespons dengan sesuatu.
3. input:
Elemen input, digunakan untuk membuat text field. Text field biasanya digunakan di dalam form.
4. label
Elemen label, digunakan untuk memberi keterangan pada text field.
5. form: digunakan untuk membuat form yang berisi beberapa field. Form dapat mengirim data-data dari field tersebut ke server.

## Cara implementasi checklist
1. Membaca dokumentasi bootstrap
2. Taruh Link file bootstrap ke base template
3. Pastikan tiap page sudah extend ke base template
4. Tambahkan kelas bootstrap pada elemen yang ingin di style
5. buat external file css, link ke page yang diinginkan. Tambahkan additonal css agar page lebih cantik jika bootstrap masih belum cukup.