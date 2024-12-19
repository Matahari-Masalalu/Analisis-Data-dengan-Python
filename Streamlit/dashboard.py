import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import datetime

# Set page config
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

def stats_year(df_clean_day):
    total_sewa_per_tahun = df_clean_day.groupby('yr').nunique().reset_index()
    total_sewa_per_tahun.rename(columns={'instant': 'sum'}, inplace=True)
    return total_sewa_per_tahun

def sidebar(df_clean_day):
    st.sidebar.image('https://github.com/Matahari-Masalalu/Analisis-Data-dengan-Python/blob/main/Asset/icon.jpg')
    min_date = pd.to_datetime(df_clean_day['dteday']).min()
    max_date = pd.to_datetime(df_clean_day['dteday']).max()
    date_input = st.sidebar.date_input(
        label='Rentang Waktu',
        value=[min_date, max_date],
        min_value=min_date,
        max_value=max_date
    )
    option = st.sidebar.selectbox('Pilih Visualisasi', ('Tahun', 'Bulan', 'Jam'))
    return date_input, option


def weather_impact(df_clean_day):
    cuaca_vs_permintaan = df_clean_day.groupby('weathersit').instant.nunique().reset_index()
    cuaca_vs_permintaan.rename(columns={'instant': 'sum'}, inplace=True)
    return cuaca_vs_permintaan

def season_impact(df_clean_day):
    rentals_per_season = df_clean_day.groupby('season').instant.nunique().reset_index()
    rentals_per_season.rename(columns={'instant': 'sum'}, inplace=True)
    return rentals_per_season

def holiday_impact(df_clean_day):
    rentals_on_holiday = df_clean_day.groupby('holiday').instant.nunique().reset_index()
    rentals_on_holiday.rename(columns={'instant': 'sum'}, inplace=True)
    return rentals_on_holiday
def year(df_clean_day):
    st.subheader('Jumlah Bike Sharing Per Tahun')
    st.markdown("---")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x='yr', y='sum', data=df_clean_day, ax=ax, palette='pastel')
    ax.set_title('Jumlah Bike Sharing Per Tahun', fontsize=20)
    ax.set_xlabel('Tahun', fontsize=15)
    ax.set_ylabel('Jumlah', fontsize=15)
    ax.tick_params(axis='x', labelsize=12)
    ax.tick_params(axis='y', labelsize=12)
    for container in ax.containers:
        ax.bar_label(container, fontsize=12, padding=3)
    st.pyplot(fig)

def month(df_clean_day):
    st.subheader('Jumlah Bike Sharing Per Bulan')
    st.markdown("---")
    total_sepeda_per_bulan = df_clean_day.groupby('mnth')['cnt'].sum().reset_index()

    fig, ax = plt.subplots(figsize=(8, 4))
    sns.lineplot(x='mnth', y='cnt', data=total_sepeda_per_bulan, ax=ax, marker='o', color='coral')
    ax.set_title('Jumlah Bike Sharing Per Bulan', loc='center', fontsize=20, pad=25)
    ax.set_xlabel('Bulan', fontsize=15)
    ax.set_ylabel('Jumlah', fontsize=15)
    ax.tick_params(axis='x', labelsize=12)
    ax.tick_params(axis='y', labelsize=12)

    st.pyplot(fig)

def hour(df_clean_day):
    st.subheader('Jumlah Bike Sharing Per Jam')
    st.markdown("---")
    total_sepeda_per_jam = df_clean_day.groupby('hr')['cnt'].sum().reset_index()

    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(x='hr', y='cnt', data=total_sepeda_per_jam, ax=ax, palette='viridis')
    ax.set_title('Jumlah Bike Sharing Per Jam', loc='center', fontsize=20, pad=25)
    ax.set_xlabel('Jam', fontsize=15)
    ax.set_ylabel('Jumlah', fontsize=15)
    ax.tick_params(axis='x', labelsize=12)
    ax.tick_params(axis='y', labelsize=12)

    for container in ax.containers:
        ax.bar_label(container, fontsize=12, padding=10)

    st.pyplot(fig)

def visual_weathersit(df_clean_day):
    fig, ax = plt.subplots(figsize=(8, 5))

    sns.barplot(x='weathersit', y='sum', data=df_clean_day, ax=ax, palette='Set2')
    ax.set_title('', loc='center', fontsize=20, pad=25)
    ax.set_xlabel('Kondisi Cuaca', fontsize=15)
    ax.set_ylabel('Rata-rata Permintaan Sepeda', fontsize=15)
    ax.set_xticks([0, 1, 2, 3])
    ax.set_xticklabels(['Clear', 'Mist + Cloudy', 'Light Snow', 'Heavy Rain'])

    st.pyplot(fig)

