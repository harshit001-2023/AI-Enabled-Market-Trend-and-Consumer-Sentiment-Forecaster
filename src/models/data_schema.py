# This is like a Java class for holding data
class ConsumerData:
    def __init__(self, source, text, date, sentiment=None, topic=None):
        self.source = source  # e.g., "YouTube"
        self.text = text  # Raw comment/review
        self.date = date  # e.g., "2024-09-29"
        self.sentiment = sentiment  # We'll add later: "positive", "negative", etc.
        self.topic = topic  # We'll add later: e.g., "battery issue"

    def to_dict(self):  # Like toString() in Java
        return {
            "source": self.source,
            "text": self.text,
            "date": self.date,
            "sentiment": self.sentiment,
            "topic": self.topic
        }