# 🚗 ABG Motors — Market Entry Analysis for India

## 📊 Customer Purchase Prediction Using Machine Learning

A data-driven **Market Entry Analysis project for ABG Motors**, using customer data from Japan to build a machine-learning model and estimate potential customers in the Indian market.

The project uses **Logistic Regression** to learn purchasing behavior from the Japanese dataset and applies the trained model to Indian customer data to identify potential purchasers.

---

## 🎯 Project Objective

The primary objective of this project is to explore whether customer characteristics observed in the Japanese market can be used to identify **potential customers in India**.

The project follows this approach:

```text
Japanese Customer Data
          │
          ▼
    Data Exploration
          │
          ▼
    Data Cleaning
          │
          ▼
 Feature Engineering
          │
          ▼
  Logistic Regression
          │
          ▼
 Model Evaluation
          │
          ▼
 Indian Customer Data
          │
          ▼
 Purchase Prediction
          │
          ▼
Potential Indian Customers
```

The Japanese dataset contains the historical `PURCHASE` target variable, while the Indian dataset contains customer characteristics without a purchase label. Therefore, Japan is used as the **training baseline** and India as the **prediction population**.

---

# 📁 Dataset Overview

This project uses two customer datasets.

## 🇯🇵 Japanese Dataset

**File:** `JPN Data.xlsx - CN_Mobiles.csv`

The Japanese dataset contains:

* **40,000 rows**
* **6 columns**

### Columns

| Column       | Description                          |
| ------------ | ------------------------------------ |
| `ID`         | Customer identifier                  |
| `CURR_AGE`   | Customer's current age               |
| `GENDER`     | Customer gender                      |
| `ANN_INCOME` | Annual income                        |
| `AGE_CAR`    | Age of customer's car                |
| `PURCHASE`   | Purchase indicator / target variable |

Example structure:

```text
ID          CURR_AGE   GENDER   ANN_INCOME   AGE_CAR   PURCHASE
00001Q15YJ     50        M       445,344       439        0
00003I71CQ     35        M       107,634       283        0
```

---

## 🇮🇳 Indian Dataset

**File:** `IN_Data.xlsx - IN_Mobiles.csv`

The Indian dataset contains:

* **70,000 rows**
* **5 original columns**

### Columns

| Column       | Description                                   |
| ------------ | --------------------------------------------- |
| `ID`         | Customer identifier                           |
| `CURR_AGE`   | Customer's current age                        |
| `GENDER`     | Customer gender                               |
| `ANN_INCOME` | Annual income                                 |
| `DT_MAINT`   | Maintenance/date-related customer information |

The Indian dataset does **not** contain the `PURCHASE` target variable.

Therefore, `PURCHASE` is predicted using the model trained on the Japanese dataset.

---

# 🛠️ Technologies Used

The project is implemented in Python using Jupyter Notebook.

### Core Technologies

* 🐍 Python
* 📓 Jupyter Notebook
* 🐼 Pandas
* 🔢 NumPy
* 📊 Matplotlib
* 🎨 Seaborn
* 🤖 Scikit-learn

### Machine Learning

The following Scikit-learn components are used:

```python
train_test_split
LogisticRegression
StandardScaler
classification_report
roc_auc_score
```

---

# 📦 Installation

Clone the repository:

```bash
git clone <your-repository-url>
```

Navigate into the project:

```bash
cd ABG-Motors-Market-Entry-Analysis
```

Install the required packages:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

---

# ▶️ Running the Project

Start Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```text
capproject.ipynb
```

Make sure the two CSV files are located in the same directory as the notebook:

```text
capproject.ipynb
JPN Data.xlsx - CN_Mobiles.csv
IN_Data.xlsx - IN_Mobiles.csv
```

Run the notebook cells sequentially.

---

# 🔍 Project Workflow

## 1. Import Libraries

The notebook starts by importing the libraries required for:

* Data manipulation
* Numerical calculations
* Visualization
* Machine learning
* Model evaluation

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

Scikit-learn is used for model development and evaluation.

---

# 2. Load the Datasets

The two datasets are loaded using Pandas:

```python
df_japan = pd.read_csv(
    'JPN Data.xlsx - CN_Mobiles.csv'
)

df_india = pd.read_csv(
    'IN_Data.xlsx - IN_Mobiles.csv'
)
```

The notebook then inspects both datasets.

---

# 3. Exploratory Data Analysis

The project performs initial dataset inspection using:

```python
df.info()
```

and:

