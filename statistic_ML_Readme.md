# 📊 Statistics & Machine Learning with Python

A comprehensive Python and Jupyter Notebook project covering fundamental concepts of **Statistics, Machine Learning, Dimensionality Reduction, and Natural Language Processing (NLP)** through practical examples and implementations.

This repository is designed as a hands-on learning project, progressing from basic statistical concepts to machine-learning algorithms and NLP preprocessing techniques.

---

## 📌 Overview

The notebook covers the following major areas:

```text
Statistics
   ↓
Sampling
   ↓
Hypothesis Testing
   ↓
Machine Learning
   ↓
Supervised Learning
   ↓
Unsupervised Learning
   ↓
Dimensionality Reduction
   ↓
NLP
```

The project combines mathematical concepts with Python implementations using libraries such as **NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn, and NLTK**.

---

# 📂 Project Structure

```text
.
├── statistics and ML.ipynb
└── README.md
```

---

# 🛠️ Technologies & Libraries

The notebook uses:

| Technology / Library | Purpose                     |
| -------------------- | --------------------------- |
| 🐍 Python            | Programming language        |
| 📓 Jupyter Notebook  | Interactive development     |
| 🔢 NumPy             | Numerical computation       |
| 🐼 Pandas            | Data manipulation           |
| 📊 Matplotlib        | Data visualization          |
| 📈 Seaborn           | Statistical visualization   |
| 🤖 Scikit-learn      | Machine learning            |
| 📝 NLTK              | Natural Language Processing |
| 🔤 Regex (`re`)      | Text cleaning               |

The notebook imports NumPy, Pandas, Statistics, Matplotlib, and later introduces Scikit-learn and NLTK functionality.

---

# 1️⃣ Statistics

The first section introduces fundamental descriptive-statistics concepts using Python.

---

## Mean

The notebook calculates the mean of a collection of marks using NumPy:

```python
marks = [23, 32, 11, 22, 12, 45]

avg_val = np.mean(marks)

print(avg_val)
```

### Concept

The mean is calculated as:

```text
Mean = Sum of all values / Number of values
```

---

## Median

The notebook calculates the median of an age dataset:

```python
age = [34, 23, 35, 53, 21, 32]

med_val = np.median(age)

print(med_val)
```

The median represents the middle value after the observations are ordered.

---

## Mode

The notebook uses Python's `statistics` module to calculate the mode:

```python
from statistics import mode

mode_val = mode(num)

print(mode_val)
```

The mode represents the most frequently occurring value.

---

## Range

The range is calculated using the maximum and minimum values:

```python
highest_val = np.max(salary)
lowest_val = np.min(salary)

range_val = highest_val - lowest_val
```

Conceptually:

```text
Range = Maximum − Minimum
```

---

# 2️⃣ Variance

The notebook calculates variance using NumPy:

```python
var_val = np.var(marks)

print(var_val)
```

Variance measures how spread out values are from their mean.

The notebook also calculates:

```python
np.mean(marks)
np.sum(marks)
```

to connect the concepts of mean, total, and variance.

---

# 3️⃣ Standard Deviation

Standard deviation is calculated using:

```python
std_val = np.std(marks)

print(std_val)
```

Standard deviation describes the typical amount of variation in the dataset.

Conceptually:

```text
Low Standard Deviation
        ↓
Values are closer together

High Standard Deviation
        ↓
Values are more spread out
```

---

# 4️⃣ Percentiles & Quartiles

The notebook introduces percentiles using:

```python
np.percentile(data, ...)
```

For example:

```python
q1 = np.percentile(data, 25)
```

Percentiles help understand where a particular value lies within a distribution.

The notebook also demonstrates quartile-related calculations and later uses the first and third quartiles to calculate the IQR.

---

# 5️⃣ Interquartile Range — IQR

The notebook calculates the Interquartile Range:

```python
q1 = np.percentile(salary, 25)
q3 = np.percentile(salary, 75)

IQR = q3 - q1
```

The formula is:

```text
IQR = Q3 − Q1
```

