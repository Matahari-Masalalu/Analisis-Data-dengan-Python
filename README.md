 # Laporan Proyek Analisis Data - Faishal Anwar Hasyim

## Analisis Data: Dataset Bike Sharing

## Domain Proyek
Proyek ini bertujuan untuk menganalisis data sewa sepeda menggunakan dataset bike sharing yang mencakup informasi mengenai waktu sewa, kondisi cuaca, dan karakteristik pengguna. Dengan meningkatnya popularitas penggunaan sepeda sebagai sarana transportasi, pemahaman tentang faktor-faktor yang mempengaruhi permintaan sepeda menjadi sangat penting. Analisis ini diharapkan dapat memberikan wawasan bagi penyedia layanan bike sharing untuk meningkatkan layanan dan memenuhi kebutuhan pengguna.

## Business Understanding

### Problem Statements

- Pernyataan Masalah: Bagaimana faktor-faktor seperti cuaca, musim, dan hari libur mempengaruhi permintaan sewa sepeda?

### Goals
- Jawaban pernyataan masalah: Menganalisis data untuk mengidentifikasi pola dan tren dalam permintaan sewa sepeda berdasarkan berbagai faktor.

### Solution Statement
- Penggunaan Analisis Data: Menggunakan teknik analisis data eksploratif untuk memahami hubungan antara variabel yang mempengaruhi permintaan sewa sepeda.
- Data Preparation: Proyek ini akan menggunakan teknik data preparation untuk meningkatkan kualitas data dan performa analisis, termasuk pembersihan data dan normalisasi.

## Data Understanding

Sumber/referensi: [Bike Sharing Dataset - Kaggle](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset/data)

Dataset yang digunakan pada proyek ini adalah dataset bike sharing yang berisi informasi historis tentang sewa sepeda. Dataset ini memiliki beberapa atribut yang mencakup waktu sewa, kondisi cuaca, dan karakteristik pengguna.

Variabel-variabel pada dataset adalah sebagai berikut:
- **instant**: Indeks tiap entri data.
- **dteday**: Tanggal saat data diambil.
- **season**: Musim (1: Musim Semi, 2: Musim Panas, 3: Musim Gugur, 4: Musim Dingin).
- **yr**: Tahun (0: 2011, 1: 2012).
- **mnth**: Bulan (1 hingga 12).
- **hr**: Jam (0 hingga 23).
- **holiday**: Apakah data diambil ketika hari libur atau tidak.
- **weekday**: Hari dalam seminggu saat data diambil.
- **workingday**: Hari kerja.
- **weathersit**: Kondisi cuaca.
  - 1: Cerah
  - 2: Kabut + Mendung
  - 3: Salju Ringan
  - 4: Hujan Lebat
- **temp**: Suhu yang dinormalisasi dalam derajat Celsius.
- **atemp**: Suhu perasaan yang dinormalisasi dalam derajat Celsius.
- **hum**: Kelembaban yang dinormalisasi.
- **windspeed**: Kecepatan angin yang dinormalisasi.
- **casual**: Jumlah pengguna kasual.
- **registered**: Jumlah pengguna terdaftar.
- **cnt**: Jumlah total sepeda yang disewakan.

## Data Preparation

Tahap **Data Preparation** adalah langkah penting dalam proses analisis data, di mana data yang telah dikumpulkan disiapkan untuk analisis lebih lanjut. Berikut adalah langkah-langkah yang dilakukan dalam tahap ini:

- Data dikumpulkan dari dua file CSV, yaitu `hour.csv` dan `day.csv`, yang berisi informasi tentang penyewaan sepeda per jam dan per hari. Data dibaca menggunakan pustaka Pandas dan dimasukkan ke dalam DataFrame.
- Data dibersihkan dengan memperbaiki tipe data untuk atribut dteday, yang awalnya bertipe object, menjadi datetime64. Ini dilakukan untuk memudahkan analisis waktu.
- Untuk memudahkan analisis dan visualisasi, beberapa kolom diubah menjadi nilai yang lebih deskriptif. Misalnya, nilai numerik untuk season, yr, holiday, dan weathersit diubah menjadi nama yang lebih mudah dipahami.

## Exploratory Data Analysis

### Total Volume Sewa Sepeda

Analisis jumlah total sewa sepeda berdasarkan Jam, Hari, Bulan, dan Tahun.

