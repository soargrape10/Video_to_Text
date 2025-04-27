# 🎧 Video Transcriber (Windows 전용)

Whisper Video Transcriber는 `.mp4` 형식의 영상에서 음성을 추출하고 텍스트로 변환해주는 Python 기반 프로그램입니다.  
강의 영상, 설명 영상 등의 내용을 텍스트로 변환하여 복습이나 정리에 활용할 수 있습니다.

---

## 🛠 프로그램 개요

- 📥 영상(mp4) 다운로드
- 🧠 OpenAI Whisper 모델을 이용한 음성 텍스트 변환
- 📄 변환된 내용을 `.txt` 파일로 저장
- 🖥 CPU 환경에서도 작동 가능 (다만 GPU 사용 시 더 빠르게 처리 가능)

---

## 🚀 설치 및 사용 방법

> ⚡ 처음 Windows PC에 Python과 VSCode가 설치되어 있지 않은 상황을 가정합니다.

### 1. Python 설치

- [Python 공식 웹사이트](https://www.python.org/)에서 최신 버전을 설치합니다.
- 설치 시, **"Add Python to PATH"** 옵션을 반드시 체크합니다.

### 2. Visual Studio Code 설치 (권장)

- [VSCode 공식 웹사이트](https://code.visualstudio.com/)에서 설치합니다.

### 3. ffmpeg 설치 및 환경 변수 등록

```bash
# ffmpeg 설치
choco install ffmpeg
```
---

## 4. ffmpeg 환경 변수 등록 방법
- Windows 검색창에 "환경 변수" 입력 → 시스템 환경 변수 편집 클릭
- "환경 변수(N)" 버튼 클릭
- 시스템 변수 목록에서 Path 선택 후 편집
- "새로 만들기" 클릭 후 다음 경로 추가:
  ```bash
    C:\ProgramData\chocolatey\bin
  ```
- 모두 저장 후, 컴퓨터를 재부팅하거나 VSCode를 재시작합니다.
---

## 5. 필수 Python 라이브러리 설치
- 터미널(또는 VSCode 터미널)에서 다음 명령어를 입력해 필요한 라이브러리를 설치합니다:

  ```bash
  pip install openai-whisper requests
  ```
## 6. 🔥 실행하면 끝!