The notebook then calculates lower and upper bounds using:

```python
lower_bound = q1 - 1.5 * IQR
upper_bound = q3 + 1.5 * IQR
```

These boundaries can be used to identify potential outliers.

---

# 6️⃣ Box Plot

The salary dataset is visualized using a box plot:

```python
plt.boxplot(salary)

plt.title("salary boxplot")

plt.show()
```

A box plot provides a visual representation of:

* Median
* Quartiles
* Interquartile range
* Potential outliers

---

# 7️⃣ Sampling Techniques

The notebook introduces different sampling methods.

---

## Random Sampling

Random sampling selects observations randomly from a population.

The notebook demonstrates this using:

```python
population = np.arange(1, 1000)

sample = np.random.choice(
    population,
    50
)
```

The example illustrates selecting a subset from a larger population.

---

## Systematic Sampling

Systematic sampling selects observations at regular intervals.

The notebook demonstrates this using NumPy ranges and fixed intervals.

Conceptually:

```text
Population
    ↓
Choose starting point
    ↓
Select every k-th observation
    ↓
Sample
```

---

## Stratified Sampling

The notebook introduces stratified sampling using groups such as:

```text
Engineering
Arts
Management
Medical
```

The objective is to ensure that different groups are represented in the sample.

---

## Cluster Sampling

The notebook also introduces cluster sampling.

The example considers a hierarchy such as:

```text
City
  ↓
Districts
  ↓
People
```

The idea is to select groups or clusters rather than independently selecting every individual.

---

# 8️⃣ Population vs Sample

The notebook includes an example comparing population and sample means:

```python
pop = [5, 6, 3, 5, 8, 7]

p_mean = 5.6

sam = [6, 5]

s_mean = 5.5
```

This introduces the relationship between:

```text
Population
   ↓
Sample
   ↓
Sample Statistics
```

---

# 9️⃣ Hypothesis Testing

The notebook introduces **Hypothesis Testing**.

It explains two major hypotheses:

### Null Hypothesis — H₀

The null hypothesis generally represents:

```text
No effect
or
No difference
```

The notebook gives an example involving average delivery time:

```text
Average delivery time = 30 minutes
```

### Alternative Hypothesis — H₁

The alternative hypothesis represents a difference or effect.

For example:

```text
Average delivery time ≠ 30 minutes
```

This section provides the conceptual foundation for statistical hypothesis testing.

---

# 🤖 10️⃣ Machine Learning

The notebook then transitions from statistics to machine learning.

It explains the difference between traditional programming and machine learning.

### Traditional Programming

```text
Input + Rules
     ↓
   Output
```

### Machine Learning

```text
Input Data + Labels
        ↓
      Model
        ↓
   Predictions
```

This introduces the fundamental idea of learning patterns from data.

---

# 1️⃣1️⃣ Input & Output

The notebook introduces the basic machine-learning relationship:

```text
f(X) = Y
```

where:

```text
X → Input / Features

Y → Output / Target
```

This concept is used throughout the supervised-learning examples.

---

# 📈 12️⃣ Linear Regression

The first machine-learning implementation demonstrates **Linear Regression**.

The notebook creates a small synthetic dataset:

```python
X = np.array([
    [10], [20], [80], [30], [100],
    [40], [90], [50], [60], [70]
])

Y = np.array([
    100, 400, 6400, 900, 10000,
    1600, 8100, 2500, 3600, 4900
])
```

The data is then divided into training and testing sets.

---

## Train-Test Split

The notebook uses:

```python
X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)
```

This creates:

```text
80% → Training data
20% → Testing data
```

---

## Model Training

The notebook uses `LinearRegression`:

```python
model = LinearRegression()

model.fit(
    X_train,
    Y_train
)
```

---

## Prediction

Predictions are generated using:

```python
Y_pred = model.predict(X_test)
```

---

# 📊 Linear Regression Evaluation

The notebook evaluates the regression model using:

* MAE
* MSE
* RMSE
* R² Score

The implementation includes:

