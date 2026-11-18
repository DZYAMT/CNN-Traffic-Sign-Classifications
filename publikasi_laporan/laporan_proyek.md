# LAPORAN PROYEK
# CNN-Based Traffic Sign Classification

## 1. Pendahuluan

Pengenalan rambu lalu lintas merupakan salah satu penerapan teknologi pengolahan citra dan kecerdasan buatan. Proyek ini bertujuan mengembangkan sistem klasifikasi rambu lalu lintas menggunakan metode Convolutional Neural Network (CNN).

## 2. Tujuan

1. Mengembangkan model CNN untuk klasifikasi rambu lalu lintas.
2. Melakukan preprocessing citra berukuran 32 × 32 piksel.
3. Mengimplementasikan dasar algoritma klasifikasi menggunakan Python.
4. Mempelajari implementasi CNN menggunakan Verilog HDL sebagai pengembangan menuju FPGA.

## 3. Dataset

Dataset yang digunakan merupakan dataset gambar rambu lalu lintas dengan empat kelas:

- STOP
- NO ENTRY
- GIVE WAY
- TURN LEFT

Citra digunakan dengan ukuran 32 × 32 piksel sebagai masukan sistem klasifikasi.

## 4. Metodologi

Tahapan pengerjaan proyek:

1. Mengumpulkan dan menyiapkan dataset.
2. Melakukan preprocessing gambar.
3. Melatih model menggunakan Convolutional Neural Network.
4. Menyimpan model hasil pelatihan.
5. Mengembangkan implementasi dasar menggunakan Verilog HDL.
6. Merencanakan pengujian melalui simulasi digital.

## 5. Implementasi

Pengembangan algoritma Python menggunakan Google Colab dan TensorFlow/Keras.

Model yang dihasilkan disimpan dalam format Keras dan TensorFlow Lite.

Implementasi Verilog mencakup modul dasar seperti:
- ReLU Activation
- Max Pooling
- Fully Connected Layer
- CNN Top Module
- Testbench

Implementasi Verilog saat ini merupakan demonstrasi dasar dan belum terintegrasi dengan bobot model CNN hasil training.

## 6. Kesimpulan

Proyek ini mengembangkan dasar sistem klasifikasi rambu lalu lintas menggunakan CNN. Model Python menjadi dasar pengembangan sistem, sedangkan implementasi Verilog merupakan tahap awal menuju realisasi perangkat keras berbasis FPGA.

## 7. Pengembangan Selanjutnya

- Integrasi bobot CNN ke dalam Verilog.
- Pengujian menggunakan ModelSim.
- Implementasi pada FPGA menggunakan Quartus Prime.
- Evaluasi akurasi dan performa sistem perangkat keras.
