# ReviewShield AI — Coordinated Bot Review Detection System

# Complete Project Report

---

# Table of Contents

1. Introduction
2. Problem Statement
3. Objectives
4. Existing System Analysis
5. Proposed System
6. System Architecture
7. Technology Stack
8. Dataset Description
9. Phase 1 — Data Engineering
10. Phase 2 — Feature Engineering
11. Future Phases
12. Expected Outcomes
13. Conclusion

---

# 1. Introduction

## Project Title

ReviewShield AI — Coordinated Bot Review Detection System

## Domain

Artificial Intelligence / Machine Learning / Fraud Detection / NLP / Graph Analytics

## Overview

Online review platforms are heavily affected by fake reviews, bot-generated spam, coordinated manipulation campaigns, and fraudulent reviewer communities.

Traditional spam detection systems mainly rely on:

* keyword filtering
* sentiment analysis
* rule-based moderation

These systems fail to detect:

* coordinated reviewer groups
* temporal fraud bursts
* graph-level suspicious behavior
* AI-generated review spam

ReviewShield AI is designed as an intelligent fraud detection platform that combines:

* Natural Language Processing (NLP)
* Temporal Analytics
* Graph Intelligence
* Machine Learning
* Explainable AI

The system aims to identify suspicious reviews, fraudulent reviewers, and coordinated bot campaigns using advanced ML engineering pipelines.

---

# 2. Problem Statement

Online review ecosystems are vulnerable to:

* fake reviewers
* bot accounts
* review farms
* coordinated review attacks
* AI-generated spam reviews

Current moderation systems are weak against modern fraud strategies because they mainly focus only on review text.

The major limitations include:

* inability to detect reviewer coordination
* lack of graph-based analysis
* absence of temporal fraud signals
* poor explainability
* weak scalability

The goal of this project is to build a scalable fraud intelligence platform capable of detecting coordinated fake review campaigns with high accuracy and explainability.

---

# 3. Objectives

## Primary Objective

Detect coordinated fake review campaigns using a multi-modal ML system.

## Secondary Objectives

* Detect suspicious reviewer communities
* Identify burst review attacks
* Generate fraud risk scores
* Provide explainable predictions
* Build graph-based reviewer intelligence
* Develop scalable ML engineering pipelines

---

# 4. Existing System Analysis

## Existing Systems

Most fake review detection systems rely on:

* sentiment analysis
* spam keywords
* text-only classifiers

## Limitations of Existing Systems

| Limitation            | Impact                                |
| --------------------- | ------------------------------------- |
| No graph intelligence | Cannot detect coordinated fraud rings |
| No temporal analysis  | Misses burst campaigns                |
| Text-only analysis    | Weak against advanced fake reviews    |
| No explainability     | Difficult to trust predictions        |
| Poor scalability      | Hard to deploy in production          |

---

# 5. Proposed System

## Proposed Solution

ReviewShield AI integrates multiple fraud intelligence modules into a unified ML pipeline.

## Core Components

### NLP Intelligence

Analyzes:

* review text
* writing patterns
* sentiment
* stylometry
* semantic behavior

### Temporal Intelligence

Analyzes:

* review burst patterns
* synchronized reviewer activity
* inter-arrival timings
* posting entropy

### Graph Intelligence

Analyzes:

* reviewer-product networks
* suspicious reviewer communities
* graph centrality
* coordinated behavior clusters

### ML Risk Engine

Combines all generated features into a unified fraud prediction system.

---

# 6. System Architecture

```text
                ┌────────────────────┐
                │ Review Datasets    │
                └─────────┬──────────┘
                          │
                          ▼
               ┌────────────────────┐
               │ Data Engineering   │
               └─────────┬──────────┘
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼

┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ NLP Features │ │ Temporal     │ │ Graph        │
│              │ │ Features     │ │ Features     │
└──────┬───────┘ └──────┬───────┘ └──────┬───────┘
       │                │                │
       └────────────────┼────────────────┘
                        ▼
             ┌────────────────────┐
             │ Feature Fusion     │
             └─────────┬──────────┘
                       ▼
             ┌────────────────────┐
             │ XGBoost Model      │
             └─────────┬──────────┘
                       ▼
             ┌────────────────────┐
             │ Fraud Risk Engine  │
             └─────────┬──────────┘
                       ▼
             ┌────────────────────┐
             │ FastAPI Backend    │
             └─────────┬──────────┘
                       ▼
             ┌────────────────────┐
             │ Streamlit UI       │
             └────────────────────┘
```

