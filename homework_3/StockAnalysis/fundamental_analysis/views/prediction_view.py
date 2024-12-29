from django.http import JsonResponse
from fundamental_analysis.services.model_trainer import train_and_predict

def analyze_prediction(request):
    predictions = train_and_predict()
    return JsonResponse({"predictions": predictions, "message": "Предвидувањата се успешно направени."})