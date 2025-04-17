# 🎧 Video Transcriber (Window.ver)

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
2. ffmpeg가 시스템에 설치 되어있어야 합니다
3. 환경변수에 choco 경로 추가하기 <- 중요


윈도우 검색창에 "환경 변수" 검색 → 시스템 환경 변수 편집 클릭
하단 "환경 변수(N)" 클릭

시스템 변수에서 Path 더블 클릭

"새로 만들기" 클릭 후 아래 경로 추가:
-> makefile
-> C:\ProgramData\chocolatey\bin
모두 확인 누르고 저장 → PC 재부팅 or VSCode 재시작

```bash
pip install openai-whisper requests

choco install ffmpeg