---

# 7. Technology Stack

| Layer                | Technology               |
| -------------------- | ------------------------ |
| Programming Language | Python                   |
| Data Processing      | Pandas                   |
| NLP                  | TextBlob, VaderSentiment |
| Graph Analysis       | NetworkX                 |
| Machine Learning     | Scikit-learn, XGBoost    |
| Backend              | FastAPI                  |
| Frontend             | Streamlit                |
| Data Storage         | Parquet                  |
| Visualization        | Plotly, PyVis            |
| Version Control      | Git + GitHub             |

---

# 8. Dataset Description

## Dataset Used

YelpChi Fraud Dataset

## Reason for Selection

| Advantage                         | Importance                  |
| --------------------------------- | --------------------------- |
| Spam labels included              | Saves labeling effort       |
| User-review-product relationships | Required for graph analysis |
| Research benchmark dataset        | Strong project credibility  |
| Used in fraud research papers     | Industry relevance          |

## Dataset Contents

The dataset contains:

* reviews
* users
* restaurants/products
* timestamps
* fraud labels

## Dataset Files

* new_data_train.csv
* new_data_test.csv

---

# 9. Phase 1 — Data Engineering

## Objective

Build a scalable and reusable fraud-analysis data pipeline.

---

## 9.1 Project Structure

```text
bot-review-detection/
│
├── data/
│   ├── raw/
│   ├── processed/
│   ├── interim/
│   └── external/
│
├── src/
│   ├── data_pipeline/
│   ├── preprocessing/
│   ├── graph/
│   └── utils/
│
├── notebooks/
├── artifacts/
└── features/
```

---

## 9.2 Data Ingestion Pipeline

### Purpose

The ingestion pipeline:

* loads raw datasets
* validates schema
* normalizes columns
* converts datasets into parquet format

### Standardized Master Schema

| Column      | Description              |
| ----------- | ------------------------ |
| review_id   | Unique review identifier |
| user_id     | Reviewer ID              |
| product_id  | Restaurant/product ID    |
| review_text | Review content           |
| rating      | Review score             |
| timestamp   | Review date              |
| label       | Fraud label              |

---

## 9.3 Initial Data Analysis

EDA was performed using Jupyter Notebook.

### Checks Performed

* dataset shape
* column inspection
* null value analysis
* datatype inspection
* label distribution
* review length analysis
* timestamp parsing

### Important Findings

* dataset imbalance detected
* few null reviews found
* timestamps required normalization
* duplicate reviews existed

---

## 9.4 Data Cleaning Pipeline

### Cleaning Operations

Removed:

* null reviews
* duplicate reviews
* empty text
* corrupted timestamps

Normalized:

* lowercase conversion
* whitespace cleanup
* unicode cleanup

### Benefits

* improves model quality
* prevents data leakage
* ensures consistent preprocessing

---

## 9.5 Chronological Data Splitting

### Why Chronological Split?

Random splitting causes:

* temporal leakage
* future information exposure
* unrealistic evaluation

### Correct Strategy

* oldest reviews → training set
* recent reviews → validation set
* newest reviews → test set

### Generated Files

```text
train.parquet
val.parquet
test.parquet
```

---

## 9.6 Graph-Ready Tables

### Users Table

Contains:

* review count
* average rating
* account activity metrics

### Products Table

Contains:

* total reviews
* average ratings

### Edges Table

Represents reviewer-product relationships.

| Column     |
| ---------- |
| user_id    |
| product_id |
| review_id  |
| timestamp  |
| label      |

---

## 9.7 Data Validation Utilities

Validation checks included:

* missing columns
* duplicate review IDs
* null IDs
* timestamp validity

---

## 9.8 Phase 1 Outputs

### Generated Artifacts

```text
reviews_clean.parquet
train.parquet
val.parquet
test.parquet
users.parquet
products.parquet
edges.parquet
```

### Deliverables Completed

#### Data

* cleaned dataset
* parsed timestamps
* split datasets
* graph-ready tables

#### Code

* ingestion pipeline
* cleaning module
* validation utilities

#### Analysis

* EDA notebook
* temporal analysis
* class imbalance analysis

---

# 10. Phase 2 — Feature Engineering

## Objective

Transform cleaned datasets into ML-ready fraud intelligence features.

---

## 10.1 Feature Engineering Modules

### Implemented Modules

