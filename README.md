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

### 3. ffmpeg 설치

- Windows 터미널(명령 프롬프트 또는 PowerShell)을 열고 다음 명령어를 입력합니다:

```bash
choco install ffmpeg
