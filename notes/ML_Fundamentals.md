# 🧠 Machine Learning — Full Overview & Roadmap

> Interview-ready notes, organized by priority so you always know what to focus on next.

---

## 🗺️ The Big Picture — Where ML Fits in AI Engineering

```
 ┌─────────────────────────────┐
 │ 1. Python, math & data      │  ← Foundation (you've started this)
 │    numpy · pandas · stats   │
 └──────────────┬───────────────┘
                │
 ┌──────────────▼───────────────┐
 │ 2. CLASSIC ML  ★ FOCUS NOW ★ │  ← This file
 │    regression · trees · KNN │
 └──────────────┬───────────────┘
                │
 ┌──────────────▼───────────────┐
 │ 3. Evaluation & deployment   │  ← Makes models usable in real apps
 │    metrics · APIs · Docker  │
 └──────────────┬───────────────┘
                │
 ┌──────────────▼───────────────┐
 │ 4. Deep learning             │  ← Neural nets, CNNs, transformers
 └──────────────┬───────────────┘
                │
 ┌──────────────▼───────────────┐
 │ 5. LLM / GenAI engineering   │  ← Most "AI Engineer" jobs today
 │    RAG · embeddings · agents│
 └───────────────────────────────┘
```

**Is classic ML important?** Yes — non-negotiable. Every deep learning and LLM concept (loss functions, overfitting, train/test splits, precision/recall) is *inherited* from classic ML. Skipping it means you'll be able to copy-paste transformer code but won't understand why anything works. **Master phases 1–2 solidly before rushing to phase 4–5.**

---

## 🎯 Priority Legend

| Symbol | Meaning |
|:---:|---|
| 🔴 | Must know cold — comes up in almost every interview |
| 🟡 | Important — shows depth, expect follow-up questions |
| 🟢 | Good to know — mention if relevant, don't over-invest yet |

---

## 1. Core ML Concepts 🔴

### What is Machine Learning?
A computer program that **learns patterns from data** instead of being told exact rules. You give it examples, it figures out the logic itself.

> 💬 *"Instead of writing rules like `if age > 60: risky`, I give the model thousands of past examples and it learns the pattern on its own."*

### Supervised Learning 🔴
You give the model **input + correct answer** together. It learns the relationship so it can predict the answer for new, unseen inputs.

- **Example:** Predicting house prices — show 1000 houses with size, location, and actual sale price. Model learns the pattern, then predicts price for a new house.

### Unsupervised Learning 🟡
You give the model **only input data**, no correct answer. It finds hidden patterns or groups on its own.

- **Example:** A store grouping customers into segments (bargain hunters, premium buyers) — nobody labeled these groups; the algorithm discovered them.

### Regression vs Classification 🔴

| | Regression | Classification |
|---|---|---|
| Predicts | A continuous number | A category/label |
| Example | House price, temperature, salary | Spam vs Not Spam, Malignant vs Benign |

### Features & Labels 🔴
- **Features** — input variables/columns used to predict. Also called `X`. *Example: square footage, bedrooms, location.*
- **Labels** — the answer you're predicting. Also called `Y`. *Example: the actual sale price.*

> 🧩 **Quick recall:** Features = questions you ask. Label = the answer you want.

---

## 2. ML Algorithms 🔴

| Algorithm | Type | What it does | When to use |
|---|---|---|---|
| Linear Regression | Regression | Fits a line to predict a number | Straight-line relationship (price from size) |
| Logistic Regression | Classification | Predicts categories via probability | Simple binary problems (churn yes/no) |
| Decision Tree | Both | Yes/no question flowchart | Need something easy to explain |
| Random Forest | Both | Many trees, averaged vote | Want accuracy + less overfitting |
| K-Means | Unsupervised | Groups data into K clusters | No labels, want natural groupings |

### Plain-English Explanations

**Linear Regression** 🔴
Draws the "best fit line": `y = mx + b`. Minimizes distance between the line and all points (least squares).
> *"Like drawing a trend line through a scatter plot — assumes a straight-line relationship."*

**Logistic Regression** 🔴
Despite the name, it's for classification. Outputs a probability (0–1) via sigmoid, applies a threshold (usually 0.5).
> *"Gives me a probability, like 'this email is 87% likely spam,' and I pick the cutoff."*

**Decision Tree** 🔴
Asks yes/no questions on features — "Is age > 30? Is income > 50k?" — until it reaches a decision.
> *"A flowchart of questions that ends in a prediction. Very easy to visualize."*

**Random Forest** 🔴
Builds hundreds of slightly different trees, takes a majority vote or average, instead of trusting one tree.
> *"A team of decision trees voting together — reduces the risk of one tree overfitting."*

**K-Means** 🟡
Picks K random centers, assigns points to nearest center, moves centers to the average, repeats until stable.
> *"Groups data into K clusters by repeatedly moving cluster centers until stable."*

### Algorithm Comparison (quick recall) 🟡

| Algorithm | Supervised? | Output | Interpretable? | Overfitting risk |
|---|:---:|---|---|---|
| Linear Regression | Yes | Number | Very easy | Low |
| Logistic Regression | Yes | Probability | Very easy | Low |
| Decision Tree | Yes | Both | Very easy | High |
| Random Forest | Yes | Both | Medium | Low |
| K-Means | No | Clusters | Medium | N/A |

---

## 3. Train/Test Split & Preprocessing 🔴

### Train/Test Split
Never train and test on the same data — like giving a student the exam questions before the test.