| Module            | Purpose                               |
| ----------------- | ------------------------------------- |
| NLP Features      | Extract textual fraud signals         |
| Temporal Features | Extract timing anomalies              |
| Graph Features    | Extract reviewer network intelligence |
| Feature Fusion    | Combine all features                  |

---

# 10.2 NLP Feature Engineering

## Features Generated

### Sentiment Features

* polarity
* subjectivity
* vader sentiment score

### Stylometry Features

* character count
* word count
* average word length
* uppercase ratio
* exclamation count
* lexical diversity

## Purpose

These features help identify:

* spam writing patterns
* exaggerated sentiment
* repetitive language
* bot-generated reviews

---

# 10.3 Temporal Feature Engineering

## Features Generated

### Review Density

Measures number of reviews posted within short time windows.

### Burst Score

Detects sudden spikes in review activity.

### Interarrival Time

Measures time difference between consecutive user reviews.

### Time Entropy

Measures randomness in reviewer posting behavior.

### Night Activity

Detects suspicious nighttime posting patterns.

## Purpose

Temporal signals help identify:

* coordinated attacks
* synchronized review campaigns
* automated bot behavior

---

# 10.4 Graph Feature Engineering

## Graph Construction

A bipartite graph was built between:

* reviewers
* products/restaurants

## Features Generated

### Degree Centrality

Measures reviewer connectivity.

### PageRank

Measures reviewer influence within the graph.

### Community Detection

Detects suspicious reviewer groups using Louvain clustering.

### Clustering Coefficient

Measures tightly connected reviewer behavior.

## Purpose

Graph intelligence helps identify:

* reviewer rings
* fraud communities
* coordinated manipulation campaigns

---

# 10.5 Feature Fusion

## Objective

The feature fusion stage combines all generated fraud intelligence features into a single machine-learning-ready dataset.

The fusion pipeline integrates:

* NLP features
* temporal features
* graph features

into one unified feature space.

---

## Operations Performed

### Removed Columns

Temporary and unnecessary columns were removed to optimize the final dataset.

Dropped columns included:

* raw review text
* cleaned review text
* timestamps
* temporary preprocessing columns

### Benefits

Feature fusion provides:

* cleaner ML inputs
* reduced memory usage
* better training efficiency
* reusable feature datasets

---

# 10.6 Centralized Feature Pipeline

## Objective

A centralized feature engineering pipeline was created to automate all feature generation stages.

The pipeline performs:

1. dataset loading
2. NLP feature generation
3. temporal feature generation
4. graph feature generation
5. feature fusion
6. parquet export

---

## Pipeline Workflow

```text
Processed Dataset
        │
        ▼
NLP Feature Engineering
        │
        ▼
Temporal Feature Engineering
        │
        ▼
Graph Feature Engineering
        │
        ▼
Feature Fusion
        │
        ▼
Feature Store Export
```

---

## Benefits of Centralized Pipelines

### Reusability

The same feature pipeline can be reused for:

* training datasets
* validation datasets
* test datasets
* future datasets

### Scalability

Modular architecture makes it easier to:

* add new features
* debug components
* retrain models
* scale workflows

### Maintainability

The project remains organized because each feature module is isolated and reusable.

---

# 10.7 Feature Store

## Objective

A dedicated feature store was created to store all engineered ML-ready datasets.

### Storage Format

All feature datasets are stored as:

```text
.parquet
```

### Why Parquet?

Parquet is optimized for:

* fast reading
* efficient compression
* scalable analytics
* ML pipelines

---

## Feature Store Structure

```text
artifacts/
│
└── feature_store/
    ├── train_features.parquet
    ├── val_features.parquet
    └── test_features.parquet
```

---

# 10.8 Features Generated Summary

## NLP Intelligence Features

| Feature           | Purpose                               |
| ----------------- | ------------------------------------- |
| polarity          | Measures review positivity/negativity |
| subjectivity      | Measures emotional bias               |
| vader_score       | Social-media style sentiment analysis |
| lexical_diversity | Detects repetitive writing            |
| uppercase_ratio   | Detects spam emphasis                 |
| exclamation_count | Detects exaggerated reviews           |

---

## Temporal Intelligence Features

| Feature              | Purpose                               |
| -------------------- | ------------------------------------- |
| review_density       | Detects dense review activity         |
| burst_score          | Detects burst attacks                 |
| interarrival_seconds | Measures posting gaps                 |
| time_entropy         | Detects posting randomness            |
| night_post           | Detects suspicious nighttime activity |