```python
mae = mean_absolute_error(Y_test, Y_pred)

mse = mean_squared_error(Y_test, Y_pred)

rmse = root_mean_squared_error(Y_test, Y_pred)

r2 = r2_score(Y_test, Y_pred)
```

---

## Evaluation Metrics

### MAE — Mean Absolute Error

Measures the average absolute difference between actual and predicted values.

```text
MAE = Average |Actual − Predicted|
```

### MSE — Mean Squared Error

Squares the prediction errors before averaging them.

```text
MSE = Average (Actual − Predicted)²
```

### RMSE — Root Mean Squared Error

The square root of MSE:

```text
RMSE = √MSE
```

### R² Score

Measures how well the regression model explains variation in the target.

---

# 🔐 13️⃣ Logistic Regression

The notebook then introduces **Logistic Regression** for classification.

It explains the concept of a confusion matrix.

---

# 🧩 Confusion Matrix

The notebook presents the four fundamental outcomes:

```text
                  Predicted
                 +         -
              ┌───────┬───────┐
Actual    +   │  TP   │  FN   │
              ├───────┼───────┤
          -   │  FP   │  TN   │
              └───────┴───────┘
```

Where:

```text
TP → True Positive
TN → True Negative
FP → False Positive
FN → False Negative
```

---

# 📐 Classification Metrics

The notebook explains four important classification metrics.

---

## Accuracy

```text
Accuracy =
(TP + TN)
────────────────────────
TP + TN + FP + FN
```

Accuracy measures overall correctness.

The notebook also highlights that accuracy can be misleading when a dataset is imbalanced.

---

## Precision

```text
Precision =
TP
────────
TP + FP
```

Precision answers:

> Of all predicted positive cases, how many were actually positive?

---

## Recall

```text
Recall =
TP
────────
TP + FN
```

Recall answers:

> Of all actual positive cases, how many were correctly identified?

---

## F1 Score

```text
F1 =
2 × Precision × Recall
──────────────────────
Precision + Recall
```

F1 score balances precision and recall.

---

# 💻 Logistic Regression Implementation

The notebook creates a simple classification dataset:

```python
X = np.array([
    [40], [30], [100], [80], [60],
    [90], [50], [20], [10], [70]
])

y = np.array([
    0, 0, 1, 1, 1,
    1, 1, 0, 0, 1
])
```

The labels represent:

```text
0 → Fail
1 → Pass
```

The data is divided into training and testing sets:

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

The Logistic Regression model is then trained:

```python
model = LogisticRegression()

model.fit(
    X_train,
    y_train
)
```

Predictions are generated using:

```python
y_pred = model.predict(X_test)
```

---

# 📊 Logistic Regression Evaluation

The notebook calculates:

```python
cm = confusion_matrix(y_test, y_pred)

acc = accuracy_score(y_test, y_pred)

pre = precision_score(y_test, y_pred)

rec = recall_score(y_test, y_pred)

f1 = f1_score(y_test, y_pred)
```

This provides a practical demonstration of evaluating a classification model.

---

# ⚠️ 14️⃣ Model Errors

The notebook introduces model error and possible causes, including:

* Poor data
* Wrong model choice
* Improper training
* Noise in the data

It then discusses different model behaviors.

---

# ⚖️ 15️⃣ Bias-Variance Tradeoff

The notebook introduces the **Bias-Variance Tradeoff**.

### Bias

Bias is described as error caused by incorrect assumptions.

```text
High Bias
    ↓
Model is too simple
```

### Variance

Variance describes sensitivity to the training data.

```text
High Variance
    ↓
Model is too sensitive / complex
```

The goal is to find an appropriate balance between bias and variance.

---

# 📉 16️⃣ Underfitting vs Overfitting

The notebook compares training and testing errors to explain:

### Underfitting

```text
Training Error → High
Test Error     → High
```

The model is too simple to capture the underlying pattern.

### Overfitting

```text
Training Error → Low
Test Error     → High
```

The model performs very well on training data but poorly on unseen data.

---

