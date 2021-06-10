from flask import Flask, render_template, url_for, request
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
from sklearn.model_selection import train_test_split
from flasgger import Swagger


# inizializza flask
app = Flask(__name__)
Swagger(app)# crea l'api per l'app Flask

# importazione dataset
df = pd.read_csv("final_movie_reviews.csv")

# features and label
X, y = df.stop_tokens, df.score_indexed

# extract featuresf with count vectorizer
cv = CountVectorizer()

X = cv.fit_transform(X)  # Fit the Data
X_train, X_test, y_train, y_test = train_test_split( # divisione training e test
    X, y, test_size=0.33, random_state=42)

clf = MultinomialNB()
clf.fit(X_train, y_train)
clf.score(X_test, y_test)

@app.route('/')
def home():
    return render_template('home.html')# renderizza template home, da qui è possibile inserire la recensione

#mostra risultato della predizione
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        vect = cv.transform(data).toarray()
        my_prediction = clf.predict(vect)
        return render_template('result.html', prediction=my_prediction)

# flasgger api, espone i risultati della predizione tramite un'api
@app.route('/predict_api',methods=["Get"])# per accedere bisogna dare il l'url '\apidocs'
def predict_api():
    
    """Controlla se la recensione è positiva 
    o negativa ! 
    ---
    parameters:  
      - name: message
        in: query
        type: string
        required: true
    responses:
        200:
            description: The output values
        
    """
    message=request.args.get("message")# prende il messaggio del form
    data = [message] # inserisce in data
    vect = cv.transform(data).toarray() # vettorizza
    prediction=clf.predict(vect) # predizione 
    print(prediction)
    return "Ciao, ecco la recensione ----> "+str(prediction)+"\n[0]--> positiva \n[1]-->negativa" # risultato

# carica il file testuale e classifica la recensione in negativa o positiva
@app.route('/predict_file',methods=["POST"])
def predict_api_file():
    """Carica un file e classifica le tue recensioni
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
      
    responses:
        200:
            description: The output values
        
    """
    df_test=pd.read_csv(request.files.get("file"))# salva e converte in dataframe
    data = df_test
    vect = cv.transform(data).toarray() # converte in array
    prediction=clf.predict(vect) # predizione
     
    return  str(list(prediction))# lista dei risultati (ATTUALMENTE FUNZIONA SOLO CON FILE CONENTENTI UNA RIGA!)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')# porta
