FROM python:3.7-slim

WORKDIR /hongminyeong

COPY requirements.txt ./

# 의존성 설치 및 캐시 정리
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# 애플리케이션 포트 노출
EXPOSE 5000

# 애플리케이션 실행
CMD ["python", "hongminyeong.py"]