```python
df.describe(include='all')
```

The notebook also displays the first records using:

```python
df.head()
```

This helps understand:

* Dataset structure
* Data types
* Numerical distributions
* Categorical variables
* Potential data-quality issues

---

# 4. Missing Value Analysis

Missing values are checked using:

```python
df.isnull().sum()
```

This is performed for both Japanese and Indian datasets.

The project uses the Japanese dataset as the training baseline and investigates the availability and quality of the features needed by the model.

---

# 5. Outlier Handling

The notebook defines a reusable function for detecting and capping outliers using the **Interquartile Range (IQR)** method.

```python
def handle_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    df[column] = np.where(
        df[column] > upper_bound,
        upper_bound,
        df[column]
    )

    df[column] = np.where(
        df[column] < lower_bound,
        lower_bound,
        df[column]
    )

    return df
```

The purpose is to reduce the influence of extreme observations.

---

# 6. Data Cleaning

Several transformations are performed before modeling.

## Annual Income

Income values contain commas and therefore need to be converted to numerical values.

For example:

```text
445,344
1,425,390
1,678,954
```

are converted into numeric values.

The notebook performs:

```python
df_japan['ANN_INCOME'] = (
    df_japan['ANN_INCOME']
    .astype(str)
    .str.replace(',', '')
    .astype(float)
)
```

A similar transformation is applied to the Indian dataset.

---

# 7. Gender Encoding

The categorical `GENDER` variable is converted into numeric values.

The notebook uses:

```python
df_japan['GENDER'] = df_japan['GENDER'].map({
    'M': 1,
    'F': 0
})
```

This allows the variable to be used by the machine-learning model.

---

# 8. Feature Engineering for India

One of the important differences between the datasets is:

### Japan

Already contains:

```text
AGE_CAR
```

### India

Contains:

```text
DT_MAINT
```

Therefore, the notebook creates an estimated `AGE_CAR` for Indian customers.

The reference date is based on the latest maintenance date in the Indian dataset:

```python
reference_date = df_india['DT_MAINT'].max()

df_india['AGE_CAR'] = (
    reference_date -
    df_india['DT_MAINT']
).dt.days
```

This creates a feature that is compatible with the Japanese training data.

---

# 🧮 Model Features

The final modeling workflow uses four customer features:

```python
features = [
    'CURR_AGE',
    'GENDER',
    'ANN_INCOME',
    'AGE_CAR'
]
```

These features represent:

```text
Customer Age
      +
Gender
      +
Annual Income
      +
Car Age
      ↓
Purchase Probability
```

---

# 🤖 Machine Learning Model

The project uses **Logistic Regression** as the classification model.

The target variable is:

```python
y = df_japan['PURCHASE']
```

The Japanese dataset therefore provides the labeled training examples.

---

# ✂️ Train-Validation Split

The Japanese dataset is divided into training and validation sets:

```python
X_train, X_val, y_train, y_val = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

The split uses:

```text
80% → Training
20% → Validation
```

with:

```text
random_state = 42
```

for reproducibility.

---

# ⚖️ Feature Scaling

Before training the model, the numerical features are standardized using `StandardScaler`.

```python
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(
    X_train
)

X_val_scaled = scaler.transform(
    X_val
)
```

The scaler is fitted only on the training data and then applied to validation and Indian data.

This ensures that the same transformation is used consistently.

---

# 🧠 Logistic Regression Training

The model is created using:

```python
model = LogisticRegression()
```

and trained using:

```python
model.fit(
    X_train_scaled,
    y_train
)
```

The model learns the relationship between the customer features and the `PURCHASE` outcome.

---

# 📊 Model Evaluation

The validation predictions are generated using:

```python
preds = model.predict(
    X_val_scaled
)
```

The project evaluates the model using:

### Classification Report

```python
classification_report(
    y_val,
    preds
)
```

This provides:

* Precision
* Recall
* F1-score
* Support

### ROC-AUC

The project also calculates:

```python
roc_auc_score(
    y_val,
    model.predict_proba(
        X_val_scaled
    )[:, 1]
)
```

ROC-AUC measures how effectively the model separates the two purchase classes.

---

# 📈 Model Coefficients

The project examines the Logistic Regression coefficients:

```python
for col, coef in zip(
    features,
    model.coef_[0]
):
    print(
        f"{col}: {coef:.4f}"
    )
