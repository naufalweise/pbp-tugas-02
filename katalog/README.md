# LINKS
[Heroku Site](https://naufalweise-pbp-tugas-02.herokuapp.com/katalog/)


# Bagan Web Aplikasi Django
![Bagan Web Aplikasi Django](../PBP%20Tugas%2002%20Bagan%20Django.drawio.png)

# Virtual Environtment
Mengapa kita menggunakan virtual environtment dalam proyek django? Virtual environtment berfungsi untuk memisahkan library yang terinstal pada satu proyek dengan proyek lainnya. Dengan begitu, masalah seperti konflik versi library akan teratasi. Sebenarnya, aplikasi django dapat dijalankan tanpa virtual environtment, tetapi metode ini lebih baik dihindari. 



# Langkah-Langkah

## Setup aplikasi
Di `project_django/settings.py` tambahkan katalog di `INCLUDED_APPS`.
```
INSTALLED_APPS = [
    ...
    'katalog',
]
```

## Migrasi
Buatlah migrasi, untuk mencatat perubahan penambahan model katalog ke file migrasi.
```
python manage.py makemigrations
```
Jalankan migrasi untuk memperbarui database agar sesuai dengan file migrasi.
```
python manage.py migrate
```
Masukkan data json yang telah tersedia ke database.
```
python manage.py loaddata initial_catalog_data.json
```

## Tambahkan View
- Di `katalog/views.py` tambahkan fungsi index untuk menampilkan katalog.
- Di fungsi index, ambil data dari database, lalu teruskan data tersebut ke template `katalog.html`. Teruskan pula nama dan npm. 
```
STUDENT_NAME = "NAUFAL WEISE WIDYATAMA"
STUDENT_ID = "2106750263"

def index(request):
    catalog_items = CatalogItem.objects.all()
    context = {'catalog_items': catalog_items, 'student_name': STUDENT_NAME, 'student_id': STUDENT_ID}
    return render(request, 'katalog.html', context)
```
## Edit template
1. Edit `katalog.html` untuk menampilkan nama dan npm.
```
<h5>Name:</h5>
<p>{{student_name}}</p>

<h5>Student ID: </h5>
<p>{{student_id}}</p>
```
2. Tampilkan pula barang-barang di daftar katalog.
```
{% for item in catalog_items %}
    <tr>
        <td>{{item.item_name}}</td>
        <td>{{item.item_price}}</td>
        <td>{{item.item_stock}}</td>
        <td>{{item.rating}}</td>
        <td>{{item.description}}</td>
        <td>{{item.item_url}}</td>
    </tr>
{% endfor %}
```

## Tambahkan routing
- Di `project_django/urls.py` include `urls.py` milik katalog.
```
urlpatterns = [
    ...
    path('katalog/', include('katalog.urls'))
]
```
- Di `katalog/urls.py` tambahkan route ke view index katalog.
```
urlpatterns = [
    path('', index, name='index'),
]
```
## Deploy
Saya menggunakan github-cli dan heroku-cli agar lebih mudah melakukan deploy. Berikut adalah langkah-langkahnya:
1. Buat aplikasi di heroku.
```
heroku apps:create -a naufalweise-pbp-tugas-02
```
2. Masukkan api key heroku dan app name heroku ke github secret repo proyek ini.
```
cd repo_folder
gh secret set HEROKU_APP_NAME
gh secret set HEROKU_API_KEY
```
3. Push pekerjaan anda ke github.