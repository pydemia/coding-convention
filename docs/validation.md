# 검증 기록

기준일: 2026-09-23. 이 기록은 사전·Skill bundle·설정·예제에 대한 검사다.
조사한 외부 저장소의 전체 테스트나 실제 사이트 배포를 뜻하지 않는다.

| 검사 | 결과 | 범위 |
|---|---|---|
| `uv run --python 3.13 scripts/validate.py` | 통과 | UTF-8·LF·개행, Markdown 링크·anchor, 37개 ID·색인, TOML, Python 문법 |
| `uvx ruff==0.16.8 check .` | 통과 | 이 저장소의 Python lint·quote·79자·import |
| `uv run --python 3.13 examples/python_style.py` | 통과 | chain 결과·원본 불변·선택 열·정렬 인자 |
| skill-creator `quick_validate.py` | 통과 | Skill frontmatter·이름·미완성 scaffold 검사 |
| validator 실패 입력 확인 | 통과 | 임시 복사본의 깨진 anchor·Python fence 오류·색인 불일치 탐지 |
| 독립 bundle 상대 링크 검사 | 통과 | Skill 디렉터리만 복사해도 references가 내부에서 연결됨 |
| `git diff --check` | 통과 | 공백 오류 검사. 최초 커밋 전에는 staged diff도 확인 |
| 공개 근거 범위 확인 | 통과 | 참조 commit·파일의 존재와 인용 line 범위 대조 |
| credential 패턴 검사 | 발견 없음 | 게시 파일의 token·private key·credential 포함 URL 패턴. 완전한 비밀 탐지 보장은 아님 |

Ruff 0.16.8 기본 formatter가 사용자 chain을 합치는 것을 재현했다. lint는
통과했으며 문장 전체를 fmt off/on으로 감싼 예제는 formatter가 유지했다.
이 저장소는 의도적으로 formatter 통과를 사전의 완료 조건으로 삼지 않는다.

현재 호스트에서 이 저장소의 기본 `python3`는 3.9.6이어서 tomllib을 import할
수 없었다. 문서에 명시한 Python 3.11 이상을 충족하도록 uv의 Python 3.13
환경에서 검증했다. 이 버전은 검증 환경이며 개인 전체의 Python 버전 규칙이
아니다. 사용자 전역 Python 설정은 변경하지 않았다.

독립된 다른 agent에게 실제 개발 과제를 주는 행동 검증, 모든 언어·framework에
대한 적용 검증, skills.pydemia.ai의 exporter·CMS 편입·배포는 수행하지 않았다.
Markdown fence는 문법 검사만 했으며 가상의 import 대상까지 실행하지 않았다.
외부 근거의 코드 품질·최신 API 호환성도 이 사전 검사와 별개다.