# ⚙️ 17️⃣ Model Optimization

The notebook introduces **feature engineering** as an optimization technique.

For date-related data, examples include extracting:

```text
Year
Quarter
Month
Week
Day
```

It also introduces the concept of rolling calculations for time-series-style data.

---

# 🔍 18️⃣ Unsupervised Learning

The notebook then moves to **Unsupervised Learning**.

Unlike supervised learning:

```text
Supervised Learning
Input + Labels
      ↓
    Model
      ↓
 Prediction
```

Unsupervised learning works with:

```text
Input Data
    ↓
   Model
    ↓
Hidden Structure
```

There are no predefined target labels.

---

# 🧩 Types of Unsupervised Learning

The notebook introduces:

### Clustering

Grouping similar observations together.

### Association Rule Learning

Finding relationships between variables.

### Dimensionality Reduction

Reducing the number of features while attempting to preserve useful information.

---

# 🔵 19️⃣ K-Means Clustering

The notebook implements **K-Means Clustering** using Scikit-learn.

Synthetic data is generated using:

```python
from sklearn.datasets import make_blobs

X, y = make_blobs(
    n_samples=500,
    centers=6,
    cluster_std=0.6,
    random_state=42
)
```

The raw data is visualized using a scatter plot.

---

## Applying K-Means

The notebook creates a K-Means model:

```python
kmeans = KMeans(
    n_clusters=3,
    random_state=42
)

kmeans.fit(X)
```

The cluster labels are retrieved using:

```python
labels = kmeans.labels_
```

and the cluster centers using:

```python
centeroid = kmeans.cluster_centers_
```

---

# 📊 K-Means Visualization

The clusters and centroids are visualized:

```python
plt.scatter(
    X[:, 0],
    X[:, 1],
    c=labels
)

plt.scatter(
    centeroid[:, 0],
    centeroid[:, 1],
    marker="x",
    s=200
)
```

This provides a visual representation of the discovered clusters.

---

# 📐 20️⃣ Elbow Method

The notebook demonstrates the **Elbow Method** for evaluating different values of `K`.

It calculates Within-Cluster Sum of Squares using:

```python
wcss = []

for i in range(1, 11):
    kmeans = KMeans(
        n_clusters=i,
        random_state=42
    )

    kmeans.fit(X)

    wcss.append(kmeans.inertia_)
```

The resulting WCSS values are plotted against the number of clusters.

The elbow point can help identify a reasonable value of `K`.

---

# 📉 21️⃣ Dimensionality Reduction

The notebook introduces dimensionality reduction.

It explains that real-world datasets can contain many features.

Examples mentioned include:

```text
Customer Analytics → 100+ features
NLP Embeddings     → 300–768 features
Image Data         → Thousands of pixels
```

Large numbers of features can increase:

* Computational cost
* Storage requirements
* Model complexity
* Difficulty in visualization

---

# 🧠 22️⃣ Principal Component Analysis — PCA

The notebook introduces **Principal Component Analysis (PCA)**.

PCA creates new features called:

```text
Principal Components
```

The basic PCA workflow demonstrated is:

```text
Original Data
     ↓
Mean Centering
     ↓
Covariance Matrix
     ↓
Eigen Decomposition
     ↓
Sort Eigenvalues
     ↓
Select Top Components
     ↓
Projection
     ↓
Reduced Data
```

---

# 🔢 PCA From Scratch

The notebook implements PCA step by step.

---

## Step 1 — Mean Centering

```python
X_mean = np.mean(X, axis=0)

X_centered = X - X_mean
```

The data is centered around its mean.

---

## Step 2 — Covariance Matrix

```python
cov_matrix = np.cov(
    X_centered.T
)
```

The covariance matrix describes relationships between features.

---

## Step 3 — Eigen Decomposition

```python
eigenvalues, eigenvectors = np.linalg.eig(
    cov_matrix
)
```

This produces eigenvalues and eigenvectors.

---

## Step 4 — Sort Eigenvalues

```python
sorted_index = np.argsort(
    eigenvalues
)[::-1]
```

