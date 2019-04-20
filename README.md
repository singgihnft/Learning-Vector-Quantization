# Learning-Vector-Quantization
Jaringan Syaraf Tiruan


Learning Vector Quantization (LVQ) adalah sebuah metode klasifikasi dimana setiap unit output mempresentasikan sebuah kelas. LVQ digunakan untuk pengelompokkan dimana jumlah kelompok sudah ditentukan arsitekturnya (target/kelas sudah ditentukan).

LVQ salah satu jaringan syaraf tiruan yang merupakan algoritma pembelajaran kompetitif terawasi versi dari algoritma Kohonen Self-Organizing Map (SOM). Tujuan dari algoritma ini adalah untuk mendekati distribusi kelas vektor  untuk meminimalkan kesalahan dalam pengklasifikasian.

Algoritma diusulkan oleh Kohonen pada tahun 1986 sebagai perbaikan dari Vector Quantization. Model pembelajaran LVQ dilatih secara signifikan agar lebih cepat dibandingkan algoritma lain seperti Back Propagation Neural Network. Hal ini dapat meringkas atau mengurangi dataset besar untuk sejumlah kecil vektor.

LVQ melakukan pembelajaran pada lapisan kompetitif yang terawasi. Lapisan kompetitif akan secara otomatis belajar untuk mengklasifikasikan vector-vector input. Kelas-kelas yang didapat sebagai hasil dari lapisan kompetitif ini hanya tergantung pada jarak antara vector-vector input. Jika vector input mendekati sama maka lapisan kompetitif akan mengklasifikasikan kedua vector input tersebut kedalam kelas yang sama.
