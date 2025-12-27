import io
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Visualisasi Data Penelitian", layout="wide")
st.title("Visualisasi Data Penelitian")

@st.cache_data
def load_data(path):
    df = pd.read_csv(path)

    if "Tahun" not in df.columns:
        raise ValueError("Kolom 'Tahun' tidak ditemukan")

    df["Tahun"] = pd.to_numeric(df["Tahun"], errors="coerce")
    df = df.dropna(subset=["Tahun"])
    df["Tahun"] = df["Tahun"].astype(int)

    return df

DATA_PATH = "data/data.csv"
df = load_data(DATA_PATH)

INDICATORS = [c for c in df.columns if c != "Tahun"]

st.subheader("Filter Data")

col1, col2 = st.columns([2, 4])

with col1:
    tahun_min, tahun_max = int(df["Tahun"].min()), int(df["Tahun"].max())
    year_range = st.slider(
        "Rentang Tahun",
        min_value=tahun_min,
        max_value=tahun_max,
        value=(tahun_min,tahun_max)
    )

with col2:
    indikator_pick = st.multiselect(
        "Pilih Indikator",
        options=INDICATORS,
        default=["CAR"] if "CAR" in INDICATORS else INDICATORS[:1]
    )

indikator_kosong = len(indikator_pick) == 0


df_filtered = df[
    (df["Tahun"] >= year_range[0]) &
    (df["Tahun"] <= year_range[1])
]

tab_line, tab_table = st.tabs(["📈 Chart Line", "📋 Tabel Data & Download"])

with tab_line:
    st.subheader("Perkembangan Indikator per Waktu")

    if indikator_kosong:
        st.info("Pilih minimal satu indikator.")
    elif df_filtered.empty:
        st.warning("Data kosong setelah filter.")
    else:
        for ind in indikator_pick:
            plot_df = df_filtered[["Tahun", ind]].dropna()

            if plot_df.empty:
                st.info(f"Tidak ada data untuk indikator {ind}")
                continue

            fig = px.line(
                plot_df,
                x="Tahun",
                y=ind,
                markers=True,
                title=f"{ind} terhadap Waktu"
            )

            fig.update_layout(height=420)
            st.plotly_chart(fig, use_container_width=True)

with tab_table:
    st.subheader("Tabel Data")

    if df_filtered.empty:
        st.warning("Data kosong.")
    else:
        cols_show = ["Tahun"] + (indikator_pick if not indikator_kosong else INDICATORS)
        table_df = df_filtered[cols_show]

        st.dataframe(table_df, use_container_width=True)

        st.divider()
        st.subheader("Download Data")

        csv_bytes = table_df.to_csv(index=False).encode("utf-8")
        st.download_button(
            "⬇️ Download CSV",
            csv_bytes,
            "data_terfilter.csv",
            "text/csv"
        )

        output = io.BytesIO()
        with pd.ExcelWriter(output, engine="openpyxl") as writer:
            table_df.to_excel(writer, index=False, sheet_name="Data")
        st.download_button(
            "⬇️ Download Excel",
            output.getvalue(),
            "data_terfilter.xlsx",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

st.caption("Sumber data: Penelitian Alma Dewi Ananda")
