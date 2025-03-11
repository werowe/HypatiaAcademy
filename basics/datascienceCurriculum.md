# Data Science Curriculum 



# 2025 Weekly Schedule

## First Three Weeks
https://github.com/werowe/HypatiaAcademy?tab=readme-ov-file#statistics

* The Normal Curve
* Normalize Data with z-Score
* Poisson Distribution
* Normalize data, std, mean, z-score in Google Sheets
* Normal and Uniform Distribution in Google Sheets
* Binomial Distribution in Google Sheets
* Exponential Distribution



## Jan 7
* generate some random data using the =NORMINV(RAND(), average, std)
* calculate the z-score---use int() to make it an integer
* calculate the cumulative property of you observation using =NORM.DIST(observed,average,std,true)
* use chart to make a chart
6:59
 


## Jan 10
homework.  what does false versus true mean in this =NORM.DIST(C2,mean,std,false) function.  put into your previous homework and test it/prove it
homework:  so figure out how to adjust the chart in google sheets to show the edges, labels
in integers like -2, -1, 0, 1, 2


## January 14

homework https://docs.google.com/spreadsheets/d/1A-iJK4s-9hwPGzLW3jgpi4eKp1Uy4qv7JybnXWo1PjY/edit?usp=sharing
 
* optional homework figure out the  probability of flipping a coin 6 times and getting 2 heads
* solve this homework optional:
- why do you multiple each combination by	
- the probability of (each trial) ^ success 	
- and the probability of (1 - each trial)^(number of trials - successes)

which answer is correct this one https://docs.google.com/document/d/1q9lmsMowu2iVxyfCTvOSSttibkm669_lTNhgW3_6B78/edit?usp=sharing or this one https://docs.google.com/spreadsheets/d/1_05Bqp00qoUvtdOi77VEA6PLQsomabY8O7akXXYkeYo/edit?usp=sharing


```

Марія Афанасьєва
 
https://docs.google.com/document/d/1L3uAsnuPmbBLlJ0ni-NV9EANCQf93mkodAjMFtUM4p4/edit?usp=sharing
The formula explanation
```

```
Illia Zhupanov
 
https://docs.google.com/spreadsheets/d/17n2Prl6EDjZ4Rp54crbgaBNNasviuuYT2gCcUypt-3Q/edit?usp=sharing
diff between the two approaches
```

## Jan 21

homework is to understand this https://docs.google.com/spreadsheets/d/1p9vqIRI7LvKr-4OLL4VqhVjlXdbAfolBljSzPb-jWIQ/edit?usp=sharing


``` 
The formula explanation and why does the sum = 1
https://docs.google.com/spreadsheets/d/1V3DUL8GfVOLA-j-kxwPS3haeZ9V5Q_EzVvS09ZqXOzU/edit?usp=sharing
```

## Jan 21 Basic Numpy Introduction (slicing comes later).  Needed for Stats next few classes

homework https://colab.research.google.com/drive/1CNhYyLEMkIo16VmxUH9vUa9b2v5yJqeX?usp=sharing
 


## Jan 28  Goodness of Fit, Normal, and Weibull

https://github.com/werowe/HypatiaAcademy/blob/master/stats/goodness_of_fit.ipynb


## Jan 31  Goodness of Fit, Normal, and Weibull
https://github.com/werowe/HypatiaAcademy/blob/master/stats/weibull_ilya_numpy_plotting_homework_31_01_25.ipynb

## Feb 4
https://github.com/werowe/HypatiaAcademy/blob/master/class/2024_02_04_numpy_slicing_diagonal.ipynb


## Feb 7
(none, review Numpy quick start guide) 

## Feb 11
https://github.com/werowe/HypatiaAcademy/blob/master/stats/2024_02_11_charting.ipynb
https://github.com/werowe/HypatiaAcademy/blob/master/stats/2024_02_11_histogram.ipynb
https://github.com/werowe/HypatiaAcademy/blob/master/charts/2025_02_14_pie_chart.ipynb

## Feb 14
https://github.com/werowe/HypatiaAcademy/blob/master/stats/seaborn_bar.ipynb

# Pandas


## Feb 21
https://github.com/werowe/HypatiaAcademy/blob/master/pandas/ilya-pandas_homework_20_02_25.ipynb


## Feb 25 Fix Issues in this Pandas data from Ilias
https://github.com/werowe/HypatiaAcademy/blob/master/pandas/ilya-pandas_homework_20_02_25.ipynb


