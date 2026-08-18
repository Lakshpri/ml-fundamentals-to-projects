# Titanic Project — Interview Questions (Simple English)

Easy answers you can say out loud in an interview, based on what you actually did in this project.

---

## 1. Tell me about this project

**Q: What did you build?**
A: I built a model that predicts if a Titanic passenger survived or not. I used their age, sex, ticket class, and family info to make the prediction.

**Q: What steps did you follow?**
A: First I looked at the data (EDA). Then I cleaned the missing values. Then I created new useful columns (feature engineering). Then I split the data into train and test. Then I trained 3 different models. Then I compared them. Then I picked the best one and tested it on new, made-up passengers.

---

## 2. Looking at the data (EDA)

**Q: What did you notice first?**
A: Women survived much more than men. Rich passengers (1st class) survived more than poor passengers (3rd class). Many passengers were missing an "age" value, and almost all were missing "cabin" info.

**Q: Why check missing data early?**
A: Because if I don't fix missing values, the model will crash or give wrong answers. I need to know how much is missing before deciding what to do.

**Q: Some columns were useless — why?**
A: Some columns basically repeated the same info in a different form (like "alive" meaning the same as "survived"). Keeping them would let the model "cheat" by copying the answer instead of learning.

---

## 3. Cleaning the data

**Q: How did you handle missing values?**
A: 
- "Cabin" was missing for almost 8 out of 10 people, so I just removed that column — too much guessing needed.
- "Age" was missing for about 2 out of 10 people, so I filled it with the middle value (median) of all ages.
- "Embarked" (which port they got on) was missing for only 2 people, so I filled it with the most common port.

**Q: Why median for age, not average?**
A: Because a few very old passengers can pull the average up. The median (middle value) is more fair and not affected by extreme numbers.

---

## 4. Making new features (Feature Engineering)

**Q: What new columns did you create, and why?**

- **family_size** = brothers/sisters/spouse + parents/kids + 1 (the person themself). 
  *Why:* Traveling with family probably changed how people acted when the ship was sinking, so this one number is more useful than two separate columns.

- **is_alone** = Yes/No, was this person traveling alone?
  *Why:* People traveling completely alone behaved differently than people in small families — I saw this clearly in the survival numbers.

- **title** = Mr, Mrs, Miss, Master, etc — taken from their name.
  *Why:* A title tells you age + gender + social status all in one word. For example "Master" means young boy, and young boys survived a lot — more than the word "male" alone would tell you.

- **fare_per_person** = ticket price divided by family size.
  *Why:* A family of 5 sharing one ticket looks "expensive" in the raw data, but the price per person is what really shows how rich they were.

**Q: Why remove "name" and "ticket" columns after that?**
A: Because I already pulled the useful part out (the title). The rest of the name and the ticket number don't help the model — they're just random text.

---

## 5. Splitting into train and test

**Q: Why split the data into train and test?**
A: So I can test the model on passengers it has never seen before. This tells me if the model really learned patterns, or just memorized the training data.

**Q: Why split BEFORE cleaning/scaling the numbers?**
A: If I scale or process all the data together first, the model accidentally "peeks" at the test data. That makes my test score look better than it really is. So I only look at the training data first, then apply the same steps to the test data separately.

**Q: What does "stratify" mean and why use it?**
A: It just makes sure the train set and test set both have a similar percentage of survivors. Otherwise, by bad luck, one half could have way more survivors than the other.

---

## 6. Preparing the data for the model

**Q: Why scale the numbers?**
A: Some numbers are big (like fare: 0–500) and some are small (like family_size: 1–8). Without scaling, the big numbers would unfairly dominate the model's decisions. Scaling makes everything fair, on the same range.

**Q: Does scaling matter for every model?**
A: No. It matters a lot for Logistic Regression. It doesn't matter for Decision Tree or Random Forest — trees don't care about number size, only about "is this bigger or smaller than X."

**Q: Why turn text categories (like "male"/"female") into 0s and 1s?**
A: Because models only understand numbers, not words. This is called one-hot encoding — turning each category into its own yes/no column.

---

## 7. The 3 models

**Q: Which models did you use, and why these three?**
A: 
1. **Logistic Regression** — a simple, easy-to-understand model. Good starting point.
2. **Decision Tree** — like a flowchart of yes/no questions. Easy to explain to anyone.
3. **Random Forest** — many decision trees working together and voting. Usually more accurate than just one tree.

I picked these three because they're different types of models, so comparing them shows which approach works best for this problem.

**Q: What is cross-validation and why did you use it?**
A: Instead of testing the model just once, I test it 5 different times on 5 different slices of the training data. This gives a more trustworthy score, instead of getting lucky (or unlucky) with just one test.

---

## 8. Comparing the models

**Q: Why not just use accuracy to pick the best model?**
A: Accuracy alone can be misleading. If most people didn't survive, a lazy model could just guess "did not survive" every time and still look accurate. So I also checked:
- **Precision** — when the model says "survived," how often is it right?
- **Recall** — out of all the people who actually survived, how many did the model correctly catch?
- **F1** — a balanced mix of precision and recall.
- **ROC-AUC** — how good the model is at ranking survivors above non-survivors overall.

**Q: How did you pick the winning model?**
A: I used the F1 score to pick the best one, since it balances the two important things (precision and recall) into one fair number.

**Q: What does the confusion matrix show?**
A: It's a simple table showing 4 numbers: correct "survived" guesses, correct "did not survive" guesses, and the two types of mistakes. It shows exactly what kind of mistakes the model makes, not just how many.

---

## 9. Feature importance (which columns mattered most)

