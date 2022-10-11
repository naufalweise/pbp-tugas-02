## Asinkronus vs Sinkronus Programming
Dalam async programming, beberapa task dapat bekerja dalam suatu saat. Ini bekerja dengan cara program tidak menunggu proses request, namun mengerjakan task yg lain. Bila hasil request sudah selesai, program baru akan kembali untuk menghandle request tersebut. Sehingga program tidak berjalan secara sekuensial, namun dapat melompat.

Dalam sync programming, hanya satu task yang dapat dikerjakaan dalam satu waktu. Program akan menunggu request sampai dibalas, baru melanjutkan tasknya. Program sinkronus berjalan secara sekuensial.


## Event driven programming
Dalam paradigma programming ini, alur program ditentukan atas terjadinya event. Dengan paradigma ini, kita bisa menulis kode yang akan merespon terhadap terjadinya suatu event. Contoh penerapannya dari tugas ini adalah saat mengeklik tombol add task, akan terbuka modal. Saat user mengeclick (event) tombol add task, melalui atribut onclick, akan dipanggil fungsi openTaskFormModal (event-handler) untuk membuka modal. 


## Penerapan Async Programming pada Ajax
Saat membuat request ajax, browser tidak menunggu request tersebut selesai. Oleh karena itu, browser masih bisa melakukan hal lainnya seperti merespons terhadap interaksi user layaknya page jika tidak melakukan request. Browser baru akan mengeksekusi handler dari respons ajax ketika request tersebut telah dibalas oleh server.

## Cara Implementasi
### AJAX GET TASK LIST
- Buat view untuk mendapatkan semua task list dalam json
- Buat view untuk menghandle request post untuk delete task dan toogle task status
- Sambungkan view tersebut ke urls.py
- Masukkan cdn jquery ke template base
- Tambahkan id ke container task yang akan digunakan di jquery
- Pindahkan html task list card ke fungsi baru renderTasklist yang memiliki parameter task. Gunakan jquery untuk merender task card.
- Buatlah fungsi fetchAndRenderTasklist yang memanggil ajax untuk mengambil data tasklist dari server. Kemudian saat respons sudah diterima, panggillah fungsi renderTasklist dengan argumen respons tersebut.
- Panggillah fungsi fetchAndRenderTasklist saat document ready

### AJAX CREATE TASK LIST
- Buat modelform untuk Task, gunakan form ini di view create task yang akan menyimpan task baru ke database
- Buatlah form di dalam modal di template. Buatlah tombol add task yang akan membuka modal ini.
- Tambahkan handler submit menggunakan atribut onsubmit ke fungsi untuk submit task.
- Pada fungsi submit task, lakukan POST dengan data dari form untuk membuat task baru.
- Panggil fungsi fetchAndRenderTasklist untuk merefresh tasklist yang ditampilkan.

### AJAX DELETE & TOGGLE STATUS
- Buatlah fungsi deleteTask dan toggleTask (parameternya id task) yang melakukan POST melalui ajax. Setelah menyelesaikan operasinya, panggil fungsi fetchAndRenderTasklist untuk merefresh tasklist yang ditampilkan.
- Sambungkan fungsi-fungsi tersebut ke tombol-tombol yang sesuai melalui atribut onclick.