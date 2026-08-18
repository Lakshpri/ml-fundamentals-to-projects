<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ML Fundamentals to Projects</title>

    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: Arial, sans-serif;
            background: #0f172a;
            color: #e2e8f0;
            line-height: 1.6;
        }

        header {
            text-align: center;
            padding: 70px 20px;
            background: linear-gradient(135deg, #1e293b, #312e81);
        }

        header h1 {
            font-size: 42px;
            margin-bottom: 10px;
        }

        header p {
            font-size: 18px;
            color: #cbd5e1;
        }

        .container {
            max-width: 1000px;
            margin: auto;
            padding: 40px 20px;
        }

        .flow {
            text-align: center;
            font-size: 20px;
            margin: 30px 0;
            padding: 20px;
            background: #1e293b;
            border-radius: 15px;
        }

        .flow span {
            color: #818cf8;
            font-weight: bold;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 20px;
            margin-top: 25px;
        }

        .card {
            background: #1e293b;
            padding: 25px;
            border-radius: 15px;
            transition: 0.3s;
            border: 1px solid #334155;
        }

        .card:hover {
            transform: translateY(-8px);
            border-color: #818cf8;
        }

        .card h3 {
            margin-bottom: 10px;
            color: #a5b4fc;
        }

        .project {
            margin-top: 40px;
            padding: 30px;
            background: #1e293b;
            border-radius: 18px;
            border-left: 5px solid #818cf8;
        }

        .project h2 {
            color: #a5b4fc;
            margin-bottom: 15px;
        }

        ul {
            padding-left: 20px;
        }

        li {
            margin: 7px 0;
        }

        footer {
            text-align: center;
            padding: 30px;
            color: #94a3b8;
        }

        .badge {
            display: inline-block;
            margin: 5px;
            padding: 7px 12px;
            border-radius: 20px;
            background: #312e81;
            color: white;
            font-size: 14px;
        }
    </style>
</head>

<body>

<header>
    <h1>🤖 ML Fundamentals → Projects</h1>
    <p>From Python & Data → Machine Learning → Real-World Project</p>
</header>

<div class="container">

    <div class="flow">
        📚 Learn
        <span>→</span>
        💻 Code
        <span>→</span>
        🛠️ Build
        <span>→</span>
        📝 Document
        <span>→</span>
        🚀 Deploy
        <span>→</span>
        🎤 Explain
    </div>

    <h2>📌 What I Covered</h2>

    <div class="grid">

        <div class="card">
            <h3>🐍 Python</h3>
            <p>Python fundamentals required for Machine Learning.</p>
        </div>

        <div class="card">
            <h3>🔢 NumPy</h3>
            <p>Arrays, mathematical operations and numerical computing.</p>
        </div>

        <div class="card">
            <h3>🐼 Pandas</h3>
            <p>Data loading, cleaning, transformation and analysis.</p>
        </div>

        <div class="card">
            <h3>📊 Visualization</h3>
            <p>Exploratory Data Analysis using charts and graphs.</p>
        </div>

        <div class="card">
            <h3>🧠 ML Fundamentals</h3>
            <p>Supervised, unsupervised learning, features, labels and evaluation.</p>
        </div>

        <div class="card">
            <h3>⚙️ ML Algorithms</h3>
            <p>Regression, classification, decision trees, random forests and clustering.</p>
        </div>

        <div class="card">
            <h3>🔬 Scikit-learn</h3>
            <p>Preprocessing, pipelines, cross-validation and model evaluation.</p>
        </div>

        <div class="card">
            <h3>🎯 Model Evaluation</h3>
            <p>Accuracy, Precision, Recall, F1-score, ROC-AUC and Confusion Matrix.</p>
        </div>

    </div>

    <div class="project">

        <h2>🚢 End-to-End Project: Titanic Survival Prediction</h2>

        <p>
            Built a complete Machine Learning project using the Titanic dataset.
        </p>

        <br>

        <ul>
            <li>🔍 Exploratory Data Analysis</li>
            <li>🧹 Data Cleaning & Missing Value Handling</li>
            <li>⚙️ Feature Engineering</li>
            <li>🔀 Train-Test Split</li>
            <li>🛠️ Preprocessing Pipeline</li>
            <li>🤖 Logistic Regression</li>
            <li>🌳 Decision Tree</li>
            <li>🌲 Random Forest</li>
            <li>📊 Model Comparison</li>
            <li>📈 Model Evaluation</li>
            <li>🔮 New Passenger Predictions</li>
        </ul>

        <br>

        <div>
            <span class="badge">Python</span>
            <span class="badge">Pandas</span>
            <span class="badge">NumPy</span>
            <span class="badge">Matplotlib</span>
            <span class="badge">Seaborn</span>
            <span class="badge">Scikit-learn</span>
        </div>

    </div>

    <div class="project">

        <h2>📈 Best Model</h2>

        <p><strong>Logistic Regression</strong></p>

        <p>Accuracy: 83.8%</p>
        <p>F1 Score: 78.2%</p>
        <p>ROC-AUC: 87.9%</p>

    </div>

    <div class="project">

        <h2>🎯 Goal</h2>

        <p>
            Build a strong foundation in Machine Learning and progress toward
            Deep Learning, Generative AI and Agentic AI.
        </p>

    </div>

</div>

<footer>
    🚀 Built as part of my AI Engineering Journey
</footer>

</body>
</html>
