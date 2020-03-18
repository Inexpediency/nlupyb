import config
from dataset import get_dataset

from random import choice as randomChoice
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
# from sklearn.svm import SVC
# from sklearn.feature_extraction.text import TfidfVectorizer


# # # Config of bot's phrases # # #
BOT_CONFIG = config.get_bot_config()

# # # Get chat dataset # # #
chat_dataset = get_dataset(BOT_CONFIG['chat_limit'])

# # # Create dataset # # #
dataset = []
for intent, intent_data in BOT_CONFIG['intents'].items():
    for example in intent_data['examples']:
        dataset.append([example, intent])
X_text = [x for x, y in dataset]
y = [y for x, y in dataset]

# # # Vectorising dataset # # #
# vectorizer = TfidfVectorizer()
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X_text)

# # # Teaching model # # #
# clf = SVC(probability=True)
clf = LogisticRegression()
clf.fit(X, y)

# # # Coefficient selection # # #
# vectors = vectorizer.transform(['Че там с погодой'])
# intent = clf.predict(vectors)[0]
# probas = clf.predict_proba(vectors)[0]
# index = (list(clf.classes_)).index(intent)
# probability = probas[index]
# print(intent, probability)


def get_intent(text):
    vectors = vectorizer.transform([text])
    intent = clf.predict(vectors)[0]

    probas = clf.predict_proba(vectors)[0]
    index = (list(clf.classes_)).index(intent)
    probability = probas[index]

    if BOT_CONFIG['threshold'] <= probability:
        return intent


def generate_random_answer(text):
    text = text.lower()
    threshold = BOT_CONFIG['chat_threshold']
    for question, answer in chat_dataset:
        if abs(len(text) - len(question)) / len(question) <= (1 - threshold):
            # Levenshtein distance
            distanse = nltk.edit_distance(text, question)
            # How many percent are the phrases like
            similarity = 1 - min(1, distanse / len(question))
            if similarity >= threshold:
                return answer


def get_failure_phrase():
    return randomChoice(BOT_CONFIG['failure_phrases'])


def generate_answer(text):
    # NLU
    intent = get_intent(text)
    if intent is not None:
        return randomChoice(BOT_CONFIG['intents'][intent]['responses'])

    # Generative model
    get_random_answer = generate_random_answer(text)
    if get_random_answer is not None:
        return get_random_answer

    # Return failure phrase
    return get_failure_phrase()
