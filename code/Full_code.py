import whisper
import requests
import os

# 저장 경로 설정
save_dir = r"C:\Users\ghkdw\Desktop\vid to txt"  //본인 저장 경로 설정하세요
os.makedirs(save_dir, exist_ok=True)

# 기본 파일 이름
base_video_name = "ssmovie"
base_text_name = "transcription"
video_ext = ".mp4"
text_ext = ".txt"

# 중복되지 않는 파일명 생성 함수
def get_unique_filename(base_name, extension, directory):
    count = 0
    while True:
        name = f"{base_name}{count if count > 0 else ''}{extension}"
        full_path = os.path.join(directory, name)
        if not os.path.exists(full_path):
            return full_path
        count += 1

# 1. 영상 다운로드
video_url = "여기에 .mp4 링크를 가져오세요"
video_path = get_unique_filename(base_video_name, video_ext, save_dir)
print("🔽 영상 다운로드 중...")
response = requests.get(video_url, stream=True)
with open(video_path, "wb") as f:
    for chunk in response.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)
print(f"✅ 다운로드 완료! 저장 경로: {video_path}")

# 2. Whisper 모델 로드 및 텍스트 변환
print("🧠 Whisper 모델 로딩 중...")
model = whisper.load_model("base")
print("📝 텍스트 추출 중...")
result = model.transcribe(video_path)

# 3. 텍스트 파일로 저장
text_path = get_unique_filename(base_text_name, text_ext, save_dir)
with open(text_path, "w", encoding="utf-8") as f:
    f.write(result["text"])
print(f"✅ 변환 완료! 텍스트는 '{text_path}' 파일로 저장되었습니다.")
