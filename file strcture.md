# Project File Structure

Generated/dependency folders are omitted from this structure:
`node_modules/`, `.git/`, `__pycache__/`, and `backend/tele/`.

```text
Telecom - Big Data Churn Prediction/
|-- backend/
|   |-- __init__.py
|   |-- data/
|   |   |-- processed/
|   |   `-- raw/
|   |       |-- Telco_customer_churn.csv
|   |       `-- Telco_customer_churn.xlsx
|   |-- docker/
|   |   `-- Dockerfile
|   |-- models/
|   |   `-- churn_pipleine/
|   |-- notebooks/
|   |   `-- eda.ipynb
|   |-- outputs/
|   |   |-- dag_screenshot.png
|   |   |-- metrics.txt
|   |   `-- predictions.csv
|   `-- src/
|       |-- __init__.py
|       |-- config/
|       |   |-- __init__.py
|       |   |-- paths.py
|       |   `-- spark_config.py
|       |-- data_processing/
|       |   |-- __init__.py
|       |   |-- load_data.py
|       |   `-- validate_data.py
|       |-- deployment/
|       |   |-- __init__.py
|       |   |-- batch_predict.py
|       |   `-- save_pipeline.py
|       |-- feature_engineering/
|       |   |-- __init__.py
|       |   |-- spark_sql_features.py
|       |   `-- vector_assembler.py
|       |-- modeling/
|       |   |-- __init__.py
|       |   |-- evaluate.py
|       |   |-- train_logistic.py
|       |   `-- train_random_forest.py
|       `-- utils/
|           |-- __init__.py
|           `-- logger.py
|-- frontend/
|   |-- public/
|   |   |-- favicon.svg
|   |   `-- icons.svg
|   |-- src/
|   |   |-- assets/
|   |   |   |-- hero.png
|   |   |   |-- react.svg
|   |   |   `-- vite.svg
|   |   |-- components/
|   |   |   |-- analytics/
|   |   |   |   |-- ChurnChart.jsx
|   |   |   |   `-- InternetServiceChart.jsx
|   |   |   |-- common/
|   |   |   |-- dashboard/
|   |   |   |   |-- HighRiskTable.jsx
|   |   |   |   |-- InsightCard.jsx
|   |   |   |   |-- PipelineCard.jsx
|   |   |   |   |-- ProgressCard.jsx
|   |   |   |   `-- StatCard.jsx
|   |   |   |-- layout/
|   |   |   |   |-- Sidebar.jsx
|   |   |   |   `-- TopNavbar.jsx
|   |   |   |-- pipeline/
|   |   |   |-- prediction/
|   |   |   `-- ui/
|   |   |       |-- badge.jsx
|   |   |       |-- button.jsx
|   |   |       |-- card.jsx
|   |   |       |-- input.jsx
|   |   |       |-- progress.jsx
|   |   |       |-- separator.jsx
|   |   |       |-- sheet.jsx
|   |   |       `-- table.jsx
|   |   |-- context/
|   |   |-- data/
|   |   |   `-- dashboardData.js
|   |   |-- hooks/
|   |   |-- layouts/
|   |   |   `-- MainLayout.jsx
|   |   |-- lib/
|   |   |   `-- utils.js
|   |   |-- pages/
|   |   |   |-- Analytics.jsx
|   |   |   |-- ChurnPrediction.jsx
|   |   |   |-- Dashboard.jsx
|   |   |   |-- DataPipeline.jsx
|   |   |   |-- FeatureEngineering.jsx
|   |   |   |-- ModelPerformance.jsx
|   |   |   `-- NotFound.jsx
|   |   |-- routes/
|   |   |   `-- AppRoutes.jsx
|   |   |-- services/
|   |   |-- styles/
|   |   |-- utils/
|   |   |-- App.css
|   |   |-- App.jsx
|   |   |-- index.css
|   |   `-- main.jsx
|   |-- .gitignore
|   |-- components.json
|   |-- eslint.config.js
|   |-- index.html
|   |-- jsconfig.json
|   |-- package-lock.json
|   |-- package.json
|   |-- README.md
|   `-- vite.config.js
|-- sparkscale-ui/
|   |-- public/
|   |   `-- vite.svg
|   |-- src/
|   |   |-- assets/
|   |   |   `-- react.svg
|   |   |-- components/
|   |   |   |-- ui/
|   |   |   |   `-- button.tsx
|   |   |   `-- theme-provider.tsx
|   |   |-- lib/
|   |   |   `-- utils.ts
|   |   |-- App.tsx
|   |   |-- index.css
|   |   `-- main.tsx
|   |-- .gitignore
|   |-- .prettierignore
|   |-- .prettierrc
|   |-- components.json
|   |-- eslint.config.js
|   |-- index.html
|   |-- package-lock.json
|   |-- package.json
|   |-- README.md
|   |-- tsconfig.app.json
|   |-- tsconfig.json
|   |-- tsconfig.node.json
|   `-- vite.config.ts
|-- .gitignore
|-- convert.py
|-- file strcture.md
|-- incomplete files
|-- main.py
|-- package-lock.json
|-- package.json
|-- README.md
|-- requirements.txt
`-- test.py
```
