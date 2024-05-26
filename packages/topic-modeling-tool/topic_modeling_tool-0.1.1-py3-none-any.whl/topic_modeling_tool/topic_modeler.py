from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import pandas as pd

class TopicModeler:
    def __init__(self, n_topics=5, max_iter=10, random_state=0):
        self.n_topics = n_topics
        self.max_iter = max_iter
        self.random_state = random_state
        self.vectorizer = CountVectorizer(stop_words='english')
        self.lda_model = LatentDirichletAllocation(n_components=n_topics, max_iter=max_iter, random_state=random_state)

    def fit_transform(self, documents):
        doc_term_matrix = self.vectorizer.fit_transform(documents)
        self.lda_model.fit(doc_term_matrix)
        return self.lda_model.transform(doc_term_matrix)

    def print_topics(self, n_top_words=10):
        feature_names = self.vectorizer.get_feature_names_out()
        for topic_idx, topic in enumerate(self.lda_model.components_):
            print(f"Topic {topic_idx}:")
            print(" ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]))

    def get_topics(self, n_top_words=10):
        topics = []
        feature_names = self.vectorizer.get_feature_names_out()
        for topic_idx, topic in enumerate(self.lda_model.components_):
            topics.append([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]])
        return topics

