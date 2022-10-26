import pandas as pd
df = pd.read_csv(r"C:\Users\chist\Desktop\ML\UNZIP_ME_FOR_NOTEBOOKS_ML_RUS_V1\DATA\airline_tweets.csv")

data = df[['airline_sentiment', 'text']]
X = data['text']
y = data['airline_sentiment']

# сначала разбиение данных, а потом векторизацию - воизбежание утечки данных в тестовый набор
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)

from sklearn.feature_extraction.text import TfidfVectorizer
vec = TfidfVectorizer(stop_words='english')
# синтаксис векторизации похож на масштабирование данных
vec.fit(X_train)
X_train_vec = vec.transform(X_train)
X_test_vec = vec.transform(X_test)

from sklearn.svm import LinearSVC
model = LinearSVC()
model.fit(X_train_vec, y_train)

preds = model.predict(X_test_vec)


from sklearn.pipeline import Pipeline
pipe = Pipeline([('vec', TfidfVectorizer()),
                 ('svc', LinearSVC())])
pipe.fit(X_train, y_train)

<<<<<<< HEAD
print('Введите фразу и комп классифицирует ее ', pipe.predict([input()]))
=======
print('Введите фразу', pipe.predict([input()]))
>>>>>>> 5f916a14b40cb4c0117d4fbe4b7186ba4fc230a0
