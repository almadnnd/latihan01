import streamlit as st
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt

st.title("Hasil dan Pembahasan")

st.markdown(
"""
    <div style="text-align: justify;">
    <p>Tabel 1 menunjukan statistik deskriptif dari variabel yang akan diteliti yang memberikan gambaran umum mengenai sebaran data karakteristik variabel independent dan variabel dependen. Terdapat 156 observasi yang yang dimulai dari 2012:1 hingga 2024:12. 
	<p>PDB Konstan periode 2012-2024 memiliki rata-rata sebesar 2.458.042 miliar rupiah dengan median sebesar 2.596.783 miliar rupiah. Standar deviasi 627.252,6 menunjukan adanya keragaman yang cukup tinggi dalam pertumbuhan ekonomi Indonesia sepanjang pengamatan. Nilai minimum PDB 633.243 dan maksimum mencapai 3.296.742 mengindikasikan adanya pertumbuhan ekonomi yang sangat signifikan dalam kurun waktu pengamatan.
	<p>Variabel CAR menunjukan rata-rata sebesar 2,281%, dengan median 2,311%, dan standar deviasi 0,302. Hasil ini mencerminkan bahwa distribusi CAR cukup stabil, dengan penyebaran nilai yang tidak terlalu ekstrem, yakni dari minimum sebesar 1,728% hingga maksimum 3,365%. Nilai tersebut menandakan bahwa rata-rata kecukupan modal bank dalam sistem keuangan Indonesia tetap dalam batas yang aman selama periode pengamatan.
	<p>Rata-rata LDR berada pada 8,693%, dengan nilai median sebesar 8,852%, dan standar deviasi sebesar 0,495. Rentang nilai LDR berkisar antara 7,043% hingga 9,619% megindikasikan bahwa tingkat penyaluran kredit terhadap dana pihak ketiga cukup tinggi, namun tetap relatif konsisten. Hal ini mencerminkan kemampuan intermediasi bank dalam mendorong sektor riil.
	<p>ROA memiliki rata-rata sebesar 2,5518%, dengan median 2,5%, dan standar deviasi sebesar 0,377. Variabel ini memiliki nilai minimum sebesar 1,59% dan maksimum sebesar 3,7%. Nilai ini mencerminkan bahwa tingkat profitabilitas bank dalam menghasilkan laba dari total aset cukup stabil dan sehat diserta fluktuasi yang masih dalam batas wajar.
	<p>Variabel NIM memiliki rata-rata 4,951%, median 4,9%, dan standar deviasi 0,429. Rentang nilai NIM berada antara 4,06% hingga 6,06%. Hal ini menunjukkan bahwa margin keuntungan dari aktivitas kredit cukup konsisten dan relatif tinggi.
	<p>Rata-rata BOPO tercatat sebesar 8,104%, dengan median 8,069%, dan standar deviasi 0,346. Rentang nilai BOPO yang cenderung kecil sebesar 7,013% hingga 9,178% menunjukkan bahwa efisiensi operasional bank cenderung berada pada tingkat yang tinggi namun stabil.
    </div>
""",
unsafe_allow_html=True
)

st.markdown(
"""
    <div style="text-align: justify;">
    <p>Hasil uji asumsi klasik dari variabel independent CAR, LDR, NIM, ROA, dan BOPO serta variabel dependen PDB Konstant menunjukan hasil dari autokorelasi, heteroskedastisitas, dan multikolinearitas yang normal. Namun, tidak lolos dari uji normalitas yang menghasilkan nilai probabilitas Jarque-Berra sangat jauh di bawah signifikansi 0,05.
     </div>
""",
unsafe_allow_html=True
)

