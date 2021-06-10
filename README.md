# Flask ML App
Flask Machine Learning app for text classification.


This app is the result of a Big Data exam. The purpose of the exame was to build an app that solves a Big data related problem. The dataset used for the project is this <a href="https://www.kaggle.com/ryati131457/web-data-amazon-movie-reviews-processed">link</a>. It contains reviews of films and Tv series from the Amazon Prime Video's platform. In summary, I've processed the dataset, built an off-line classifier, and created an app with Flask. Inside Flask I've included also Flassgger, in this It's also possible to expose the model as an Api.

The solution implemented includes a set of stages and technologies:
<br>
<ol>
<li>Pre-processing with PySpark, the result of this stage is a csv dataset (final_movie_reviews.csv);</li>
<li>Building an off-line classifier (Naive Bayes) with Scikit-learn;</li>
<li>Creation of a Flask web app that allows users to use the classifier for new predictions;</li>
<li>Web app Dockerization.</li>
</ol>

Clone and try the app in your local env!
- `python3 -m venv venv` 
- `  . venv/bin/activate`
- `pip install -r requirements.txt`
- `python app.py`

You can also use the `docker-compose` file.
