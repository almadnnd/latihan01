import streamlit as st

st.tittle("Pengaruh Kinerja Perbankan terhadap Pertumbuhan Ekonomi Indonesia Periode 2012-2024")

st.write("""
Alma Dewi Ananda / 021002414005
""")

st.subheader("Abstrak")

st.markdown("""
    <div style="text-align: justify;">
    <p>Penelitian ini bertujuan untuk menganalisis pengaruh kinerja perbankan yang diukur dengan lima indikator yaitu Capital Adequacy Ratio (CAR), Loan to Deposit Ratio (LDR), Return on Assets (ROA), Net Interest Margin (NIM), dan Biaya Operasional terhadap Pendapatan Operasional (BOPO) terhadap pertumbuhan ekonomi di Indonesia selama periode tahun 2012-2024. Pertumbuhan ekonomi diukur dengan variabel Produk Domestik Bruto (PDB) Konstan. Metode analisis yang digunakan yaitu analisi regresi linear berganda dengan data time series dan uji asumsi klasik. Hasil penelitian ini diharapkan dapat memberikan gambaran empiris terkait kontribusi indikator perbankan terhadap stabilitas pertumbuhan ekonomi di Indonesia.
    
Kata Kunci: CAR, LDR, ROA, NIM, BOPO, PDB

</div>
    """,
    unsafe_allow_html=True
)

st.subheader("Latar Belakang")

st.markdown("""
    <div style="text-align: justify;">
    <p>Sektor perbankan memiliki peran strategis dalam medorong pertumbuhan ekonomi melalui intermediasi keuangan. Keberadaan sektor perbankan sangat penting untuk meningkatkan pertumbuhan ekonomi (Purbayanti & Yogatama, 2018). Dukungan keuangan yang kuat dan stabil dapat menciptakan proses transaksi ekonomi yang efisien. Perbankan menjadi tulang punggung dalam penyediaan pembiayaan dengan mengalirkan dana ke sektor-sektor yang produktif termasuk industri, pertanian, perdangan, manufaktur, dan jasa (Ronaldo, 2017). Efektivitas dan efisiensi fungsi intermediasi bank sangat berpengaruh terhadap kelancaran arus modal dalam perekonomian di Indonesia. Oleh karena itu, diperlukan analisis bagaimana faktor-faktor kinerja bank seperti Capital Adequacy Ratio (CAR), Loan to Deposit Ratio (LDR), Return on Assets (ROA), Biaya Operasional terhadap Pendapatan Operasional (BOPO), dan Net Interest Margin (NIM), berpengaruh terhadap pertumbuhan ekonomi Indonesia dalam jangka pendek dan panjang.
	<p>Produk Domestik Bruto (PDB) konstan berperan sebagai indikator utama dalam mengukur pertumbuhan ekonomi Indonesia (Ningrum & Hutagaol, 2023). PDB mencerminkan nilai tambah dari seluruh barang dan jasa yang mampu dihasilkan suatu negara setelah disesaikan dengan tingkat inflasi. Kinerja ekonomi yang sehat dapat ditinjau melalui pertumbuhan PDB yang stabil dan keberlanjutan. Ekonomi Indonesia periode 2012-2024 dihantam dinamika ekonomi global dan domestik. Tantangan yang dihadapi Indonesia berasal dari fluktuasi harga komoditas, instabilitas politik, tekanan geopolitik, percepatan digitalisasi sektor keuangan, hingga pandemi COVID-19. Adaptasi sektor perbankan dalam menyesuaikan strategi operasional dan pembiayaan di tengah dinamika tersebut menjadi perhatian untuk dievaluasi, khususnya yang berkaitan dengan PDB.
	<p>Penelitian ini bertujuan untuk menganalisis secara sistematis bagaimana indikator kinerja perbankan yang diwakili oleh CAR, LDR, ROA. NIM, dan BOPO berkontribusi terhadap pertumbuhan PDB Konstan di Indonesia selama periode waktu 2012-2024. Penelitian ini diharapkan dapat menambah khazanah literatur dalam pemahaman tentang sektor keuangan dalam pembangunan ekonomi nasional serta memperkuat sinergi sektor perbankan dan ekonomi makro di Indonesia.
     </div>
    """,
    unsafe_allow_html=True
)  

