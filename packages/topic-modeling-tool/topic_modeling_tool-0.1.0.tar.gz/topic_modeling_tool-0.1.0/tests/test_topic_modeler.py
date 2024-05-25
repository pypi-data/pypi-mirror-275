import unittest
from topic_modeling_tool import TopicModeler

class TestTopicModeler(unittest.TestCase):
    def test_topic_modeler(self):
        documents = [
            "I love programming in Python",
            "Python and Java are popular programming languages",
            "Machine learning and data science are exciting",
            "I enjoy learning new things in tech",
            "Artificial intelligence is the future"
        ]
        modeler = TopicModeler(n_topics=2)
        topic_distribution = modeler.fit_transform(documents)
        self.assertEqual(topic_distribution.shape[0], len(documents))
        self.assertEqual(topic_distribution.shape[1], 2)

if __name__ == '__main__':
    unittest.main()