- **Training set (70–80%)** — model learns from this
- **Test set (20–30%)** — model is evaluated on unseen data

> *"I split my data so the model is tested on unseen data — this tells me how it'll perform in the real world."*

### Scaling / Normalization 🟡
Distance-based (K-Means) and gradient-based (Logistic Regression) algorithms get confused when features have very different ranges (age 0–100 vs salary 0–1,000,000).

- **Normalization (Min-Max)** — squishes values between 0 and 1
- **Standardization (Z-score)** — mean = 0, std dev = 1

> *"Without scaling, a feature like salary would dominate the model just because its numbers are bigger."*

### Feature Engineering 🟡
Creating new, more useful features from raw data.
- **Example:** From "Date of Birth" → engineer "Age". From "Purchase Timestamp" → extract "Day of Week".

### Full Preprocessing Pipeline (in order) 🔴
1. Load the dataset
2. Handle missing values (fill or drop)
3. Encode categorical variables
4. Split into train/test sets
5. Scale/normalize numeric features
6. Train the model
7. Evaluate on test set

---

## 4. Model Evaluation 🔴

### Why not just use "Accuracy"?
Accuracy alone can mislead. If 95% of emails are "not spam," a lazy model that always predicts "not spam" gets 95% accuracy — but it's useless.

### Confusion Matrix

| | Predicted Positive | Predicted Negative |
|---|---|---|
| **Actual Positive** | ✅ True Positive (TP) | ❌ False Negative (FN) |
| **Actual Negative** | ❌ False Positive (FP) | ✅ True Negative (TN) |

- **TP** — correctly caught a spam email
- **TN** — correctly let a real email through
- **FP** — false alarm (real email marked spam)
- **FN** — missed it (spam email let through)

### The Metrics 🔴

| Metric | Formula | Use when... |
|---|---|---|
| **Accuracy** | (TP+TN)/Total | Classes are balanced |
| **Precision** | TP/(TP+FP) | False alarms are costly (spam) |
| **Recall** | TP/(TP+FN) | Missing a positive is costly (cancer detection) |
| **F1 Score** | 2×(P×R)/(P+R) | Need balance of both, imbalanced classes |
| **ROC-AUC** | Area under ROC curve | Overall separability, 1.0 = perfect, 0.5 = random |

> *"I choose the metric based on the business problem — recall for cancer detection, precision for spam detection, F1 when both matter."*

---

## 5. Common ML Problems 🔴

| Problem | What it means | Real-world analogy |
|---|---|---|
| **Overfitting** 🔴 | Memorizes training data, fails on new data | A student who memorizes last year's exact exam answers |
| **Underfitting** 🟡 | Too simple, fails on both train & test | Fitting a straight line to clearly curved data |
| **Regularization** 🟡 | Penalizes complexity to reduce overfitting (L1/L2) | Forcing the model to "keep it simple" |
| **Class Imbalance** 🟡 | One class dominates (95% not-fraud, 5% fraud) | Fixed via SMOTE, undersampling, class weights |
| **Cross-Validation** 🔴 | K-fold splits for more reliable performance estimates | Testing on every part of the data, not just one split |

> *"Cross-validation gives a more reliable performance estimate because every data point gets used for both training and testing at some point."*

---

## 6. 🎤 Interview Cheat Sheet (30-Second Answers)

| Question | Answer |
|---|---|
| Supervised vs unsupervised? | Supervised has labeled answers to learn from; unsupervised finds patterns without labels. |
| How do you know if overfitting? | Training accuracy high, test accuracy much lower — big gap. |
| Metric for imbalanced dataset? | F1 or precision/recall, not accuracy — accuracy can mislead. |
| Why scale features? | So larger-range features don't unfairly dominate the model. |
| What is cross-validation and why? | Tests the model on multiple splits for a more reliable estimate. |
| Random Forest vs Decision Tree? | Random Forest = many trees combined, averaging out individual mistakes. |

---

## 7. 🏗️ End-to-End ML Pipeline (Project Structure)

Use this exact flow for a Customer Churn / Credit Risk project:

1. **EDA** — understand data, distributions, missing values, correlations
2. **Cleaning** — handle nulls, remove duplicates, fix data types
3. **Feature Engineering** — create columns, encode categoricals
4. **Train/Test Split** — separate data before touching the model
5. **Preprocessing** — scale numeric features
6. **Train Multiple Models** — Logistic Regression, Decision Tree, Random Forest
7. **Compare Models** — Accuracy, Precision, Recall, F1
8. **Evaluate Best Model** — confusion matrix, ROC-AUC on test set
9. **Prediction** — use final model on new/unseen data
10. **Document in README** — problem statement, approach, results, conclusion

> 💬 *"I built an end-to-end churn prediction pipeline — did EDA to understand drivers of churn, engineered features, trained and compared Logistic Regression, Decision Tree, and Random Forest, and selected the best model using F1 score since the classes were imbalanced."*

---

## 8. 📍 What to Focus on Next (After This File)

Once 🔴 items above feel automatic (you can explain them without notes):

1. **Model deployment basics** — wrap a trained model in a FastAPI endpoint, containerize with Docker
2. **Deep learning fundamentals** — perceptrons → neural nets → why backprop works
3. **LLM engineering track** — embeddings, vector databases, RAG, prompt engineering, agents

This is the track most "AI Engineer" roles actually test today — classic ML gets you in the door and gives you the vocabulary; the LLM/GenAI layer is where the current job demand is concentrated.