st.markdown(
"""
    <div style="text-align: justify;">
   <p>Hasil uji autokorelasi pada model regresi dengan menambahkan LAG pada variabel PDB Konstan menghasilkan p-value sebesar 0,6732. Nilai tersebut lebih dari ambang signifikansi 0,05, artinya tidak terdapat autokorelasi pada model regresi. Nilai residual saat ini tidak bergantung pada nilai residual periode sebelumnya. Selanjutnya uji heteroskedastisitas dengan metode ARCH (Autoregressive Conditional Heteroskedasticity) dan lag 1 menunjukan p-value sebesar 0,9978. Hal ini mencerminkan tidak terdapat pola varians residual yang berubah-ubah secara sistematis dari waktu ke waktu. Artinya, data dalam model yang diuji lolos dari heteroskedastisitas dan varians error cenderung konstan. 
   <p>Uji multikolinearitas menggunakan metode Variance Inflation Factor (VIF), seluruh variabel uji menghasilkan nilai VIF di bawah 10. Dapat disimpulkan bahwa tidak ada korelasi yang tinggi antar variabel independent dalam model pengujian. Setiap variabel independen mampu menjelaskan variasi dari variabel dependen secara mandiri tanpa dipengaruhi variabel lain secara signifikan. Namun, error dalam model pengujian tidak terdistribusi normal terbukti dari hasil p-value Jarque-Berra sebesar 0,0000, bisa dikatakan model dalam uji tidak lolos uji normalitas. 
   </div>
""",
unsafe_allow_html=True
)

