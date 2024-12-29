from django.urls import path
from .views import finance_view, sentiment_view, prediction_view

urlpatterns = [
    path('', finance_view.index, name='index'),
    path('analyze/finance/', finance_view.analyze_finance, name='analyze_finance'),
    path('analyze/sentiment/', sentiment_view.analyze_sentiment, name='analyze_sentiment'),
    path('analyze/prediction/', prediction_view.analyze_prediction, name='analyze_prediction'),
]