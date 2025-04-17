# 🎧 Whisper Video Transcriber

Whisper Video Transcriber는 `.mp4` 형식의 영상에서 음성을 추출하고, 이를 텍스트로 변환해주는 Python 기반 프로그램입니다.  
강의 영상, 설명 영상 등을 텍스트화하여 복습이나 요약에 활용할 수 있습니다.

---

## 🛠 프로그램 개요

- 📥 영상(mp4) 다운로드
- 🧠 OpenAI Whisper 모델을 이용한 음성 텍스트 변환
- 📄 변환된 내용을 `.txt` 파일로 저장
- 🖥 CPU 환경에서도 사용 가능 (다만 속도는 느릴 수 있음)

---

## 🚀 사용 방법

1. Python 환경에서 필수 라이브러리를 설치합니다:

```bash
pip install openai-whisper requests
