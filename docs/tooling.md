# 편집 설정과 검증

[.editorconfig](../.editorconfig)는 LF·UTF-8·들여쓰기·79자 편집 힌트를,
[.gitattributes](../.gitattributes)는 Git 텍스트 개행을 설정한다.
EditorConfig의 max_line_length만으로 긴 줄이 모두 검사되지는 않는다.
포맷터는 프로젝트에서 선택하며 이 사전은 특정 도구를 지정하지 않는다.

Python 3.11 이상에서 다음 검사를 실행한다.

```bash
uv run --python 3.13 scripts/validate.py
uv run --python 3.13 examples/python_style.py
```

자체 validator는 UTF-8·LF, 링크와 anchor, 규칙 ID의 중복·색인 누락,
Python 파일과 fence의 문법, TOML 문법, Markdown 줄 길이를 확인한다.
AST 검사는 문법 확인이며 fence 예제의 외부 package import나 실제 실행을
검증하는 것은 아니다. Python의 미사용 import·정렬·quote·줄 길이를 모두
검사하지는 않는다. 실행 예제는 chain 결과와 원본 불변 등의 동작을 확인한다.

## 다른 저장소로 가져갈 때

기존 편집·검사 설정과 필요한 항목만 병합한다. 이 저장소의 설정 파일을
그대로 덮어쓰면 기존 기준이 바뀔 수 있다. 명시적 마이그레이션 범위 없이
전체 repository를 재서식하지 않는다. YAML 2칸과 Makefile 탭은 형식별
예외이며 Python 기본값과 구분한다.
