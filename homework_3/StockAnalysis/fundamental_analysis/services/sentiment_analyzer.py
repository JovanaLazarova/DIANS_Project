from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_news_sentiment(news):
    analyzer = SentimentIntensityAnalyzer()
    return analyzer.polarity_scores(news)