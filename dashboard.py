import streamlit as st
import pandas as pd
import plotly.express as px

# Configuration de la page
st.set_page_config(
    page_title="Social Media Performance Dashboard",
    page_icon="📊",
    layout="wide"
)

# Chargement des données
@st.cache_data
def load_data():
    df = pd.read_csv("social_media_sample.csv")
    df["Acquisition_Cost"] = pd.to_numeric(df["Acquisition_Cost"], errors="coerce")
    df["Date"] = pd.to_datetime(df["Date"])
    df["CTR"] = df["Clicks"] / df["Impressions"] * 100
    return df

df = load_data()

# ─── HEADER ───────────────────────────────────────────
st.title("📊 Social Media Performance Dashboard")
st.markdown("Analyse des performances publicitaires — Instagram, Facebook, Twitter, Pinterest")
st.divider()

# ─── FILTRES ──────────────────────────────────────────
col1, col2 = st.columns(2)

with col1:
    plateformes = st.multiselect(
        "Filtrer par plateforme",
        options=df["Channel_Used"].unique(),
        default=df["Channel_Used"].unique()
    )

with col2:
    objectifs = st.multiselect(
        "Filtrer par objectif",
        options=df["Campaign_Goal"].unique(),
        default=df["Campaign_Goal"].unique()
    )

# Appliquer les filtres
df_filtered = df[
    (df["Channel_Used"].isin(plateformes)) &
    (df["Campaign_Goal"].isin(objectifs))
]

st.divider()

# ─── KPI CARDS ────────────────────────────────────────
st.subheader("📈 Indicateurs clés")

k1, k2, k3, k4 = st.columns(4)

k1.metric("ROI Moyen", f"{df_filtered['ROI'].mean():.2f}")
k2.metric("CTR Moyen", f"{df_filtered['CTR'].mean():.1f}%")
k3.metric("Coût d'acquisition moyen", f"${df_filtered['Acquisition_Cost'].mean():,.0f}")
k4.metric("Nb Campagnes", f"{len(df_filtered):,}")

st.divider()

# ─── GRAPHIQUES ───────────────────────────────────────
st.subheader("📊 Analyse par plateforme")

col1, col2 = st.columns(2)

with col1:
    roi_platform = df_filtered.groupby("Channel_Used")["ROI"].mean().reset_index()
    fig1 = px.bar(
        roi_platform,
        x="Channel_Used",
        y="ROI",
        title="ROI moyen par plateforme",
        color="Channel_Used",
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.box(
        df_filtered,
        x="Channel_Used",
        y="ROI",
        title="Distribution du ROI par plateforme",
        color="Channel_Used",
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

# ─── EVOLUTION TEMPORELLE ─────────────────────────────
st.subheader("📅 Evolution dans le temps")

roi_monthly = df_filtered.groupby(df_filtered["Date"].dt.to_period("M"))["ROI"].mean().reset_index()
roi_monthly["Date"] = roi_monthly["Date"].astype(str)

fig3 = px.line(
    roi_monthly,
    x="Date",
    y="ROI",
    title="Evolution du ROI mensuel moyen",
    markers=True,
    color_discrete_sequence=["#7B2D8B"]
)
st.plotly_chart(fig3, use_container_width=True)

st.divider()

# ─── AUDIENCE & SEGMENTS ──────────────────────────────
st.subheader("🎯 Performance par audience")

col1, col2 = st.columns(2)

with col1:
    audience = df_filtered.groupby("Target_Audience")["Conversion_Rate"].mean().reset_index()
    audience = audience.sort_values("Conversion_Rate", ascending=True)
    fig4 = px.bar(
        audience,
        x="Conversion_Rate",
        y="Target_Audience",
        orientation="h",
        title="Taux de conversion par audience",
        color_discrete_sequence=["#2ecc71"]
    )
    st.plotly_chart(fig4, use_container_width=True)

with col2:
    segment = df_filtered.groupby("Customer_Segment")["ROI"].mean().reset_index()
    fig5 = px.pie(
        segment,
        values="ROI",
        names="Customer_Segment",
        title="ROI moyen par segment client"
    )
    st.plotly_chart(fig5, use_container_width=True)

st.divider()

# ─── TOP ENTREPRISES ──────────────────────────────────
st.subheader("🏆 Top 10 entreprises par ROI")

top_companies = df_filtered.groupby("Company").agg(
    ROI_Moyen=("ROI", "mean"),
    Taux_Conversion=("Conversion_Rate", "mean"),
    Nb_Campagnes=("Campaign_ID", "count")
).reset_index().sort_values("ROI_Moyen", ascending=False).head(10)

top_companies["ROI_Moyen"] = top_companies["ROI_Moyen"].round(2)
top_companies["Taux_Conversion"] = (top_companies["Taux_Conversion"] * 100).round(2)

st.dataframe(top_companies, use_container_width=True)