st.markdown(
"""
    <div style="text-align: justify;">
    <p>Hasil uji regresi linear berganda, variabel CAR menghasilkan koefisien positif sebesar 128,9478 dengan p-value 0,0324. Hal ini mengindikasikan bahwa setiap kenaikan 1 satuan CAR mampu meningkatkan PDB Konstan sebesar 128,9478. Hal ini sesuai dengan Teori Stabilitas Keuangan menyatakan bahwa nilai CAR yang stabil akan berkontribusi positif terhadap pertumbuhan PDB. Dapat diinterpretasikan bahwa bank yang memiliki modal kuat akan lebih tahan terhadap guncangan, yang pada akhirnya mampu menyalurkan kredit berkelanjutan sehingga mendorong pertumbuhan PDB. 
    <p>Koefisien variabel LDR sebesar 9,802100 dengan p-value 0,6392. Hal ini menandakan bahwa kenaikan variabel LDR dalam penelitian ini tidak memiliki pengaruh langsung terhadap PDB Konstan terbukti dari hasil p-value lebih dari nilai signifikansi 5%. Secara teori, LDR yang digambarkan dengan kredit produktif akan mendorong peningkatan konsumsi, investasi, dan lapangan pekerjaan, sehingga akan berdampak positif pada PDB. Namun, tidak dapat dipungkiri bahwa semakin banyak kredit yang disalurkan memiliki risiko likuiditas yang tinggi atau Non-Performing Loan sehingga mempengaruhi kualitas kredit menjadi tidak optimal. Selain itu, kredit bank biasanya terkonsentrasi pada daerah perkotaan dan sektor unggulan seperti perdagangan besar, manufaktur, pertanian, dan properti. Sedangkan UMKM sebagai penggerak ekonomi seringkali sulit mendapatkan pembiayaan kredit yang memadai. 
    <p>Koefisien NIM sebesar -1.452,021 dengan p-value 0,9494 menunjukan bahwa penurunan NIM tidak berpengaruh lansung terhadap PDB Konstan. Hal ini disebabkan oleh nilai NIM yang terlalu tinggi biasanya mengindikasikan biaya bunga pinjaman yang besar dapat mengurangi permintaan kredit, yang akhirnya menghambat aktivitas ekonomi dan pertumbuhan menurun. NIM yang tinggi tidak serta merta menunjukan perbankan agresif dalam ekspansi kredit sehingga tidak berdampak pada penigkatan ekonomi riil. Rentang 2012-2024 bank mulai menggeser fokus pendapatan menjadi fee-based income seperti ATM, jasa kustodian, layanan digital, transfer dana, kartu kredit, kartu debit, mesin Electronic Data Capture (EDC), dan manajemen investasi. Pendapatan yang lebih stabil dari layanan tersebut membuat bank tidak lagi bergantung pada kredit. Nilai NIM tidak lagi mencerminkan produktifitas bank, sehingga pengarih NIM terhadap PDB cenderung menurun.
    <p>Efek digitalisasi juga berpengaruh terhadap ROA yang menggambarkan profitabilitas bank terhadap total asetnya. Pada model ini nilai ROA memiliki koefisien 17761,64 dan p-value 0,5418. Meskipun memiliki koefisien positif, ROA belum berpengaruh langsung terhadap PDB. Profit yang tinggi belum tentu berasal dari aktivitas penyaluran kredit ke sektor riil yang tinggi. Tren digitalisasi dan diversifikasi produk perbankan kini menjadi penopang profit yang lebih stabil bagi perbankan. Indonesia mengalami tekanan global yang sangat tajam akibat COVID-19 yang menyebabkan bank lebih berhati-hati dalam penyaluran kredit produktif.
    <p>Hal yang tidak biasa terjadi pada variabel BOPO. Umumnya, BOPO akan berpengaruh negatif terhadap PDB. Tingginya akan BOPO mengindikasikan inefisiensi pada bank karena lebih banyak biaya operasional yang dikeluarkan daripada pendapatan, sehingga akan berdampak negatif terhadap pertumbuhan ekonomi. Pada penelitian ini, BOPO memiliki koefisien positif sebesar 50,92092 dengan p-value 0,0692 yang berarti mendekati signifikan pada tingkat signifikansi 5%. Seiring dengan perkembangan zaman, nilai BOPO yang tinggi tidak murni disebabkan oleh inefisiensi, melainkan karena bank mengalami transformasi digital dan investasi teknologi. Selain itu, bank melakukan ekspansi untuk menjangkau masyarakat kategori unbanked dan underbanked dengan membuka kantor cabang di daerah kecil dan agen bank di daerah pedesaan. Bank mengeluarkan biaya yang tinggi dalam jangka pendek untuk investasi dalam sistem digital yang bertujuan meningkatkan efisiensi dalam jangka panjang.
    <p>Lag dari PDB Konstan atau (pdb(-1)) menjadi variabel paling signifikan dengan koefisien 0,9147 dan p-value 0,0000. Hal ini mengindikasikan adanya autopersistensi atau pertumbuhan ekonomi Indonesia memiliki keterkaitan dengan kondisi ekonomi sebelumnya. Pertumbuhan ekonomi terjadi secara bertahap dari waktu ke waktu dan berkelanjutan. Ekonomi yang tubuh pada satu periode, akan terus bertumbuh secara cepat maupun lambat pada periode berikutnya. Selain itu, berbagai sektor ekonomi memiliki proses produksi jangka waktu panjang seperti pembangunan jalan tol dan kereta cepat yang memerlukan pengerjaan bertahun-tahun dan akan berdampak terhadap PDB secara bertahap. Kebijakan pemerintah seperti stimulus ekonomi dan pelonnggaran suku bunga oleh Bank Indonesia tidak langsung berdampak pada tahun berjalan, melainkan berefek pada tahun-tahun berikutnya. 
    <p>Hasil regresi model penelitian menunjukan nilai Adjusted R2 sebesar 0,969758, yang artinya secara simultan seluruh variabel independen mampu menjelaskan variasi PDB sebesar 96% dan sisanya dijelaskan variabel lain yang tidak ada dalam penelitian ini. Nilai Prob (F) sebesar 0,0000 (kurang dari 5%) menjelaskan secara statistik setidaknya ada satu variabel independen yang berpengaruh terhadap PDB konstan. Hal ini terbukti dengan adanya variabel CAR dan lag PDB konstan yang berpengaruh terhadap PDB konstan.

       </div>
""",
unsafe_allow_html=True
)


    



