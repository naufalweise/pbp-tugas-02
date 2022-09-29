
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