---

## Graph Intelligence Features

| Feature           | Purpose                                   |
| ----------------- | ----------------------------------------- |
| degree_centrality | Measures reviewer connectivity            |
| pagerank          | Measures reviewer influence               |
| community_id      | Detects suspicious reviewer groups        |
| clustering_coeff  | Measures tightly connected fraud behavior |

---

# 10.9 Phase 2 Outputs

## Generated Datasets

The Phase 2 pipeline generated:

```text
train_features.parquet
val_features.parquet
test_features.parquet
```

These datasets are fully prepared for:

* machine learning
* fraud classification
* anomaly detection
* explainable AI analysis

---

## Phase 2 Deliverables

### Feature Engineering

* NLP fraud signals
* temporal fraud signals
* graph intelligence features
* fused feature datasets

### Pipeline Engineering

* reusable feature modules
* centralized feature pipeline
* parquet feature store

### ML Preparation

* scalable feature architecture
* model-ready datasets
* production-style preprocessing

---

# 11. Phase 3 — Modeling

## Objective

Build machine learning models capable of predicting fraudulent reviews and suspicious reviewer behavior.

---

## 11.1 Baseline Modeling

The first stage of modeling focuses on establishing benchmark performance using simple and interpretable algorithms.

### Initial Models

* Logistic Regression
* Decision Tree
* Random Forest

### Purpose

These models help:

* establish baseline metrics
* validate feature quality
* understand feature importance
* identify data leakage issues

---

## 11.2 Advanced Fraud Detection Model

After baseline validation, advanced ensemble models are planned.

### Planned Models

* XGBoost
* LightGBM (optional)
* CatBoost (optional)

### Why XGBoost?

XGBoost performs exceptionally well on:

* tabular fraud datasets
* imbalanced classification problems
* heterogeneous feature spaces

It also supports:

* class weighting
* missing value handling
* feature importance extraction

---

## 11.3 Training Pipeline

The modeling pipeline will:

* load engineered feature datasets
* separate features and labels
* handle imbalance using class weights
* train multiple ML models
* evaluate model performance
* save trained artifacts

---

## 11.4 Evaluation Metrics

Fraud detection systems require specialized evaluation metrics.

### Metrics Used

| Metric    | Purpose                              |
| --------- | ------------------------------------ |
| Accuracy  | Overall correctness                  |
| Precision | Reduces false positives              |
| Recall    | Detects maximum fraud                |
| F1 Score  | Balance between precision and recall |
| ROC-AUC   | Overall classification capability    |

### Important Focus

In fraud detection:

* high precision prevents innocent users from being flagged
* high recall ensures fraudulent reviews are detected

---

## 11.5 Planned Outputs

### Generated Artifacts

```text
models/
│
├── logistic_regression.pkl
├── random_forest.pkl
├── xgboost_model.pkl
└── scaler.pkl
```

---

## 11.6 Explainability Integration

The trained models will later integrate:

* SHAP explainability
* feature attribution analysis
* fraud reasoning visualization

Example explanation:

```text
Fraud detected because:
- high burst activity
- suspicious graph community
- repetitive writing behavior
```

---

# 12. Future Phases

## Phase 3 — Modeling

Planned models:

* Logistic Regression
* Random Forest
* XGBoost

## Phase 4 — Explainability

Planned features:

* SHAP explanations
* feature importance visualization
* fraud reasoning system

## Phase 5 — Backend Development

Technology:

* FastAPI

## Phase 6 — Frontend Dashboard

Technology:

* Streamlit

Planned features:

* fraud analytics dashboard
* graph visualization
* explainability insights

## Phase 7 — Deployment & MLOps

Planned additions:

* MLflow
* model monitoring
* experiment tracking
* deployment pipeline

---

# 13. Expected Outcomes

The completed system should:

* detect coordinated fake review campaigns
* identify suspicious reviewer communities
* provide explainable fraud predictions
* visualize fraud networks
* simulate industry-grade ML engineering workflows

---

# 14. Conclusion

ReviewShield AI represents a modern AI-powered fraud detection platform that combines:

* Natural Language Processing
* Temporal Analytics
* Graph Intelligence
* Machine Learning
* Explainable AI

The project demonstrates:

* scalable ML engineering
* fraud intelligence pipelines
* graph-based anomaly detection
* real-world production-style architecture

The system is designed not only as an academic project, but also as a simulation of modern trust & safety platforms used in industry-scale review ecosystems.