**Q: Which features mattered the most?**
A: Sex, passenger class, and title mattered the most. This matches the real history — "women and children first," and richer passengers had better access to lifeboats.

**Q: A tricky question — does Logistic Regression have "feature importance"?**
A: Not exactly. Decision Tree and Random Forest have a built-in "feature_importances_" score. Logistic Regression instead has "coefficients" — numbers that show how much each feature pushes the prediction up or down. So technically, for Logistic Regression, we call it "coefficients" or "feature influence," not "feature importance."

---

## 10. Predicting on new passengers

**Q: How did you test the model on brand-new, made-up passengers?**
A: I made a small table of fake passengers (like a rich woman, a poor man, a young boy). Then I applied the exact same steps I used before (like calculating family_size and fare_per_person) and fed them to the trained model to get a prediction and a survival probability.

**Q: Why does it matter that you used the exact same steps as before?**
A: If the new data isn't prepared in the exact same way as the training data, the model gets confused and gives wrong answers, or the code just breaks. Consistency is key.

---

## 11. Big-picture / business questions

**Q: In simple words, what did you learn from this project?**
A: Gender and class were the biggest factors in survival. Combining features (like title, which mixes age+gender+status) works better than using raw columns alone. Random Forest was usually the strongest model. And looking at multiple scores (not just accuracy) gives a more honest picture.

**Q: What would you improve if you had more time?**
A: I would try tuning the model settings automatically (instead of guessing good settings), try a stronger model like XGBoost, and move the missing-age fix fully inside the pipeline so there's zero chance of the test data leaking into training.

**Q: What's one weakness of this project?**
A: It's a small, old, well-known dataset (only about 900 people), so it's more of a learning exercise than a real production model. Real-world data would be messier and bigger.

---

## 12. General ML basics (not just about Titanic)

**Q: What is overfitting?**
A: Overfitting is when a model learns the training data TOO well — it even memorizes the noise and random little details, not just the real pattern. It looks great on training data but does badly on new data, because it never really "understood" the pattern, it just memorized answers.

**Q: What is underfitting?**
A: Underfitting is the opposite — the model is too simple, so it doesn't even learn the real pattern properly. It does badly on both training data AND new data.

**Q: What is the bias-variance tradeoff?**
A: 
- **Bias** = how wrong the model is because it's too simple (this causes underfitting).
- **Variance** = how much the model changes if you give it slightly different training data (high variance causes overfitting).
You usually can't have both very low bias AND very low variance at the same time — improving one often makes the other worse. The goal is to find a good middle balance.

**Q: How does Random Forest actually reduce variance?**
A: A single Decision Tree can overfit easily and change a lot if you tweak the training data. Random Forest builds MANY trees, and each tree only sees a random chunk of the data and a random set of features. Then all the trees vote on the final answer. Because each tree makes different mistakes, the mistakes cancel out when you average them — so the final answer is more stable and less overfit than any single tree.

**Q: What does regularization do in Logistic Regression?**
A: Regularization adds a small penalty for having very large coefficient values. This stops the model from relying too heavily on just one or two features and getting overconfident. It keeps the model simpler and helps it perform better on new, unseen data.

**Q: When would you pick a tree-based model over a linear model, and vice versa?**
A: 
- Pick a **linear model** (like Logistic Regression) when: the relationship between features and the answer is roughly straight-line/simple, you want easy explainability, or you have a smaller dataset.
- Pick a **tree-based model** (like Random Forest) when: the pattern is complex or non-linear, features interact with each other in tricky ways, or you have enough data to support a more complex model.

---

## 13. "What if" and debugging questions

**Q: Your model gets 95% accuracy on training data but only 60% on test data. What's wrong?**
A: This is a classic sign of overfitting. The model memorized the training data instead of learning general patterns. To fix it, I would: make the model simpler (like lowering max_depth in a tree), add regularization, get more training data, or use cross-validation to catch this earlier.

**Q: How would you handle a dataset that's 100x bigger than this one?**
A: A few changes I'd make:
- Use more memory-efficient data loading (like reading the file in chunks, or using a format like Parquet instead of CSV).
- Random Forest might get slow to train, so I might switch to a faster model like Logistic Regression, or a more efficient boosted-tree library like XGBoost/LightGBM.
- Use cross-validation carefully — with huge data, even a single train/test split might already give a stable, trustworthy score, so I could save time by not always doing 5-fold CV.
- Consider running training on a cloud machine or using a library that supports distributed computing.

**Q: How would you deploy this model so other people could use it?**
A: 
1. Save the trained pipeline (the model plus the preprocessing steps together) to a file, using something like `joblib` or `pickle`.
2. Build a small API (for example with Flask or FastAPI) that loads this saved pipeline and accepts new passenger data as input.
3. The API would return a prediction (survived or not) and a probability score as output.
4. Put this API behind a server, so other apps or a website could send requests to it and get predictions back.
5. I'd also want to monitor it over time, to check if its performance drops as new data patterns change (this is called "model drift").

**Q: What would you check first if your model's predictions suddenly seemed way off in production?**
A: First I'd check if the input data format changed (missing columns, different value types). Then I'd check if the real-world data has "drifted" away from what the model was trained on — for example, if the type of passengers changed a lot. I'd also compare recent predictions against actual outcomes, if available, to measure how much accuracy dropped.

**Q: How would you know if a feature is actually helping the model, or just adding noise?**
A: I'd check the feature's importance/coefficient score after training. I could also try removing that one feature and re-training, then compare the F1/accuracy score with and without it. If removing it barely changes performance, it probably wasn't helping much.