# 📊 Social Media Performance Dashboard

Dashboard interactif d'analyse des performances publicitaires sur les réseaux sociaux, construit avec Python, SQL et Streamlit.

🔗 **[Voir le dashboard en ligne](https://social-media-dashboard-w6ntuj3ua8pijez9taoqpw.streamlit.app/)**

---

## 🎯 Objectif du projet

Analyser les performances de 300 000 campagnes publicitaires sur Instagram, Facebook, Twitter et Pinterest pour identifier les leviers de performance et optimiser le ROI.

---

## 💡 Insights clés

- **Pinterest génère un ROI 5x inférieur** aux autres plateformes (0.72 vs ~4.0)
- **La combinaison Twitter + Product Launch** est la plus rentable (ROI 4.04)
- **Avril est le meilleur mois** pour lancer des campagnes (ROI 3.21)
- **Men 45-60 et Men 18-24** ont les meilleurs taux de conversion (~8%)

---

## 🛠️ Stack technique

| Outil | Usage |
|---|---|
| Python / Pandas | Nettoyage et exploration des données |
| SQLite / SQL | Requêtes analytiques |
| Plotly | Visualisations interactives |
| Streamlit | Dashboard web déployé en ligne |
| GitHub | Versioning et déploiement |

---

## 📁 Structure du projet

social-media-dashboard/

│

├── dashboard.py              # Application Streamlit

├── social_media_sample.csv   # Dataset (échantillon 10 000 lignes)

├── requirements.txt          # Dépendances Python

└── README.md                 # Documentation

---

## 📊 Fonctionnalités du dashboard

- **Filtres interactifs** par plateforme et objectif de campagne
- **KPI cards** — ROI moyen, CTR, coût d'acquisition, nombre de campagnes
- **ROI par plateforme** — bar chart + boxplot
- **Evolution temporelle** — ROI mensuel moyen
- **Performance par audience** — taux de conversion et segments clients
- **Top 10 entreprises** — classement par ROI

---

## 🚀 Lancer le projet en local

```bash
# Installer les dépendances
pip install -r requirements.txt

# Lancer le dashboard
streamlit run dashboard.py
```

---

## 📂 Dataset

Source : [Social Media Advertising Dataset](https://www.kaggle.com/datasets/jsonk11/social-media-advertising-dataset) — Kaggle  
300 000 campagnes publicitaires avec métriques de performance (ROI, CTR, conversions, engagement)