![Cuplikan layar 2024-12-19 222613](https://github.com/user-attachments/assets/26597435-ac39-4d00-b840-a76adaaeaf25)

Bisa dilihat bahwa angka permintaan sepeda mengalami penurunan mulai dari jam 00.00 hingga mencapai titik terendah di jam 04.00 dan mencapai puncak permintaan pada jam 17.00.

![Cuplikan layar 2024-12-19 222731](https://github.com/user-attachments/assets/026b4a1c-a671-4d13-94d9-d2b2f0754917)

Bisa dilihat bahwa hari tidak mempengaruhi pada angka permintaan sepeda secara signifikan

![Cuplikan layar 2024-12-19 222844](https://github.com/user-attachments/assets/6ab6dc1e-7e13-45b4-9fb5-ae564fc37aa0)

Bisa dilihat bahwa angka permintaan sepeda mengalami penurunan mulai dari bulan Agustus hingga mencapai titik terendah di bulan Januari

![Cuplikan layar 2024-12-19 222942](https://github.com/user-attachments/assets/3a89896f-e64a-48ee-a7bb-2eeeee96cf5e)

Bisa dilihat bahwa angka permintaan sepeda mengalami kenaikan drastis hingga 2 kali lipat dari tahun 2011 ke tahun 2012.


### Pengaruh Cuaca terhadap Permintaan Sepeda Per hari

![Cuplikan layar 2024-12-19 223317](https://github.com/user-attachments/assets/2211dd67-5aa1-4290-ab44-c99c4a3b0ed6)


Analisis menunjukkan bahwa rata-rata permintaan sepeda mengalami peningkatan yang signifikan pada hari-hari dengan cuaca cerah. Hal ini dapat dijelaskan oleh kenyataan bahwa cuaca yang baik, seperti sinar matahari dan suhu yang nyaman, mendorong orang untuk beraktivitas di luar ruangan. Ketika cuaca cerah, banyak individu merasa lebih termotivasi untuk menggunakan sepeda sebagai sarana transportasi atau rekreasi. Selain itu, kondisi cuaca yang baik juga meningkatkan pengalaman berkendara, menjadikannya lebih menyenangkan dan nyaman. Sebaliknya, pada hari-hari dengan cuaca buruk, seperti hujan atau suhu yang sangat dingin, permintaan sewa sepeda cenderung menurun. Hal ini menunjukkan bahwa penyedia layanan bike sharing perlu mempertimbangkan faktor cuaca dalam perencanaan dan pengelolaan armada sepeda mereka, serta dalam penawaran promosi untuk menarik pengguna saat cuaca baik.

### Tren Musiman dalam Penggunaan Sepeda

![Cuplikan layar 2024-12-19 223407](https://github.com/user-attachments/assets/3038f967-1722-48f3-b127-7cfb57e82d6d)


Dalam analisis musiman, ditemukan bahwa permintaan sepeda tidak menunjukkan pola yang signifikan berdasarkan musim. Meskipun ada kecenderungan untuk bersepeda lebih banyak pada musim tertentu, data menunjukkan bahwa variasi dalam permintaan sewa sepeda antara musim semi, panas, gugur, dan dingin tidak cukup mencolok untuk diidentifikasi sebagai pengaruh yang signifikan.


### Pengaruh Hari Libur

![Cuplikan layar 2024-12-19 223438](https://github.com/user-attachments/assets/fcf84e6c-e8cb-4e81-8b08-b0a823ce8d59)

Hasil analisis menunjukkan bahwa penggunaan sepeda cenderung lebih tinggi pada hari-hari yang bukan hari libur. Ini mungkin disebabkan oleh fakta bahwa pada hari kerja, banyak orang yang menggunakan sepeda sebagai sarana transportasi untuk pergi ke tempat kerja atau sekolah. Dalam konteks ini, sepeda menjadi pilihan yang efisien dan ramah lingkungan. Sebaliknya, pada hari libur, meskipun ada kemungkinan untuk bersepeda sebagai kegiatan rekreasi, banyak orang memilih untuk melakukan aktivitas lain, seperti berkumpul dengan keluarga atau berlibur, yang dapat mengurangi minat mereka untuk menyewa sepeda. Oleh karena itu, penyedia layanan sepeda dapat mempertimbangkan untuk menawarkan promosi khusus pada hari kerja atau mengembangkan program yang mendorong penggunaan sepeda selama hari libur, seperti acara komunitas atau perlombaan sepeda, untuk meningkatkan partisipasi.

### Perbandingan Penggunaan Sepeda oleh Pengguna Terdaftar dan Kasual

![Cuplikan layar 2024-12-20 161631](https://github.com/user-attachments/assets/9ad685c6-67c9-4296-9c21-dbcbc0ed58b3)

Dalam analisis perbandingan antara pengguna terdaftar dan pengguna kasual, ditemukan bahwa pengguna terdaftar lebih aktif dan konsisten dalam menyewa sepeda. Pengguna terdaftar, yang biasanya merupakan individu yang telah mendaftar untuk menggunakan layanan secara rutin, menunjukkan pola penggunaan yang lebih teratur dan terjadwal. Mereka cenderung menggunakan sepeda untuk perjalanan harian mereka, baik untuk bekerja, berolahraga, maupun aktivitas sehari-hari lainnya. Di sisi lain, pengguna kasual sering kali menggunakan sepeda secara sporadis, mungkin hanya saat mereka berlibur atau dalam situasi tertentu. Hal ini menunjukkan bahwa penyedia layanan sepeda perlu mengembangkan strategi yang berbeda untuk menarik kedua jenis pengguna ini. Misalnya, untuk pengguna terdaftar, mereka dapat menawarkan program loyalitas atau diskon untuk penyewaan jangka panjang, sementara untuk pengguna kasual, mereka bisa menawarkan paket promosi atau pengalaman unik yang mendorong mereka untuk mencoba layanan sepeda lebih sering.

# Dasbor Analisis Data Bike Sharing

![Cuplikan layar 2024-11-16 194130](https://github.com/user-attachments/assets/f60b6518-0257-4f79-b703-847a770b881e)


Ini adalah proyek analisis data sepeda menggunakan Python yang bisa diakses [di sini]([https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset](https://kvjm374ffckfuewbtpvjn2.streamlit.app/)) dengan dataset "Bike Sharing", yang dapat diakses [di sini](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset) di Kaggle. Proyek ini dilakukan dengan menggunakan Google Colab untuk analisis data dan Streamlit untuk membuat dashboard interaktif.

## Deskripsi Proyek

Proyek ini bertujuan untuk menganalisis data sepeda dan menyajikannya dalam bentuk dashboard interaktif. Analisis data mencakup beberapa aspek, antara lain dampak cuaca buruk terhadap permintaan sepeda, tren musiman penggunaan sepeda, dan pengaruh hari libur terhadap penggunaan sepeda.

## Struktur Folder

- `Streamlit`: Folder utama yang berisi file dashboard.py untuk menghasilkan dasboard Streamlit.
- `Dataset`: Folder berisi dataset yang digunakan untuk analisis.
- `Aset`: Folder berisi gambar dan aset lain yang digunakan di dasbor.

## Penggunaan

1. Instal semua dependensi dengan menjalankan perintah berikut: ```pip install pandas matplotlib seaborn streamlit```
2. Pastikan Anda memiliki kumpulan data "bike share" yang dapat diakses dari tautan yang disediakan dan simpan di folder `Dataset`.
3. Jalankan aplikasi dengan perintah berikut: ```streamlit run dashboard.py```
4. Aplikasi akan berjalan di browser Anda, dan Anda dapat mulai menjelajahi analisis data sepeda.

## Fitur Dasbor

- Analisis total penyewaan sepeda per tahun.
- Analisis dampak cuaca buruk terhadap permintaan sepeda.
- Analisis tren musiman penggunaan sepeda.
- Analisis dampak liburan terhadap penggunaan sepeda.

## Kesimpulan
Analisis data Bike Sharing mengungkapkan faktor-faktor kunci yang mempengaruhi permintaan sewa sepeda, termasuk cuaca, hari kerja, dan karakteristik pengguna. Cuaca cerah meningkatkan permintaan, sedangkan hari kerja mendorong penggunaan sepeda sebagai transportasi. Pengguna terdaftar menunjukkan pola penggunaan yang lebih konsisten dibandingkan pengguna kasual.

Temuan ini memberikan peluang bagi penyedia layanan untuk mengoptimalkan operasional, menyesuaikan armada sepeda sesuai permintaan, dan menawarkan program menarik bagi pengguna. Peningkatan layanan, seperti aplikasi mobile yang lebih baik, dapat meningkatkan kepuasan pengguna dan mendorong lebih banyak orang untuk memilih sepeda sebagai transportasi berkelanjutan.

## Referensi
1. Lakshmipathi N  - Kagle. Diakses pada 16 November 2024 dari (https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset/data)
2. Eslam Mohamed  - Kagle. Diakses pada 16 November 2024 dari (https://www.kaggle.com/code/eslammohamed100/bike-sharing-prediction)