The eigenvalues are sorted from largest to smallest.

---

## Step 5 — Select Top Components

The notebook selects the top component:

```python
k = 1

w = sorted_eigenvectors[:, :k]
```

---

## Step 6 — Projection

The centered data is projected onto the selected component:

```python
X_reduced = np.dot(
    X_centered,
    w
)
```

The notebook compares:

```text
Original shape
Reduced shape
```

to demonstrate dimensionality reduction.

---

# 🌸 23️⃣ PCA on Iris Dataset

The notebook also applies PCA to a real dataset using Scikit-learn.

It loads the Iris dataset:

```python
from sklearn.datasets import load_iris

data = load_iris()

X = data.data
y = data.target
```

---

## Feature Scaling

The features are standardized using:

```python
from sklearn.preprocessing import StandardScaler

X_scaled = StandardScaler().fit_transform(X)
```

---

## PCA Transformation

PCA is then applied with two components:

```python
from sklearn.decomposition import PCA

pca = PCA(
    n_components=2
)

X_reduced = pca.fit_transform(
    X_scaled
)
```

The notebook displays:

* Original shape
* Reduced shape
* Explained variance ratio

---

# 📊 Explained Variance

The notebook also demonstrates information retention using values:

```text
72.96%
22.85%
```

and calculates:

```text
Information Carry = 72.96 + 22.85
```

followed by the remaining information loss.

This illustrates how PCA components can retain a large portion of the original information while reducing dimensionality.

---

# 📝 24️⃣ Natural Language Processing — NLP

The final major section introduces **Natural Language Processing**.

The notebook presents an NLP pipeline:

```text
Raw Text
   ↓
Cleaning
   ↓
Tokenization
   ↓
Normalization
   ↓
Vectorization
   ↓
Model
```

---

# 🧹 Text Cleaning

The notebook uses the Python `re` module.

Example text:

```python
text = " I love @ Spicy # FOOd !!; so MUch "
```

The text is converted to lowercase:

```python
text = text.lower()
```

Punctuation is removed using:

```python
cln_text = re.sub(
    r'[^\w\s]',
    "",
    text
)
```

This demonstrates basic text normalization.

---

# 🔤 25️⃣ Tokenization

The notebook uses NLTK's `word_tokenize()`:

```python
from nltk.tokenize import word_tokenize

token = word_tokenize(cln_text)
```

The notebook also downloads the required NLTK tokenizer resources.

Tokenization converts text into individual tokens.

Example:

```text
"I love spicy food"
        ↓
["I", "love", "spicy", "food"]
```

---

# 🛑 26️⃣ Stop Words

The notebook removes English stop words using NLTK:

```python
from nltk.corpus import stopwords

stop_words = set(
    stopwords.words('english')
)
```

Filtered tokens are created using a list comprehension.

Stop words are common words that may carry relatively little useful information for some NLP tasks.

---

# 🌱 27️⃣ Stemming

The notebook introduces stemming with `PorterStemmer`:

```python
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
```

It demonstrates stemming on words such as:

```text
Playing
Played
Singing
Cooking
Dancing
Bathing
```

Stemming attempts to reduce words to a common root form.

---

# 🌳 28️⃣ Lemmatization

The notebook also demonstrates lemmatization using:

```python
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
```

Unlike simple stemming, lemmatization attempts to produce meaningful base forms.

---

# 👜 29️⃣ Bag of Words — BOW

The notebook introduces the **Bag of Words** approach using:

```python
from sklearn.feature_extraction.text import CountVectorizer
```

Example documents include:

```text
I Love NLP
I Like Python
I Love Spicy Food
I Like Horror Movies
```

`CountVectorizer` converts text into numerical feature representations based on word counts.

Conceptually:

```text
Text
 ↓
Vocabulary
 ↓
Word Counts
 ↓
Numerical Matrix
```

---

# 📐 30️⃣ TF-IDF

The notebook then introduces **TF-IDF — Term Frequency-Inverse Document Frequency**.

