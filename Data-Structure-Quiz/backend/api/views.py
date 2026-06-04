from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import QuizRecord  

@csrf_exempt
def save_quiz_score(request):
    if request.method == 'POST':
        try:
          
            data = json.loads(request.body)
            
          
            user_nickname = data.get('nickname', '匿名玩家')
            user_score = data.get('score', 0)
            

            QuizRecord.objects.create(
                nickname=user_nickname,
                score=user_score
            )
            
            print(f"🎉 成功存入一筆戰績：{user_nickname} 獲得了 {user_score} 分！")
            
          
            response = JsonResponse({"status": "success", "message": "成績上傳成功！"})
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
            response["Access-Control-Allow-Headers"] = "Content-Type"
            return response
            
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
            
   
    elif request.method == 'OPTIONS':
        response = JsonResponse({})
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type"
        return response

    return JsonResponse({"error": "Only POST method allowed"}, status=405)