## Feb 27  Take Data from Previous Classes and Now put into Spark


## Example 1
https://github.com/werowe/HypatiaAcademy/blob/master/spark/youtube_german_channels.ipynb


## Example 2
https://github.com/werowe/HypatiaAcademy/blob/master/spark/2025_02_28_diana_pandas_to_spark.ipynb


## Imdb Spark
https://github.com/werowe/HypatiaAcademy/blob/master/spark/Imdb_spark_data.ipynb

## March 4 Steam Games
https://github.com/werowe/HypatiaAcademy/blob/master/spark/homework_spark_04_03_25.ipynb



## March 8 Data Cleaning part II

https://github.com/werowe/HypatiaAcademy/blob/master/pandas/pandas_missing_data.ipynb

**Homework**:  fix x=df.loc[abs(df['salary'] - mean) > 2 * std].apply(makeMean) in that notebook.  It updates all columns and the index too instead of one column.


## March 11: Data Cleaning part I

https://github.com/werowe/HypatiaAcademy/blob/master/pandas/pandas_drop_outliers.ipynb

### Homework Bad data Examples

* UCI Machine Learning Repository
- Wine Quality Dataset (contains outliers and formatting issues).    https://archive.ics.uci.edu/dataset/186/wine+quality
- Solar Flare Dataset (missing values and categorical inconsistencies)  https://archive.ics.uci.edu/dataset/89/solar+flare

* Kaggle
- https://www.kaggle.com/code/bozungu/ebay-used-car-sales-data  eBay Car Sales Dataset (contains missing values and inconsistencies).
- https://www.kaggle.com/datasets/yasserh/housing-prices-dataset (Includes missing values for features like lot size and house condition, as well as price outliers)
- https://www.kaggle.com/datasets/unsdsn/world-happiness


  

## Kaggle Data Cleaning Competition

 

https://www.kaggle.com/code/rtatman/data-cleaning-challenge-handling-missing-values


 

