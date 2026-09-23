# coding-convention 작업 지침

답변은 존댓말을 사용한다. 산출물은 독자와 기존 문체에 맞춘다.

수정 전에 `skills/pydemia-coding-style/references/dictionary.md`와 관련
항목·근거를 읽는다. Markdown 사전이 원본이다. ID는 유지하고 새 규칙에는
적용 범위, 근거, 이유, 예외를 함께 기록한다.

사용자의 명시 규칙, 조건부 선호, 코드 관측, 편집상 선택을 구분한다.
assistant의 제안, Git author, fork 소유만으로 개인의 확정 취향을 만들지
않는다. 비공개 원문·credential·전체 대화 로그를 이 공개 저장소에 복제하지
않는다. 기존 공개 심볼과 사용자의 다른 checkout을 수정하지 않는다.

Python과 일반 문장은 79자, 공백 4칸, LF, UTF-8을 사용한다. URL·표·분리할 수
없는 식별자는 예외다. 도구 설정은 `docs/tooling.md`를 따른다.

검증은 `uv run --python 3.13 scripts/validate.py`,
`uv run --python 3.13 examples/python_style.py`, `git diff --check`를 사용한다.
현재 사전·예제 검사와 다른 agent에서의 실제 행동 검증은 구분해 보고한다.
