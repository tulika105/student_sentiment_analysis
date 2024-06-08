# student_sentiment_analysis
The project aims at diving into the world of engineering education to understand what students think. We're not just listening to what they say, we're analyzing their feedback using a technique called sentiment analysis. The objective of the project is to uncover the positive and negative feelings students have on engineering education based on their feedbacks using nlp and machine learning techniques.
1.	We created a google form through which we collected data from students such as their subjects, no of hours studying, gender, attendance, etc.
2.	The google form is then converted to csv format for analysis.
3.	First step includes importing necessary python libraries, data cleaning, data pre-processing such as tokenization, stemming, lemmatization and stopwords removal.
4.	We then calculated sentiment scores, subjectivity scores and labels to categorize the feedback as positive, negative or neutral.
5.	Machine learning techniques such as k-means clustering have been used to group similar feedbacks together and techniques such as TF-IDF is applied to represent the text in numerical format.
6.	To visualize the data for easy interpretation we performed exploratory analysis to get more insights.
7.	We used different ml models for predicting sentiment labels by training the data and testing it on unseen data.
8.	Tuning the hyperparameters to improve the performance of the model by achieving higher accuracy.
# Technologies used
- Jupyter notebook
- pandas
- numpy
- nltk
- textblob
- re
