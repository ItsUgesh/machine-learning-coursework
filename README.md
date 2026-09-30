# Machine Learning Coursework

A collection of machine learning projects, I am doing at Arden University. Each project covers the full workflow: loading data, exploring it, cleaning it, building a model, and evaluating the results.

**Author:** Ugesh · [LinkedIn](https://www.linkedin.com/in/Ugeshsimkhada) · [Email](mailto:ugeshsimkhada.com)

---

## Projects

| Project | Type | Notebook |
|---|---|---|
| Heart Attack Prediction | Binary classification | [`heart_attack_logistic_regression.ipynb`](heart_attack_logistic_regression.ipynb) |
| Social Media, Dopamine & Productivity | Exploratory data analysis | [`exploratory_data_analysis.ipynb`](exploratory_data_analysis.ipynb) |
| EA Sports FC27 Player Ratings | Exploratory data analysis | [`exploratory_data_analysis.ipynb`](exploratory_data_analysis.ipynb) |

### 1. Heart Attack Prediction

**Goal:** Predict whether a patient's record indicates a heart attack from clinical measurements.

- **Features:** Age, heart rate, systolic and diastolic blood pressure, blood sugar, CK-MB, troponin
- **Model:** Logistic regression (scikit-learn)
- **Method:** 80/20 train-test split, feature standardization with `StandardScaler`
- **Evaluation:** Accuracy, precision, recall, F1-score, and a confusion matrix heatmap
- **Result:** Accuracy of **[XX%]** on the held-out test set

### 2. Social Media, Dopamine & Productivity

**Goal:** Explore how social media habits relate to self-reported productivity.

- Inspected the structure, column types, and value distributions
- Measured data quality: missing values (as a share of all cells) and duplicate rows
- Summarized productivity self-ratings and screen-time variables
- **Key finding:** [one sentence on what you found]

### 3. EA Sports FC27 Player Ratings

**Goal:** Explore a large football player dataset to understand rating and position patterns.

- Summarized overall ratings and player positions
- Measured data quality: missing values and duplicate rows
- **Key finding:** [one sentence on what you found]

---

## Tech Stack

- **Language:** Python 3
- **Libraries:** pandas, NumPy, scikit-learn, Matplotlib, Seaborn
- **Tools:** Jupyter Notebooks, GitHub Codespaces, Kaggle API, Git

---

## Repository Structure

```
machine-learning-coursework/
├── heart_attack_logistic_regression.ipynb
├── exploratory_data_analysis.ipynb
├── requirements.txt
├── data/            # datasets (not tracked by Git, see below)
├── .gitignore
└── README.md
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ItsUgesh/machine-learning-coursework.git
cd machine-learning-coursework
```

You can also open it directly in **GitHub Codespaces** (Code → Codespaces → Create codespace on main).

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Download the datasets

Datasets are not stored in this repository. They are downloaded from Kaggle when needed.

1. Create a Kaggle API token at [kaggle.com/settings](https://www.kaggle.com/settings).
2. Store it as an environment variable named `KAGGLE_TOKEN`. In GitHub Codespaces, add it under **Settings → Codespaces → Secrets**.
3. Download each dataset into the `data/` folder:

```bash
kaggle datasets download -d <owner>/<dataset-name> -p data --unzip
```

| Dataset | Source |
|---|---|
| Heart Attack – Medical Dataset | [Kaggle link](https://www.kaggle.com/datasets/) |
| Social Media Dopamine & Productivity | [Kaggle link](https://www.kaggle.com/datasets/) |
| EA Sports FC27 Player Ratings | [Kaggle link](https://www.kaggle.com/datasets/) |

### 4. Run the notebooks

Open any `.ipynb` file in VS Code, Codespaces, or Jupyter and run the cells from top to bottom.

---

## Skills Demonstrated

- Data loading, inspection, and quality checks
- Handling missing values and duplicates
- Feature selection and scaling
- Training and evaluating classification models
- Data visualization
- Reproducible project setup with Git, `.gitignore`, and `requirements.txt`
- Secure handling of API credentials with environment variables

---

## Future Improvements

- Compare additional models (random forest, gradient boosting) against logistic regression
- Add cross-validation and hyperparameter tuning
- Add more visualizations and feature-importance analysis

---

## About Me

I'm a student building practical skills in machine learning and data analysis. I'm open to internships and entry-level roles in data science and machine learning.

📫 **Contact:** [your.email@example.com](mailto:your.email@example.com) · [LinkedIn](https://www.linkedin.com/in/your-profile)
