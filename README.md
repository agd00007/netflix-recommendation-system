# 🎬 Netflix Recommendation System

A **content-based recommendation system** for Netflix movies and TV shows developed with **Python** and Machine Learning techniques.

The user enters a movie or TV show they enjoyed, and the application analyzes the catalog to return the **10 most similar titles**, including their similarity percentage.

## 📸 Application Preview

> A screenshot of the application will be added here.

## 🚀 Features

* Graphical user interface for searching movies and TV shows.
* Returns the **10 most similar titles**.
* Displays a **similarity percentage** for each recommendation.
* Content-Based Recommendation System.
* Text processing using **TF-IDF**.
* Similarity calculation using **Cosine Similarity**.
* Recommendations based on multiple features:

  * Genre
  * Description
  * Cast
  * Director
  * Country
  * Rating
* Handling of missing values in the dataset.
* Case-insensitive title search.
* Automatic removal of accidental leading and trailing spaces.
* Validation for titles that are not available in the catalog.
* Validation for empty searches.
* Desktop graphical interface developed with **Tkinter**.

## 🧠 How It Works

The recommendation engine combines several features from each movie or TV show to create a textual representation of its content.

The selected features are processed using **TF-IDF (Term Frequency-Inverse Document Frequency)**, which transforms the textual information into numerical vectors.

The system then uses **Cosine Similarity** to compare the title selected by the user with the rest of the Netflix catalog.

The results are sorted from highest to lowest similarity, and the **10 most similar titles** are displayed as recommendations.

## 🛠️ Technologies

* Python
* Pandas
* Scikit-learn
* Tkinter
* TF-IDF
* Cosine Similarity

## 📊 Dataset

The project uses a Netflix movies and TV shows dataset containing information such as:

* Title
* Genre
* Description
* Cast
* Director
* Country
* Rating

The original dataset is available on **Kaggle — Netflix Movies and TV Shows 2021**.

## 💻 User Interface

The application includes a desktop graphical interface built with **Tkinter**.

The user enters the title of a movie or TV show and clicks the recommendation button. The system then displays the 10 most similar titles and their similarity percentages.

Example output:

```text
1. Recommended Title - Similarity: 58%
2. Recommended Title - Similarity: 51%
3. Recommended Title - Similarity: 47%
...
```

## ▶️ Installation and Usage

Clone the repository:

```bash
git clone https://github.com/agd00007/netflix-recommendation-system.git
```

Install the required dependencies:

```bash
pip install pandas scikit-learn
```

Run the application:

```bash
python Netflix.py
```

## 📁 Project Structure

```text
netflix-recommendation-system/
│
├── Netflix.py
├── netflix_titles.csv
├── README.md
└── screenshot.png
```

## 🎯 Project Goal

The goal of this project is to apply **Python, data processing and Machine Learning concepts** to build a complete recommendation system, from dataset preprocessing and feature extraction to similarity calculation and integration into a graphical user interface.

This project demonstrates the implementation of a **content-based recommendation engine** and the integration of a Machine Learning workflow into a functional desktop application.

---

Developed by **Ana María Gutiérrez Díaz**