def visual_season(df_clean_day):
    fig, ax = plt.subplots(figsize=(8, 5))

    sns.barplot(x='season', y='sum', data=df_clean_day, ax=ax, palette='coolwarm')
    ax.set_title('', loc='center', fontsize=20, pad=25)
    ax.set_xlabel('Musim', fontsize=15)
    ax.set_ylabel('Rata-rata Permintaan Sepeda', fontsize=15)

    st.pyplot(fig)

def visual_holiday(df_clean_day):
    fig, ax = plt.subplots(figsize=(8, 5))

    sns.barplot(x='holiday', y='sum', data=df_clean_day, ax=ax, palette='pastel')
    ax.set_title('', loc='center', fontsize=20, pad=25)
    ax.set_xlabel('Hari Libur', fontsize=15)
    ax.set_ylabel('Rata-rata Permintaan Sepeda', fontsize=15)

    st.pyplot(fig)

df_clean_day = pd.read_csv('https://github.com/Matahari-Masalalu/Analisis-Data-dengan-Python/blob/main/Dataset/data_day.csv')

date, selected_option = sidebar(df_clean_day)
df_main = df_clean_day[
    (df_clean_day["dteday"] >= str(date[0])) & (df_clean_day["dteday"] <= str(date[1]))
]

with st.container():
    st.subheader('Total Sewa Sepeda')
    df_year = stats_year(df_main)

    if selected_option == 'Tahun':
        year(df_year)

    elif selected_option == 'Bulan':
        month(df_main)

    elif selected_option == 'Jam':
        hour(df_main)

# The remaining section of your Streamlit app...
with st.container():
    st.subheader('Pengaruh Cuaca Buruk Terhadap Permintaan Sepeda')
    df_weathersit = weather_impact(df_main)
    visual_weathersit(df_weathersit)

with st.expander('Keterangan Cuaca'):
    st.write(
    """
    `Mist + Cloudy`: Berkabut dan berawan  
    `Light Snow`: Sedikit bersalju  
    `Clear`: Cuaca cerah  
    `Heavy Rain`: Hujan Deras
    """
    )

# Repeat the same process for seasons and holidays
with st.container():
    st.subheader('Tren Musiman dalam Penggunaan Sepeda')
    df_season = season_impact(df_main)
    visual_season(df_season)

with st.expander('Keterangan Musim'):
    st.write(
    """
    `Fall`: Musim Gugur  
    `Spring`: Musim Semi  
    `Summer`: Musim Panas  
    `Winter`: Musim Dingin
    """
    )

with st.container():
    st.subheader('Pengaruh Hari Libur Terhadap Penggunaan Sepeda')
    df_holiday = holiday_impact(df_main)
    visual_holiday(df_holiday)

with st.expander('Keterangan Hari Libur'):
    st.write(
    """
    `Holiday`: Hari Libur  
    `Non Holiday`: Bukan Hari Libur 
    """
    )

# Footer and custom style remain unchanged
st.markdown("""
<style>
    .footer {
        background-color: #f8f9fa; /* Light background color */
        padding: 20px;
        text-align: center;
        border-top: 1px solid #e0e0e0; /* Subtle top border */
        font-size: 14px;
    }
    .footer a {
        color: #007bff; /* Link color */
        text-decoration: none;
        margin: 0 10px; /* Space between links */
    }
    .footer a:hover {
        text-decoration: underline; /* Underline on hover */
    }
    .footer .icon {
        font-size: 20px; /* Icon size */
        vertical-align: middle; /* Align icon with text */
    }
</style>
<div class="footer">
    <p>© 2024 Bike Sharing Data Analyst. by Faishal Anwar Hasyim</p>
    <p>
        <a href="https://github.com/Matahari-Masalalu" target="_blank" class="icon">
            <i class="ti ti-brand-github"></i> GitHub
        </a>
        |
        <a href="https://www.linkedin.com/in/faishal-anwar-hasyim-1391682a5/" target="_blank" class="icon">
            <i class="ti ti-brand-linkedin"></i> LinkedIn
        </a>
    </p>
</div>
""", unsafe_allow_html=True)

# Add CSS for custom styling
st.markdown("""
<style>
    .stContainer {
        background-color: #f0f0f5;
    }
    .stButton {
        background-color: #4CAF50; /* Green */
        color: white;
    }
    .stButton:hover {
        background-color: #45a049;
    }
</style>
""", unsafe_allow_html=True)