st.subheader("Tinjauan Pustaka")

st.markdown("""
    <div style="text-align: justify;">
    <p>Indikator-indikator kinerja perbankan memiliki peran dan pengaruh yang berbeda dalam perekonomian. CAR menunjukan kemampuan perbankan dalam menjaga stabilitas modal dan menyerap risiko keuangan (Safitri, Zakiyyah, & Nasir, 2024). Indikator LDR menggambarkan efektivitas perbankan untuk menyalurkan dana yang dihimpun ke masyarakat menjadi kredit (Juwita, Raga, Prasetyo, & Rimawan, 2018). Sedangkan, indikator ROA mengukur kemampuan bank dalam mengelola aset untuk menghasilkan keuntungan (Sari & Fauzan, 2025). NIM menjadi indikator dalam menghasilkan pendapatan dari aktivitas intermediasi (Sari & Fauzan, 2025). Terakhir, indikator BOPO mencerminkan efisiensi biaya operasional terhadap pendapat yang diperoleh (Sari & Fauzan, 2025). Secara teori, rasio kinerja perbankan yang positif mendorong kemampuan perbankan dalam mendukung ekspansi kegiatan ekonomi melelaui efisiensi operasional dan peningkatan kredit, yang akhirnya berdampak pada peningkatan output nasional.
	<p>Namun, rasio yang positif dari masing-masing indikator maupun keterkaitan indikator kinerja perbankan dan pertumbuhan ekonomi tidak selalu bersifar linear (Rahmatullah & Mustafa, 2022). Terdapat faktor internal dan eksternal yang turut memengaruhi hal tersebut. Rasio LDR yang tinggi tidak selalu berdampak positif apabila diikuti dengan peningkatan angka kredit bermasalah. Begitu pula dengan BOPO yang mencerminkan efisiensi operasional belum tentu memiliki dampak yang signifikan terhadap ekonomi apabila bank belum menjangkau sektor prioritas secara optimal (Irawan, Damayanti, Pratama, Siagian, & Hanggraeni, 2025). 
     </div>
    """,
    unsafe_allow_html=True
)  

st.subheader("Metodologi Penelitian")

st.markdown("""
    <div style="text-align: justify;">
    <p>Penelitian ini menggunakan pendekatan kuantitatif dengan metode regresi linier berganda untuk menganalisis pengaruh kinerja perbankan terhadap pertumbuhan ekonomi di Indonesia selama periode 2012-2024. Data untuk variabel independen berupa CAR, LDR, ROA. NIM, dan BOPO diperoleh dari Otoritas Jasa Keuangan (OJK). Variabel dependen yang digunakan dalam penelitian ini yaitu PDB Konstant yang datanya berasal dari Bank Indonesia. 
	<p>Data diperoleh melalui laporan bulanan dan publikasi resmi dari kedua instansi terkait. Data yang digunakan bersifat time series selama periode 2012-2024 dalam periode waktu bulanan. Analisis data yang digunakan berupa regresi linier berganda dengan metode Ordinary Least Square (OLS) untuk menguji pengaruh varibel independent terhadap variabel dependen. Model regresi yang digunakan sebagai berikut:
 </div>
    """,
    unsafe_allow_html=True
)  

st.latex(r'''
PDB Kontan_{it} = \beta_0_{it}
+ \beta_1 CAR_{it}
+ \beta_2 LDR_{it}
+ \beta_3 ROA_{it}
+ \beta_4 NIM_{it}
+ \beta_5 BOPO_{it}
+ \varepsilon
''')





