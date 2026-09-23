# pydemia coding convention

pydemia의 명시적 요청, 직접 관리한 코드·문서, Codex 설계 대화를 근거로
정리한 convention 사전이다. Python·YAML·Markdown·Java·Kotlin을 별도로
관리하며 서식과 구조·상태·검증의 적용 범위, 근거, 예외를 기록한다. 동일
범위의 충돌은 최신 명시적 결정을 우선한다.

- [71개 항목 사전](skills/pydemia-coding-style/references/dictionary.md)
- [Agent Skill](skills/pydemia-coding-style/SKILL.md)
- [근거와 조사 범위](skills/pydemia-coding-style/references/evidence.md)
- [충돌·선택 이유·미확정 항목](skills/pydemia-coding-style/references/decisions.md)
- [편집 설정과 검증](docs/tooling.md)
- [skills.pydemia.ai 편입 안내](docs/publication.md)
- [검증 기록](docs/validation.md)
- [전수 목록·내용 검사 범위](docs/research-coverage.md)

79자·공백 4칸·LF·UTF-8·큰따옴표와 사용자가 제시한 Python 줄바꿈을
개인 기본값으로 삼는다. 기존 프로젝트의 설정과 충돌하면 현재 작업의
요구와 프로젝트 기준을 먼저 확인한다. 과거 코드의 모든 패턴을 취향으로
간주하지 않는다.

## Agent에서 사용

`skills/pydemia-coding-style/` 전체가 독립 Skill이다. 사용하는 agent의
Skill 검색 경로에 이 디렉터리를 복사하거나 저장소 경로를 직접 알려 준다.
`SKILL.md`만 복사하면 references가 빠진다. 기존 설치가 있으면 먼저 diff를
확인하며 이 저장소를 받았다는 이유만으로 전역 설정을 덮어쓰지 않는다.

예시 요청:

```text
pydemia-coding-style을 적용해 이 Python 모듈을 수정해 주세요.
기존 공개 API와 저장소 설정을 유지하고 변경한 코드에만 적용해 주세요.
규칙 충돌이 있으면 적용한 기준과 이유를 알려 주세요.
```

## 검증

Python 3.11 이상에서 실행한다.

```bash
uv run --python 3.13 scripts/validate.py
uv run --python 3.13 examples/python_style.py
```

이 저장소는 사전과 Skill의 원본이다. 다른 개인 저장소와 실제 웹사이트의
설정·배포는 이 저장소 push만으로 변경되지 않는다.