### Student Project: **Exploratory Analysis of a Public Dataset**
- **Objective**: Perform data cleaning and exploratory analysis on a dataset.
- **Dataset Ideas**:
  - [Kaggle Titanic Dataset](https://www.kaggle.com/c/titanic): Analyze survival rates based on passenger demographics.
  - [World Happiness Report](https://www.kaggle.com/unsdsn/world-happiness): Explore factors contributing to happiness scores.
- **Deliverables**:
  - Cleaned dataset.
  - Visualizations (e.g., bar plots, histograms, scatterplots).
  - Insights from descriptive statistics.

---

## Month 2: Statistics and Probability for Data Science

### Regression

- **Week 4**: Correlation vs. causation and linear regression.

### Student Project: **Analyzing Relationships Between Variables**
- **Objective**: Use statistical techniques to find relationships between variables.
- **Dataset Ideas**:
  - [Housing Prices Dataset](https://www.kaggle.com/c/house-prices-advanced-regression-techniques): Analyze relationships between house prices and features like square footage or location.
  - [COVID-19 Dataset](https://ourworldindata.org/coronavirus-data): Explore relationships between vaccination rates and case numbers.
- **Deliverables**:
  - Hypothesis tests with conclusions.
  - Correlation matrix or scatterplots showing relationships.
  - Regression model results with interpretation.

---

## Month 3: Machine Learning Basics

### Topics Covered:
- Introduction to Machine Learning
- Supervised Learning (Regression & Classification)
- Unsupervised Learning (Clustering)

### Week-by-Week Breakdown:
- **Week 1**: Overview of machine learning concepts and workflows.
- **Week 2**: Supervised learning with regression models.
- **Week 3**: Supervised learning with classification models.
- **Week 4**: Unsupervised learning with clustering algorithms.

### Student Project: **Predicting Outcomes Using Machine Learning**
- **Objective**: Build a supervised learning model to predict outcomes.
- **Dataset Ideas**:
  - [Titanic Dataset](https://www.kaggle.com/c/titanic): Predict survival based on passenger features using classification models.
  - [California Housing Dataset](https://scikit-learn.org/stable/datasets/real_world.html#california-housing-dataset): Predict house prices using regression models.
- **Deliverables**:
  - Trained machine learning model with evaluation metrics (accuracy, R², etc.).
  - Feature importance analysis or insights from the model.

---

## Month 4: Advanced Machine Learning Techniques

### Topics Covered:
- Decision Trees and Random Forests
- Model Optimization
- Ensemble Methods (Bagging, Boosting)

### Week-by-Week Breakdown:
- **Week 1**: Decision trees and random forests.
- **Week 2**: Hyperparameter tuning and cross-validation.
- **Week 3–4**: Ensemble methods like Gradient Boosting (XGBoost, LightGBM).

### Student Project: **Improving Model Performance**
- **Objective**: Build an optimized ensemble model for a real-world problem.
- **Dataset Ideas**:
  - [Customer Churn Dataset](https://www.kaggle.com/blastchar/telco-customer-churn): Predict customer churn using ensemble methods like Random Forest or XGBoost.
  - [Credit Card Fraud Detection Dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud): Detect fraudulent transactions using boosting algorithms.
- **Deliverables**:
  - Optimized machine learning model with hyperparameter tuning results.
  - Comparison of performance metrics before and after optimization.

---

## Month 5: Neural Networks and Deep Learning Basics

### Topics Covered:
1. Fundamentals of Neural Networks
    - Architecture, activation functions, forward/backpropagation
    - Loss functions
    - TensorFlow/Keras basics
2. Applications of Deep Learning
    - Convolutional Neural Networks (CNNs)
    - Recurrent Neural Networks (RNNs)

### Week-by-Week Breakdown:
1. Weeks 1–2 focus on neural network fundamentals.
2. Weeks 3–4 introduce CNNs for image data and RNNs for sequential data.

### Student Project: **Image Classification or Text Analysis**
#### Option A: Image Classification
   - Use a CNN to classify images in a dataset like MNIST or CIFAR10.
   - Example Dataset: [MNIST Handwritten Digits](http://yann.lecun.com/exdb/mnist/).

#### Option B: Text Sentiment Analysis
   - Use an RNN or LSTM to perform sentiment analysis on text data.
   - Example Dataset: [IMDB Movie Reviews](https://ai.stanford.edu/~amaas/data/sentiment/).

#### Deliverables for Both Options:
   - Trained neural network model with evaluation metrics (accuracy, loss).
   - Visualizations of training progress (e.g., loss curves).

---

## Month 6: Advanced Deep Learning & Capstone Project

### Topics Covered:
1. Advanced Deep Learning Topics
    - Transfer learning with pre-trained models (e.g., ResNet, VGG).
    - Generative Adversarial Networks (GANs).
2. Capstone Project Execution & Presentation

### Week-by-Week Breakdown:
1. Weeks 1–2 focus on advanced deep learning techniques like transfer learning and GANs.
2. Weeks 3–4 are dedicated to the capstone project.

---

### Capstone Project Ideas
Students choose a topic based on their interests. They will work independently or in teams to apply all the skills learned during the course.

#### Example Capstone Projects:
1. **Image Classification Using Transfer Learning**
   - Use a pre-trained model like ResNet or VGG to classify custom images (e.g., medical images or wildlife photos).
   - Example Dataset: [Chest X-Ray Images for Pneumonia Detection](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia).

2. **Time-Series Forecasting**
   - Use RNNs/LSTMs to forecast stock prices or weather patterns.
   - Example Dataset: [Stock Market Data](https://www.kaggle.com/datasets/szrlee/stock-time-series-data).

3. **Customer Segmentation + Predictive Modeling**
   - Combine clustering techniques with supervised learning to segment customers and predict behavior like churn or purchase likelihood.
   - Example Dataset: [E-Commerce Customer Behavior](https://www.kaggle.com/mkechinov/ecommerce-behavior-data-from-multi-category-store).

#### Deliverables for Capstone Projects:
   - Problem statement and goals clearly defined.
   - Cleaned dataset with EDA visualizations.
   - Machine learning/deep learning models built with evaluation metrics reported.
   - Final presentation summarizing findings, challenges, and results.



# One-Month Curriculum: Teaching Large Language Models (LLMs)

This curriculum is designed to teach students about Large Language Models (LLMs) using practical tools like **Hugging Face** and **Google Colab**, with a focus on leveraging pre-trained models due to limited computational resources.

---

## Week 1: Introduction to Large Language Models

### Day 1: Basics of LLMs
- **Objective**: Understand what LLMs are and their applications.
- **Topics**:
  - What are LLMs? (e.g., GPT, BERT, T5)
  - Key concepts: transformers, attention mechanism.
  - Applications: text generation, summarization, translation, etc.
- **Activity**:
  - Watch introductory videos on transformers (e.g., "Attention is All You Need").
  - Discuss real-world applications of LLMs.

### Day 2: Hugging Face and Google Colab Setup
- **Objective**: Familiarize students with Hugging Face and Google Colab.
- **Topics**:
  - Overview of Hugging Face's Transformers library.
  - Setting up Google Colab for NLP tasks.
- **Activity**:
!pip install transformers datasets
text
- Explore the Hugging Face Model Hub.

### Day 3–4: Understanding Pre-Trained Models
- **Objective**: Learn how pre-trained models work and why they’re useful.
- **Topics**:
- Pre-training vs. fine-tuning.
- Common pre-trained models (GPT, BERT, DistilBERT).
- **Activity**:
from transformers import pipeline
summarizer = pipeline("summarization")
text = "Your long text here..."
print(summarizer(text))
text
- Experiment with different pipelines (e.g., text classification, question answering).

### Day 5: Quiz/Review
- Review key concepts from the week.
- Small quiz or discussion to reinforce learning.

---

## Week 2: Fine-Tuning Pre-Trained Models

### Day 6–7: Dataset Preparation
- **Objective**: Learn how to prepare datasets for fine-tuning.
- **Topics**:
- Overview of datasets for NLP tasks (e.g., IMDB for sentiment analysis).
- Tokenization and preprocessing.
- **Activity**:
from datasets import load_dataset
dataset = load_dataset("imdb")
print(dataset["train"])
text

### Day 8–9: Fine-Tuning Basics
- **Objective**: Fine-tune a small pre-trained model on a custom task.
- **Topics**:
- Fine-tuning vs. full training.
- Using smaller models like DistilBERT for resource efficiency.
- **Activity**:

 
from transformers import AutoModelForSequenceClassification, TrainingArguments, Trainer
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased", num_labels=2)
Define training arguments
training_args = TrainingArguments(
output_dir="./results",
evaluation_strategy="epoch",
save_strategy="epoch",
logging_dir="./logs",
per_device_train_batch_size=8,
num_train_epochs=3,
)
trainer = Trainer(
model=model,
args=training_args,
train_dataset=dataset["train"],
eval_dataset=dataset["test"],
)
trainer.train()
text

### Day 10: Evaluation
- Evaluate the fine-tuned model on test data.
- Discuss metrics like accuracy, precision, recall.

---

## Week 3: Advanced Applications

### Day 11–12: Text Generation with GPT Models
- **Objective**: Generate coherent text using GPT-based models.
- **Topics**:
- How GPT works for text generation.
- Adjusting parameters like `temperature` and `max_length`.
- **Activity**:
from transformers import pipeline
generator = pipeline("text-generation", model="gpt2")
prompt = "Once upon a time"
print(generator(prompt, max_length=50, num_return_sequences=3))
text

### Day 13–14: Summarization and Translation
- Use pre-trained models for summarization and translation tasks.
- Activity:
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
translator = pipeline("translation_en_to_fr", model="Helsinki-NLP/opus-mt-en-fr")
text = "Your long English text here..."
print(summarizer(text))
print(translator(text))
text

---

## Week 4: Custom Projects and Deployment

### Day 15–16: Custom NLP Task
- Students choose an NLP task (e.g., sentiment analysis, question answering).
- Prepare data and fine-tune a small model.

### Day 17–18: Model Deployment Basics
- Learn how to deploy models using Hugging Face Spaces or Streamlit.
- Activity:
 - Use Hugging Face Spaces with Gradio for deployment.

#### Example Deployment Code:
import gradio as gr
from transformers import pipeline
generator = pipeline("text-generation", model="gpt2")
def generate_text(prompt):
return generator(prompt, max_length=50)["generated_text"]
gr.Interface(fn=generate_text, inputs="text", outputs="text").launch()
text

---

### Day **19–20: Presentations and Wrap-Up**
1. Students present their projects to the class.
2. Review key concepts learned throughout the month.

---

## Tools Used

1. **Hugging Face Transformers Library**:
   - For accessing pre-trained models and pipelines.
2. **Google Colab**:
   - For running code without requiring powerful local machines.
3. **Gradio or Hugging Face Spaces**:
   - For deploying simple interfaces for NLP tasks.

---

## Key Benefits of This Curriculum

1. Focuses on practical usage rather than computationally expensive training.
2. Introduces students to industry-standard tools like Hugging Face.
3. Encourages hands-on learning through projects and experimentation.

 