```

This provides an indication of how each feature contributes to the model's prediction.

The coefficients can be used as an initial way to understand which customer characteristics have stronger positive or negative associations with the predicted purchase outcome.

---

# 🇮🇳 Predicting Potential Indian Customers

After training and validating the model using Japanese customer data, the same preprocessing pipeline is applied to the Indian dataset.

The Indian feature matrix is aligned with the columns used during model training:

```python
X_india = df_india[
    scaler.feature_names_in_
]
```

The Indian data is then transformed using the same scaler:

```python
X_india_scaled = scaler.transform(
    X_india
)
```

Finally, purchase predictions are generated:

```python
india_predictions = model.predict(
    X_india_scaled
)
```

---

# 🎯 Potential Customer Estimation

The predictions are added to the Indian dataset:

```python
df_india[
    'PREDICTED_PURCHASE'
] = india_predictions
```

The total number of predicted potential customers is calculated using:

```python
total_potential_sales = (
    india_predictions.sum()
)
```

The notebook reports this as:

```text
Total projected sales in the Indian sample
```

This provides an estimate of how many customers in the Indian sample are classified as potential purchasers by the model.

---

# 📊 Business Interpretation

The overall business logic can be represented as:

```text
Japanese Market
      │
      ▼
Historical Customer Behavior
      │
      ▼
Machine Learning Model
      │
      ▼
Purchase Pattern
      │
      ▼
Indian Customer Data
      │
      ▼
Predicted Customer Segments
      │
      ▼
Market Entry Insight
```

The project can therefore support an initial exploration of whether a customer-purchase model trained on Japanese data can provide useful signals for the Indian market.

---

# 🧪 Model Development Summary

| Stage                     | Method                           |
| ------------------------- | -------------------------------- |
| Data Loading              | Pandas                           |
| Data Inspection           | `info()`, `describe()`, `head()` |
| Missing Value Analysis    | `isnull().sum()`                 |
| Outlier Method            | IQR                              |
| Income Cleaning           | String → Numeric                 |
| Gender Encoding           | Binary Encoding                  |
| Date Processing           | Pandas Datetime                  |
| Feature Engineering       | `AGE_CAR`                        |
| Train/Test Strategy       | `train_test_split()`             |
| Scaling                   | `StandardScaler`                 |
| Model                     | Logistic Regression              |
| Classification Evaluation | Classification Report            |
| Ranking Metric            | ROC-AUC                          |
| Business Interpretation   | Model Coefficients               |
| India Prediction          | Trained Japan Model              |

---

# 📌 Important Assumption

A key assumption of this project is that **purchasing behavior learned from the Japanese customer dataset can be transferred to Indian customers**.

This is an important modeling assumption and should be validated before using the results for real-world business decisions.

Differences between the two markets may affect model performance, including:

* Customer demographics
* Income distributions
* Consumer behavior
* Automotive preferences
* Economic conditions
* Market structure
* Cultural factors

Therefore, the Indian predictions should be considered **model-based estimates**, not confirmed sales forecasts.

---

# ⚠️ Limitations

## 1. Cross-Market Generalization

The model is trained on Japanese customer behavior but applied to India.

The notebook does not provide an independently labeled Indian `PURCHASE` variable, so actual Indian model accuracy cannot be directly measured.

---

## 2. Target Availability

The Japanese dataset contains:

```text
PURCHASE
```

while the Indian dataset does not.

Therefore, Indian predictions cannot be directly compared with actual Indian purchase outcomes using the provided data.

---

## 3. Reference Date for `AGE_CAR`

Indian `AGE_CAR` is derived from the latest maintenance date in the Indian dataset.

This is a project-specific feature-engineering decision and should be reconsidered if a real business reference date is available.

---

## 4. Model Selection

The project uses Logistic Regression as the classification model.

Other algorithms could potentially capture more complex relationships.

For example:

* Decision Trees
* Random Forest
* Gradient Boosting
* XGBoost
* Support Vector Machines
* Neural Networks

could be compared in future work.

---

# 🚀 Future Improvements

## 🔹 1. Compare Multiple Models

Train and compare:

```text
Logistic Regression
        vs
Decision Tree
        vs
Random Forest
        vs