It uses:

```python
from sklearn.feature_extraction.text import TfidfVectorizer
```

TF-IDF assigns importance to words based on their frequency within documents and their frequency across the collection of documents.

Conceptually:

```text
TF-IDF
  │
  ├── Term Frequency
  │
  └── Inverse Document Frequency
```

---

# 🔗 31️⃣ Machine Learning Pipeline for NLP

The notebook begins building a small NLP machine-learning pipeline using:

```python
from sklearn.linear_model import LogisticRegression

from sklearn.pipeline import Pipeline

from sklearn.model_selection import train_test_split
```

This connects text processing and machine learning:

```text
Raw Text
   ↓
Text Vectorization
   ↓
Logistic Regression
   ↓
Prediction
```

---

# 📦 Required Installation

Install the main Python packages with:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn nltk
```

The notebook itself also contains installation commands for:

```bash
pip install nltk
pip install bs4
pip install requests
```

The `bs4` and `requests` installations occur near the end of the notebook.

---

# ▶️ How to Run

## 1. Clone the Repository

```bash
git clone <your-repository-url>
```

## 2. Navigate to the Project

```bash
cd <repository-name>
```

## 3. Install Dependencies

```bash
pip install numpy pandas matplotlib seaborn scikit-learn nltk beautifulsoup4 requests
```

## 4. Start Jupyter Notebook

```bash
jupyter notebook
```

## 5. Open the Notebook

Open:

```text
statistics and ML.ipynb
```

Run the notebook cells sequentially.

---

# ⚠️ NLTK Resources

Some NLP examples require NLTK resources.

The notebook downloads resources including:

```python
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
```

Run these downloads before executing the corresponding NLP cells if the resources are not already installed.

---

# 📊 Complete Topic Map

| Section                     | Concepts                                 |
| --------------------------- | ---------------------------------------- |
| 📊 Statistics               | Mean, Median, Mode, Range                |
| 📈 Dispersion               | Variance, Standard Deviation             |
| 📐 Distribution             | Percentiles, Quartiles, IQR              |
| 📦 Visualization            | Box Plot                                 |
| 🎲 Sampling                 | Random, Systematic, Stratified, Cluster  |
| 🧪 Statistics               | Population vs Sample                     |
| 🔬 Hypothesis Testing       | H₀ and H₁                                |
| 🤖 ML Fundamentals          | Features, Labels, Models                 |
| 📈 Regression               | Linear Regression                        |
| 📊 Regression Metrics       | MAE, MSE, RMSE, R²                       |
| 🔐 Classification           | Logistic Regression                      |
| 🧩 Classification Metrics   | Accuracy, Precision, Recall, F1          |
| ⚠️ Model Behavior           | Bias, Variance                           |
| 📉 Model Problems           | Underfitting, Overfitting                |
| ⚙️ Optimization             | Feature Engineering                      |
| 🔵 Clustering               | K-Means                                  |
| 📐 Clustering Optimization  | Elbow Method                             |
| 📉 Dimensionality Reduction | PCA                                      |
| 🧮 PCA                      | Mean Centering, Covariance, Eigenvectors |
| 🌸 Dataset                  | Iris                                     |
| 📝 NLP                      | Text Cleaning                            |
| 🔤 NLP                      | Tokenization                             |
| 🛑 NLP                      | Stop Words                               |
| 🌱 NLP                      | Stemming                                 |
| 🌳 NLP                      | Lemmatization                            |
| 👜 NLP                      | Bag of Words                             |
| 📊 NLP                      | TF-IDF                                   |
| 🔗 NLP + ML                 | Pipeline + Logistic Regression           |

---

# 🎯 Learning Objectives

After completing this notebook, you should have practical exposure to:

### Statistics

* Calculate mean, median, and mode
* Understand range and variance
* Calculate standard deviation
* Work with percentiles and quartiles
* Calculate IQR
* Identify potential outliers
* Understand sampling techniques
* Understand basic hypothesis testing

### Machine Learning

* Understand supervised learning
* Split datasets into training and testing sets
* Train regression models
* Evaluate regression models
* Train classification models
* Interpret confusion matrices
* Calculate classification metrics
* Understand bias and variance
* Recognize underfitting and overfitting

### Unsupervised Learning

* Understand clustering
* Apply K-Means
* Analyze cluster centers
* Use the Elbow Method

### Dimensionality Reduction

* Understand the purpose of PCA
* Mean-center data
* Calculate covariance matrices
* Perform eigen decomposition
* Select principal components
* Project data into lower dimensions
* Apply PCA using Scikit-learn

### NLP

* Clean text
* Tokenize text
* Remove stop words
* Apply stemming
* Apply lemmatization
* Convert text into numerical features
* Understand Bag of Words
* Understand TF-IDF
* Build an NLP pipeline

---

# 🔄 Overall Learning Journey

```text
                  Python
                    │
                    ▼
              Statistics
                    │
       ┌────────────┴────────────┐
       ▼                         ▼
   Sampling               Hypothesis Testing
       │
       └────────────┬────────────┘
                    ▼
            Machine Learning
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
     Supervised          Unsupervised
          │                   │
     ┌────┴────┐          ┌───┴────┐
     ▼         ▼          ▼        ▼
 Regression Classification K-Means  PCA
     │         │
     ▼         ▼
  Metrics   Confusion Matrix
              │
              ▼
          NLP
              │
      ┌───────┴────────┐
      ▼                ▼
 Text Processing   Vectorization
      │                │
      ▼                ▼
 Tokenization      BOW / TF-IDF
      │                │
      └───────┬────────┘
              ▼
         ML Pipeline
