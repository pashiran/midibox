# MIDI to Music Box (MIDI 뮤직박스 변환기)
Turns .midi files into .dxf files, primarily for music box paper strips with a high degree of customizability.  
MIDI 파일을 DXF 파일로 변환하여 뮤직박스 종이 테이프를 제작할 수 있습니다. 높은 사용자 정의 기능을 제공합니다.

Allows for variable dimensions of the strip, as well as different sized stock paper that will be cut. Will output a new .dxf file for each page of paper needed.  
스트립의 가변 크기와 다양한 종이 규격을 지원합니다. 필요한 각 페이지마다 새로운 DXF 파일을 출력합니다.

## Features (기능)
- **30-note Music Box Support (30노트 뮤직박스 지원)**: Supports both C-type and F-type 30-note music box configurations  
  C형과 F형 30노트 뮤직박스 구성을 모두 지원합니다
- **Batch Processing (일괄 처리)**: Processes all MIDI files in the folder automatically  
  폴더 내 모든 MIDI 파일을 자동으로 처리합니다
- **Dynamic Width Calculation (동적 폭 계산)**: Automatically calculates optimal strip width based on song length  
  곡 길이에 따라 최적의 스트립 폭을 자동으로 계산합니다
- **Standalone Executable (독립 실행 파일)**: No Python installation required  
  Python 설치가 필요하지 않습니다

## How to Use (사용 방법)

### Method 1: Using Executable Files (실행 파일 사용)
1. Download the appropriate executable from the `releases` folder:  
   `releases` 폴더에서 적절한 실행 파일을 다운로드하세요:
   - `MidiToMusicBox_C.exe` for C-type 30-note music box (C형 30노트 뮤직박스용)
   - `MidiToMusicBox_F.exe` for F-type 30-note music box (F형 30노트 뮤직박스용)

2. Place your MIDI files in the same folder as the executable  
   MIDI 파일을 실행 파일과 같은 폴더에 넣으세요

3. Run the executable file  
   실행 파일을 실행하세요

4. DXF files will be automatically generated in the `output` folder  
   DXF 파일이 `output` 폴더에 자동으로 생성됩니다

### Method 2: Using Python Script (Python 스크립트 사용)
1. Put your midi file in the `midi` directory  
   MIDI 파일을 `midi` 디렉토리에 넣으세요

2. In `main.py`, change `docName` to the path to your midi file, and edit any relevant global variables  
   `main.py`에서 `docName`을 MIDI 파일 경로로 변경하고 관련 전역 변수를 편집하세요

3. Run `./midibox/bin/python3 gui.py` to generate your DXF file  
   `./midibox/bin/python3 gui.py`를 실행하여 DXF 파일을 생성하세요

## Note Configurations (노트 구성)

### C-type (C형)
C3, D3, G3, A3, B3, C4, D4, E4, F4, F#4, G4, G#4, A4, A#4, B4, C5, C#5, D5, D#5, E5, F5, F#5, G5, G#5, A5, A#5, B5, C6, D6, E6

### F-type (F형)
F3, G3, C4, D4, E4, F4, G4, A4, A#4, B4, C5, C#5, D5, D#5, E5, F5, F#5, G5, G#5, A5, A#5, B5, C6, C#6, D6, D#6, E6, F6, G6, A6

## Requirements (요구사항)
- Python 3.x (for script usage / 스크립트 사용시)
- Required packages: mido, pretty_midi, ezdxf (for script usage / 스크립트 사용시)
- For executable files: No additional requirements (실행 파일의 경우: 추가 요구사항 없음)
