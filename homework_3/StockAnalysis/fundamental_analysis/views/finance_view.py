from django.shortcuts import render
from django.http import JsonResponse
from fundamental_analysis.services.data_fetcher import fetch_financial_data

# Основна страница
def index(request):
    return render(request, 'fundamental_analysis/index.html')

# Анализа на финансиски податоци
def analyze_finance(request):
    data = fetch_financial_data()
    return JsonResponse({"financial_data": data, "message": "Финансиските податоци се успешно анализирани."})