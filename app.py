from flask import Flask, render_template_string
import secrets
import datetime

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ru">
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>Криптографическая утилита безопасности - Вариант 22</title>
 <style>
 body { font-family: 'Segoe UI', sans-serif; background-color: #0e1e38; color: #ffffff; margin: 0; padding: 40px; display: flex; justify-content: center; align-items: center; min-height: 80vh; }
 .crypto-container { background: #1a2f4c; padding: 40px; border-radius: 12px; box-shadow: 0 8px 30px rgba(0,0,0,0.3); max-width: 700px; width: 100%; border-top: 6px solid #0052cc; }
 h1 { color: #4c9aff; font-size: 24px; border-bottom: 1px solid #2c4a6f; padding-bottom: 10px; margin-top: 0; }
 .token-area { font-family: 'Courier New', monospace; background: #0b1a30; padding: 15px; border-radius: 6px; color: #36b37e; word-break: break-all; font-size: 16px; font-weight: bold; margin: 20px 0; border: 1px solid #2c4a6f; }
 .info-table { width: 100%; border-collapse: collapse; margin-top: 20px; }
 .info-table td { padding: 12px; border-bottom: 1px solid #2c4a6f; font-size: 14px; }
 .label { color: #97a0af; font-weight: 500; }
 .status-online { background-color: #ffab00; color: #0e1e38; padding: 3px 10px; border-radius: 4px; font-weight: bold; font-size: 12px; }
 .footer { margin-top: 30px; font-size: 11px; color: #6b778c; text-align: center; }
 </style>
</head>
<body>
 <div class="crypto-container">
 <h1>Криптографическая утилита безопасности БГУИР (гр. 363441)</h1>
 <p>Данный interface генерирует уникальные сессионные ключи доступа для веб-интерфейсов. Развернуто автоматически через Bitbucket Pipelines по модели GitLab Flow.</p>
 
 <div class="label">Сгенерированный защищенный токен сессии (URL-Safe Base64):</div>
 <div class="token-area">{{ generated_token }}</div>

 <table class="info-table">
 <tr>
 <td class="label">Статус службы авторизации</td>
 <td><span class="status-online" style="background-color: #36b37e; color: white;">ONLINE</span></td>
 </tr>
 <tr>
 <td class="label">Время генерации токена (Серверное)</td>
 <td><strong>{{ gen_time }}</strong></td>
 </tr>
 <tr>
 <td class="label">Срок действия токена (TTL)</td>
 <td><strong>{{ expire_time }} (осталось 15 мин)</strong></td>
 </tr>
 </table>
 <div class="footer">
 Контрольная работа • Вариант 22 • 2026
 </div>
 </div>
</body>
</html>
"""

@app.route('/')
def index():
    token = secrets.token_urlsafe(32)
    now = datetime.datetime.now()
    expire = now + datetime.timedelta(minutes=15)
    return render_template_string(
        HTML_TEMPLATE,
        generated_token=token,
        gen_time=now.strftime("%Y-%m-%d %H:%M:%S"),
        expire_time=expire.strftime("%Y-%m-%d %H:%M:%S")
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