```

---

# 🚀 Possible Improvements

This notebook is primarily a learning project. It could be expanded by:

### Statistics

* Add probability distributions
* Add confidence intervals
* Implement t-tests
* Implement chi-square tests
* Add correlation analysis

### Machine Learning

* Add cross-validation
* Add hyperparameter tuning
* Compare multiple regression models
* Compare multiple classification algorithms
* Add ROC-AUC analysis
* Add classification reports
* Add model visualization

### K-Means

* Experiment with different datasets
* Automatically determine an appropriate `K`
* Compare Silhouette Score with the Elbow Method

### PCA

* Visualize principal components
* Plot cumulative explained variance
* Compare different numbers of components

### NLP

* Add text classification datasets
* Add sentiment analysis
* Add n-grams
* Add TF-IDF + model evaluation
* Add confusion-matrix visualization
* Build a complete text-classification application

---

# ⚠️ Project Scope

This repository is primarily intended for **learning and experimentation**.

The notebook contains small, manually created datasets for demonstrating machine-learning concepts, as well as Scikit-learn's built-in datasets such as Iris.

The examples should therefore be viewed as educational implementations rather than production-ready machine-learning systems.

---

# 💡 Key Takeaways

This project demonstrates an important progression:

```text
Understand Data
      ↓
Describe Data
      ↓
Sample Data
      ↓
Test Assumptions
      ↓
Build ML Models
      ↓
Evaluate Models
      ↓
Discover Hidden Patterns
      ↓
Reduce Dimensions
      ↓
Process Text
      ↓
Build NLP Models
```

The notebook connects **statistical thinking** with **machine-learning workflows**, making it useful as a foundation for further study in data science and artificial intelligence.

---

# 👩‍💻 Author

**Sandhya Shakya**

Python | Data Science | Machine Learning | AI

---

# ⭐ Conclusion

**Statistics & Machine Learning with Python** is a hands-on learning repository covering a wide range of foundational data-science concepts.

From calculating a simple mean and standard deviation to implementing **Linear Regression, Logistic Regression, K-Means, PCA, and NLP preprocessing**, the project provides practical exposure to the core ideas used in modern data science.

> **Learn the statistics → Understand the data → Build the model → Evaluate the results → Keep experimenting. 🚀🐍📊**

If you find the repository useful, consider giving it a ⭐ on GitHub.

**Happy Learning & Happy Coding!**
