# 도구 설정

[.editorconfig](../.editorconfig)는 LF·UTF-8·들여쓰기·79자 편집 힌트를,
[.gitattributes](../.gitattributes)는 Git 텍스트 개행을 설정한다.
EditorConfig의 max_line_length만으로 긴 줄이 모두 검사되지는 않는다.
[ruff.toml](../ruff.toml)은 이 저장소와 Python 예제의 lint profile이다.

```bash
uvx ruff==0.16.8 check .
python3 scripts/validate.py
```

Ruff는 syntax 관련 오류·미사용 import·import 정렬·79자·quote를 검사한다.
자체 validator는 UTF-8·LF, 링크와 anchor, 규칙 ID의 중복·색인 누락,
Python fence 문법, 일반 문장의 줄 길이를 확인한다. AST 검사는 문법 확인이며
fence 예제의 외부 package import나 실제 실행을 검증하는 것은 아니다.

## method chain과 formatter

Ruff 0.16.8의 기본 모드에서 다음 입력을 `ruff format --diff`로 확인했다.

```python
result = (
    instance
    .method1()
    .method2()
)
```

출력은 다음과 같다.

```python
result = instance.method1().method2()
```

이 저장소는 사전의 예제를 유지하기 위해 lint를 실행하고 formatter의 출력을
필수로 삼지 않는다. format 설정의 trailing comma 옵션도 모든 chain을
이 형태로 유지해 주지는 않는다. 이미 formatter를 사용하는 프로젝트에서
수직 chain을 반드시 보존해야 한다면 문장 단위로 최소 범위를 보호할 수 있다.

```python
# fmt: off
result = (
    instance
    .method1()
    .method2()
)
# fmt: on
```

문장 단위 suppression은 [Ruff 공식 문서]에서 지원한다. formatter 버전이나
preview mode를 바꾸면 해당 예제로 결과를 다시 확인한다. 설정만 보고 개인
서식이 완전히 자동화되었다고 보고하지 않는다.

[Ruff 공식 문서]: https://docs.astral.sh/ruff/formatter/#format-suppression

## 다른 저장소로 가져갈 때

기존 pyproject.toml·ruff.toml·EditorConfig와 필요한 항목만 병합한다.
이 저장소의 설정 파일을 그대로 덮어쓰면 기존 검사·ignore·Python 버전이
바뀔 수 있다. 명시적 마이그레이션 범위 없이 전체 repository를 재서식하지
않는다. YAML 2칸과 Makefile 탭은 형식별 예외이며 Python 기본값과 구분한다.
