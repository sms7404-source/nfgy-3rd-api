

# app.py
from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)

# 모든 도메인에서의 요청을 허용합니다.
CORS(app)

@app.route('/api/random')
def random_number():
    """1부터 99 사이의 랜덤한 정수를 생성하고 JSON 형태로 반환합니다."""
    number = random.randint(1, 99)
    return jsonify({'number': number})

# ===============================================================
# 새로 추가된 API: 간단한 결정 도우미
# ===============================================================
@app.route('/api/decision')
def decision_helper():
    """
    미리 정의된 활동 목록('오늘 뭐 할지')에서 하나를 무작위로 선택하여
    JSON 형태로 반환합니다.
    """
    activities = [
        "책 읽기",
        "가벼운 산책하기",
        "좋아하는 영화 다시 보기",
        "음악 감상하며 휴식하기",
        "새로운 레시피로 요리 도전하기",
        "10분 동안 스트레칭하기",
        "아무것도 안 하고 그냥 쉬기"
    ]
    chosen_activity = random.choice(activities)
    return jsonify({'decision': chosen_activity})

if __name__ == '__main__':
    # Render.com과 같은 서비스에서는 gunicorn을 사용하므로,
    # 이 부분은 로컬 테스트용으로만 사용됩니다.
    app.run(host='0.0.0.0', port=5000)