Gradient Boosting
```

Compare their:

* Accuracy
* Precision
* Recall
* F1-score
* ROC-AUC

---

## 🔹 2. Hyperparameter Tuning

Use:

```text
GridSearchCV
RandomizedSearchCV
```

to find better model parameters.

---

## 🔹 3. Cross-Validation

Instead of relying on a single validation split, use cross-validation to obtain a more robust estimate of model performance.

---

## 🔹 4. Better Feature Engineering

Additional customer features could be developed if available.

Potential features include:

```text
Age Groups
Income Groups
Car Age Groups
Income-to-Age Ratio
Customer Segments
Interaction Features
```

---

## 🔹 5. Model Explainability

Use techniques such as:

* Feature importance
* SHAP
* Partial dependence
* Coefficient analysis

to better understand customer purchasing behavior.

---

## 🔹 6. India-Specific Training Data

The most important future improvement would be to obtain **actual Indian purchase outcomes**.

This would allow the model to be:

```text
Train
  ↓
Validate
  ↓
Test
  ↓
India-specific Evaluation
```

rather than relying entirely on cross-market transfer.

---

# 📂 Recommended Repository Structure

```text
ABG-Motors-Market-Entry-Analysis/
│
├── capproject.ipynb
│
├── JPN Data.xlsx - CN_Mobiles.csv
│
├── IN_Data.xlsx - IN_Mobiles.csv
│
└── README.md
```

For a more production-oriented version, the repository could eventually be organized as:

```text
ABG-Motors-Market-Entry-Analysis/
│
├── data/
│   ├── japan.csv
│   └── india.csv
│
├── notebooks/
│   └── capproject.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── training.py
│   └── prediction.py
│
├── models/
│
├── README.md
└── requirements.txt
```

---

# 📋 Example `requirements.txt`

```text
pandas
numpy
matplotlib
seaborn
scikit-learn
jupyter
```

You can create it with:

```bash
pip freeze > requirements.txt
```

---

# 💡 Key Skills Demonstrated

This project demonstrates practical experience with:

### Python

* Pandas
* NumPy
* Functions
* Data manipulation
* Datetime processing

### Data Science

* Data exploration
* Data cleaning
* Missing-value analysis
* Outlier handling
* Feature engineering
* Descriptive statistics

### Machine Learning

* Train/validation split
* Feature scaling
* Logistic Regression
* Classification
* Probability prediction
* Model evaluation
* ROC-AUC

### Business Analytics

* Customer segmentation
* Purchase prediction
* Cross-market analysis
* Market-entry analysis
* Potential customer estimation

---

# 🏆 Project Highlights

```text
🇯🇵 40,000 Japanese Customer Records
             ↓
       Data Preparation
             ↓
       Feature Engineering
             ↓
    Logistic Regression
             ↓
      Model Evaluation
             ↓
🇮🇳 70,000 Indian Customer Records
             ↓
      Purchase Prediction
             ↓
 Potential Customer Estimate
```

---

# 🎓 Learning Outcomes

Through this project, I practiced how to:

* Work with real-world customer datasets
* Inspect and clean structured data
* Convert categorical variables into numerical features
* Process dates using Pandas
* Engineer new machine-learning features
* Detect and handle potential outliers
* Build a Logistic Regression classifier
* Scale features using StandardScaler
* Split data into training and validation sets
* Evaluate classification models
* Interpret model coefficients
* Apply a trained model to a different dataset
* Translate machine-learning results into a business context

---

# 🔮 Future Vision

This project can be extended from a Jupyter Notebook into a complete **Market Intelligence & Customer Prediction System**:

```text
Raw Customer Data
       ↓
Automated Data Pipeline
       ↓
Data Quality Checks
       ↓
Feature Engineering
       ↓
Multiple ML Models
       ↓
Model Evaluation
       ↓
Customer Scoring
       ↓
India Market Dashboard
       ↓
Business Decision Support
```

A future version could include an interactive dashboard using **Streamlit**, allowing business users to explore customer segments and potential market opportunities.

---

# 👩‍💻 Author

**Sandhya Shakya**

Aspiring Data Scientist | Python | Machine Learning | Data Analytics

---

# ⭐ Conclusion

The **ABG Motors Market Entry Analysis** project demonstrates how machine learning can be used to explore customer purchasing patterns and support market-entry analysis.

The project uses Japanese customer data containing historical purchase outcomes to train a Logistic Regression model and then applies the learned patterns to **70,000 Indian customer records** to estimate potential purchasers.

While the results should not be treated as definitive sales forecasts without India-specific validation, the project provides a strong foundation for **customer analytics, predictive modeling, and data-driven market analysis**.

> **Data → Insights → Predictions → Business Decisions 🚗📊🤖**

If you find this project useful, consider giving the repository a ⭐ on GitHub.

**Happy Learning & Happy Coding! 🚀**
