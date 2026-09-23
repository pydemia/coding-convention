# 검증 기록

기준일: 2026-09-23. 이 기록은 사전·Skill bundle·설정·예제에 대한 검사다.
조사한 외부 저장소의 전체 테스트나 실제 사이트 배포를 뜻하지 않는다.

| 검사 | 결과 | 범위 |
|---|---|---|
| `uv run --python 3.13 scripts/validate.py` | 통과 | UTF-8·LF·개행, Markdown 링크·anchor, 71개 ID·색인, TOML, Python 문법 |
| `uv run --python 3.13 examples/python_style.py` | 통과 | chain 결과·원본 불변·선택 열·정렬 인자 |
| skill-creator `quick_validate.py` | 통과 | Skill frontmatter·이름·미완성 scaffold 검사 |
| validator 실패 입력 확인 | 통과 | 임시 복사본의 깨진 anchor·Python fence 오류·색인 불일치 탐지 |
| 독립 bundle 상대 링크 검사 | 통과 | Skill 디렉터리만 복사해도 references가 내부에서 연결됨 |
| `git diff --check` | 통과 | 공백 오류 검사. 최초 커밋 전에는 staged diff도 확인 |
| 공개 근거 범위 확인 | 통과 | 참조 commit·파일의 존재와 인용 line 범위 대조 |
| credential 패턴 검사 | 발견 없음 | 게시 파일의 token·private key·credential 포함 URL 패턴. 완전한 비밀 탐지 보장은 아님 |

현재 호스트에서 이 저장소의 기본 `python3`는 3.9.6이어서 tomllib을 import할
수 없었다. 문서에 명시한 Python 3.11 이상을 충족하도록 uv의 Python 3.13
환경에서 검증했다. 이 버전은 검증 환경이며 개인 전체의 Python 버전 규칙이
아니다. 사용자 전역 Python 설정은 변경하지 않았다.

독립된 다른 agent에게 실제 개발 과제를 주는 행동 검증, 모든 언어·framework에
대한 적용 검증, skills.pydemia.ai의 exporter·CMS 편입·배포는 수행하지 않았다.
Python·Java·Kotlin fence는 문법 검사만 했으며 가상의 import 대상이나 JVM
프로그램까지 실행하지 않았다.
외부 근거의 코드 품질·최신 API 호환성도 이 사전 검사와 별개다.

## 확대 조사 후 추가 검증

| 검사 | 결과 | 범위 |
|---|---|---|
| GitHub 수집 목록 대조 | 통과 | 인증된 non-fork 239개가 clone 212·빈 clone 4·source-only 23으로 모두 분류됨 |
| 소스 snapshot 대조 | 통과 | 수집 파일 11,769개 존재 확인. notebook 확장자 353개는 별도 점검, 나머지는 Git blob hash 대조 |
| clone HEAD·origin·작업 트리 | 확인 | 216개 HEAD 상태·credential 없는 origin 확인. 2개는 대소문자 경로 충돌을 별도 보존·기록 |
| 전수 내용 검색 | 완료 | 393개 입력 위치, UTF-8 텍스트 64,988개. 중복 제외 39,985개. 제외 항목은 조사 범위 문서에 명시 |
| 추가 언어 색인·metadata | 통과 | Java·Kotlin·YAML·Markdown 항목까지 자동 수집해 총 71개 ID 대조 |
| validator 실패 입력 | 통과 | Java metadata 누락·Kotlin 색인 불일치·깨진 anchor·Python 문법 오류 탐지 |
| repos 제외 | 통과 | 임시 복사본의 repos에 binary를 넣어도 사전 validator가 순회·검사하지 않음 |
| Java·Kotlin 예제 | 문법 통과 | tree-sitter grammar로 각각 1개 예제 parse. compile·실행은 수행하지 않음 |
| YAML 예제 | 통과 | safe_load 성공, 정수 타입·placeholder 유지·block scalar의 중간/끝 개행 확인 |

macOS에서 `javac` 명령 경로는 있으나 실제 Java runtime은 설치되어 있지
않았고 Kotlin compiler도 없었다. 문법 검사를 compile 성공으로 표시하지
않았다. 외부 예제 코드는 실행하지 않았다. 소스 snapshot의 notebook 확장자 353개
중 352개는 JSON notebook이며 code output을 비웠다. 이 중 구형 v3 20개도
worksheet 출력까지 정리했다. JSON이 아닌 원본 1개는 별도로 Git blob hash를
확인했고 실행 가능한 notebook으로 세지 않았다.

처음 수집한 큰 저장소에 포함됐던 데이터 JSON·text 사본 9,718개는 코드
수집 범위에서 제외하고 이번 작업의 다운로드 사본만 제거했다. 원격 자료와
사용자의 다른 로컬 checkout은 수정하지 않았다. 원래 UTF-8 텍스트가 아닌
외부 fixture, binary, 이미 사라진 경로는 검사 통과 파일에 포함하지 않았다.
