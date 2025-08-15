# MIDI to Music Box - Executable Files
MIDI 뮤직박스 변환기 - 실행 파일

## Files (파일)
- **MidiToMusicBox_C.exe**: For C-type 30-note music box (C형 30노트 뮤직박스용)
- **MidiToMusicBox_F.exe**: For F-type 30-note music box (F형 30노트 뮤직박스용)

## How to Use (사용법)
1. Choose the appropriate executable for your music box type  
   뮤직박스 타입에 맞는 적절한 실행 파일을 선택하세요

2. Create a new folder and copy the executable file  
   새 폴더를 만들고 실행 파일을 복사하세요

3. Place your MIDI files (.mid, .midi) in the same folder  
   MIDI 파일(.mid, .midi)을 같은 폴더에 넣으세요

4. Double-click the executable to run  
   실행 파일을 더블클릭하여 실행하세요

5. DXF files will be generated in the `output` folder  
   DXF 파일이 `output` 폴더에 생성됩니다

## Note Configurations (노트 구성)

### C-type (C형)
C3, D3, G3, A3, B3, C4, D4, E4, F4, F#4, G4, G#4, A4, A#4, B4, C5, C#5, D5, D#5, E5, F5, F#5, G5, G#5, A5, A#5, B5, C6, D6, E6

### F-type (F형)
F3, G3, C4, D4, E4, F4, G4, A4, A#4, B4, C5, C#5, D5, D#5, E5, F5, F#5, G5, G#5, A5, A#5, B5, C6, C#6, D6, D#6, E6, F6, G6, A6

## Notes (참고사항)
- No Python installation required (Python 설치 불필요)
- Supports batch processing of multiple MIDI files (여러 MIDI 파일 일괄 처리 지원)
- Automatically calculates optimal strip width (최적 스트립 폭 자동 계산)
- Console window will show processing progress (콘솔 창에서 처리 진행 상황 표시)
