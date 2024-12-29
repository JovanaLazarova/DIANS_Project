from django.http import JsonResponse
from fundamental_analysis.services.sentiment_analyzer import analyze_news_sentiment

def analyze_sentiment(request):
    sentiment = analyze_news_sentiment("Company profits have increased this quarter.")
    return JsonResponse({"sentiment": sentiment, "message": "Сентимент анализата е успешно завршена."})