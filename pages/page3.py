import streamlit as st

st.markdown("""
          <style>
                    body {
                              background-color: #f5f6fa;
                    }
                    .main {
                              padding-top: 2rem;
                    }
                    h1 {
                              text-align: center;
                              font-weight: 700;
                    }
                    .author {
                              text-align: center;
                              font-size: 16px;
                              color: #555;
                              margin-bottom: 35px;
                    }
                    .section {
                              background-color: black;
                              padding: 30px 35px;
                              border-radius: 14px;
                              margin-bottom: 30px;
                              box-shadow: 0px 6px 18px rgba(0,0,0,0.06);
                    }
                    .section h2 {
                              font-size: 22px;
                              font-weight: 700;
                              margin-bottom: 15px;
                              border-left: 6px solid #1f77b4;
                              padding-left: 12px;
                    }
                    .section p {
                              font-size: 16px;
                              line-height: 1.85;
                              text-align: justify;
                    }
                    .keyword {
                              font-weight: 600;
                    }
          </style>
""", unsafe_allow_html=True)

# st.subheader("Simpulan")
st.markdown("""
    <div class="section">
        <h2>Simpulan</h2>
        <p>
        Berdasarkan hasil analisis regresi, uji asumsi klasik, dan data teoritis, dapat diambil kesimpulan bahwa variabel independen CAR secara independen berpengaruh positif dan signifikan terhadap pertumbuhan PDB konstan di Indonesia selama periode 2012 hingga 2024. Sedangkan, variabel lainnya LDR, NIM, ROA, dan BOPO tidak berpengaruh terhadap PDB yang disebabkan menurunnya kredit dan tren digitalisasi dalam perbankan. Namun, secara simultan variabel independen dalam penelitian berpengaruh positif dan signifikan terhadap pertumbuhan PDB. Hal ini sejalan dengan penelitian (Wiratnoko & Putra, 2022) yang menyatakan bahwa perkembangan sektor perbankan berhubungan positif dengan pertumbuhan ekonomi dalam jangka pendek. Hal ini disebabkan variabel kinerja bank saling mempengaruhi dalam operasional bank.
	    Secara metodologis, penelitian ini memiliki beberapa kendala, yaitu korelasi yang tinggi antar variabel seperti ROA dan NIM yang mengukur profitabilitas bank dari segi margin bunga dan efisiensi aset serta LDR dan BOPO yang menggambarkan efisiensi dan kemampuan penyaluran dana. Meskipun multikolinearitas mampu diatasi dengan variabel lag PDB konstan, secara individu variabel LDR, NIM, ROA, dan BOPO tidak berpengaruh terhadap PDB konstan. Kendala berikutnya yaitu perbedaan variabel dan skala yang sangat berbeda. Kinerja bank diukur dengan persentase yang angkanya di bawah 100%, sedangkan PDB memiliki satuan miliar rupiah. Perbedaan ini menyebabkan peningkatan varian error dan mengganggu kestabilan model. Penguatan model penelitian dapat dilakukan dengan menambah variabel makro ekonomi seperti kurs, suku bunga, dan inflasi untuk mewakili variabel eksternal yang mempengaruhi PDB dan menghindari bias.
        </p>
    </div>
""",unsafe_allow_html=True)

# st.subheader("Daftar Pustaka")
st.markdown("""
    <div class="section">
        <h2>Daftar Pustaka</h2>
        <p>Bahauddin, U. A., & Budiandru. (2023). Pengaruh Kinerja Laporan Keuangan Bank Perkreditan Rakyat Syariah dan Konvensional terhadap Pertumbuhan Ekonomi Indonesia. Jurnal Ilmu Ekonomi dan Studi Pembangunan.</p>
        <p>Irawan, P., Damayanti, E., Pratama, R. P., Siagian, L. D., & Hanggraeni, D. (2025). Operational Risk and Bank Profitability: Analyzing BOPO and Efficiency Ratios in Indonesian Commercial Banks. Jurnal Pendidikan Indonesia.</p>
        <p>Juwita, S., Raga, P. D., Prasetyo, F. I., & Rimawan, E. (2018). Effect of Car (Capital Adequacy Ratio), BOPO (Operational Costs on Operational Revenues, and LDR (Loan to Deposit Ratio) to ROA (Return on Assets) PD Bank Pasar Bogor City. International Journal of Innovative Science and Reserch Technology, 305-309.</p>
        <p>Ningrum, A. M., & Hutagaol, R. M. (2023). Penerapan Time Series Forecasting untuk Memprediksi Pertumbuhan Ekonomi Indonesia 2024. Data Sciences Indonesia, 12-22.</p>
        <p>Purbayanti, R. T., & Yogatama, A. N. (2018). Pengaruh Earning Share Per Share, Debt To Equity Ratio, dan Return on Equity Terhadap Saham LQ45 . Jurnal Ilmiah Bisnis dan Ekonomi Asia, 66-76.</p>
        <p>Rahmatullah, & Mustafa, M. (2022). Pandemic Effect in the Influence of Growth of Credit, CAR, LDR, and Credit Interest on NPL on Commercial Banks in Indonesia. BIRCI-Journal.</p>
        <p>Ronaldo, E. (2017). Pengaruh Intermediasi Perbankan Terhadap Pertumbuhan Ekonomi Indonesia. Tirtayasa Ekonomika.</p>
        <p>Safitri, N., Zakiyyah, N. A., & Nasir, M. S. (2024). Determinants of The Influence of CAR, NIM, NPL, LDR, BOPO, and Total Credit on ROA in Conventional Commercial Banks: ARDL Approach. ResearchGate.</p>
        <p>Sari, K., & Fauzan. (2025). The Impact of Financial Ratios on Bank Profitability: Evidence From IDX (2021-2023). Institute for Law and Economics Studies.</p>
        <p>Setiawan, I. (2020). Analisis Peran Perbankan Terhadap Pertumbuhan Ekonomi di Indonesia: Bank Syariah Versus Bank Konvensional. Jurnal Akuntansi, Ekonomi, dan Manajemen Bisnis, 52-60.</p>
        <p>Suhendra, I., & Ronaldo, E. (2017). Pengaruh Intermediasi Perbankan Terhadap Pertumbuhan Ekonomi Indonesia. Tirtayasa Ekonomika.</p>
        <p>Syahputra, D., & Ningsih, S. (2020). Pengaruh Kredit Perbankan Konvensional dan Pembiayaan Perbankan Syariah terhadap Pertumbuhan Ekonomi Indonesia. Jurnal Ekonomi dan Bisnis Islam.</p>
        <p>Wijaksana, A. C., Pangestu, P. A., Febriyanti, S., Anwar, C. J., & Suhendra, I. (2023). Analisis Pengaruh Kinerja Bank Indonesia terhadap Pertumbuhan Ekonomi Indonesia. Jurnal Ilmiah Manajemen, Ekonomi Bisnis, Kewirausahaan.</p>
        <p>Wiratnoko, D., & Putra, W. L. (2022). Pengaruh Aktivitas Lembaga Perbankan terhadap Pertumbuhan Ekonomi: Kajian pada Sektor Perbankan dan Perubahan Teknologi. Jurnal Mahasiswa.</p>
    </div>
""",unsafe_allow_html=True)


    