# Convention 사전

각 항목에는 고유 ID, 상태, 적용 범위, 규칙, 이유, 예외와 근거를 둔다.
ID는 제목이 바뀌어도 유지한다. 삭제된 ID는 다른 뜻으로 재사용하지 않는다.

| 상태 | 의미 | Agent 적용 |
|---|---|---|
| 명시 | 현재 요청 또는 보관된 개인 지침에 명시 | 해당 범위에서 기본 적용 |
| 선호 | 특정 요청과 여러 구현이 지지하는 방향 | 현재 문제에 맞는지 확인 후 적용 |
| 관측 | 실제 코드에서 확인했으나 개인 규칙으로 확정되지 않음 | 기존 저장소를 우선하고 강제하지 않음 |
| 조건부 | 특정 실행 환경·언어·신뢰 경계에서만 성립 | 적용 조건이 있을 때만 사용 |

상태는 품질 점수나 사용자의 별도 승인 결과가 아니다. 과거 요청의 적용 범위를
확대해 개인 전역 규칙으로 만들지 않는다. 이유가 사용자 발언이 아니라 편집상
해석이면 그 사실을 적었다. 미확정·채택하지 않은 항목은
[충돌과 결정](decisions.md)에 모았다.

## 우선순위

현재 작업의 명시적 요구 → 해당 프로젝트의 명시적 지침·formatter·실제 API
명세 → 이 사전의 명시 규칙 → 선호 → 관측 순으로 판단한다.
언어 문법과 실제 동작은 어떤 서식 선택에서도 지킨다.

사용자가 개인 스타일로의 마이그레이션을 명시했다면 대상 범위에서 설정과
코드를 함께 변경한다. 단순히 이 Skill을 사용하는 것만으로 전체 저장소의
formatter·API·공개 이름을 변경하지 않는다. 충돌 시 적용한 기준과 이유를
남기되 일반적인 지역적 선택마다 승인을 요구하지 않는다.

## 항목

| ID | 항목 | 상태 | 적용 범위 |
|---|---|---|---|
| [FMT-001](python.md#fmt-001) | 79자 줄 길이 | 명시 | 소스·주석·docstring·일반 Markdown·설정 |
| [FMT-002](python.md#fmt-002) | 공백 4칸 들여쓰기 | 명시 | Python과 별도 규칙이 없는 새 텍스트 설정 |
| [FMT-003](python.md#fmt-003) | LF와 UTF-8 | 명시 | 직접 관리하는 텍스트 파일 |
| [FMT-004](python.md#fmt-004) | 수직 인자와 닫는 괄호 | 명시 | 여러 줄 Python 선언·호출·컨테이너 |
| [FMT-005](python.md#fmt-005) | 수직 method chain | 명시 | 줄을 나누어 작성하는 Python chain |
| [FMT-006](python.md#fmt-006) | 큰따옴표 기본값 | 명시 | Python 문자열과 docstring |
| [PY-001](python.md#py-001) | 이름의 형태와 의미 | 명시 | Python 클래스·함수·변수·모듈 |
| [PY-002](python.md#py-002) | 배포 패키지의 절대 import | 명시 | 배포 패키지의 공개 사용 경로와 패키지 수준 참조 |
| [PY-003](python.md#py-003) | 내부 상대 import와 공개 API | 명시 | 외부 공개를 제한하는 subpackage 내부 |
| [PY-004](python.md#py-004) | 상수와 실행 설정의 구분 | 명시 | 모듈 수준 이름·런타임 설정 |
| [PY-005](python.md#py-005) | 타입이 있는 데이터 구조 | 선호 | Python 입력·출력 DTO와 검증 경계 |
| [PY-006](python.md#py-006) | 호출 인자의 의미 | 관측 | 옵션이 여러 개인 새 Python API |
| [PY-007](python.md#py-007) | import 부작용과 선택 의존성 | 조건부 | 재사용 라이브러리와 선택 adapter |
| [PY-008](python.md#py-008) | import 정리의 범위 | 관측 | Python import 목록 |
| [DESIGN-001](design.md#design-001) | 추적 가능한 실행 흐름 | 명시 | 구조·제어 흐름·의존 관계 |
| [DESIGN-002](design.md#design-002) | mixin 회피와 composition | 명시 | 동작 재사용과 클래스 설계 |
| [DESIGN-003](design.md#design-003) | 필요가 확인된 추상화 | 명시 | class·Protocol·factory·wrapper·공통 module |
| [DESIGN-004](design.md#design-004) | 책임별 모듈 경계 | 선호 | library·service·UI·adapter |
| [DESIGN-005](design.md#design-005) | 수명과 상태의 단일 소유자 | 선호 | runtime·connection·checkpoint·구독·공유 조회 |
| [DESIGN-006](design.md#design-006) | 문자열로 복제한 구현 정보 | 선호 | 내부 tracing·logging·catalog metadata |
| [DESIGN-007](design.md#design-007) | 의존성 도입의 판단 기준 | 선호 | 새 package·framework·외부 service |
| [DESIGN-008](design.md#design-008) | 관리 원본과 생성 결과 | 조건부 | 문서 기반 Skill·규칙·생성 artifact 관리 |
| [STATE-001](design.md#state-001) | 다른 상태는 다른 값으로 | 명시 | 조회·작업 실행·검증 상태 |
| [STATE-002](design.md#state-002) | 오류의 원인과 의미 보존 | 명시 | 예외·fallback·retry |
| [STATE-003](design.md#state-003) | 비동기 결과의 소유권 | 관측 | 동시 실행·재시도·reload가 있는 UI 또는 runtime |
| [STATE-004](design.md#state-004) | 완료 판정의 근거 | 조건부 | LLM 결과·게시·권한·DB 실행 |
| [DOC-001](workflow.md#doc-001) | 함수 docstring과 이유를 설명하는 주석 | 명시 | 코드 문서화 |
| [DOC-002](workflow.md#doc-002) | docstring 형식 | 관측 | 새 Python library의 공개 API |
| [DOC-003](workflow.md#doc-003) | 구체적인 한국어와 정확한 용어 | 명시 | 개발 문서·보고·설계 설명 |
| [DOC-004](workflow.md#doc-004) | 설계 결정의 기록 | 명시 | 대안 선택·충돌 해결·범위 변경 |
| [WORK-001](workflow.md#work-001) | 가장 작은 완결된 변경 | 명시 | 구현·수정·리뷰 |
| [WORK-002](workflow.md#work-002) | 호환성과 기존 데이터 | 명시 | 공개 API·설정·schema·이벤트·저장 상태 |
| [WORK-003](workflow.md#work-003) | 동작을 검증하는 테스트 | 명시 | 기능·오류·동시성 변경 |
| [WORK-004](workflow.md#work-004) | 완료와 검증 범위의 보고 | 명시 | 커밋·push·release·작업 결과 |
| [LANG-001](languages.md#lang-001) | TypeScript와 프런트엔드의 기존 형식 | 조건부 | TS·TSX·JS |
| [LANG-002](languages.md#lang-002) | SQL 생성과 데이터 값 | 조건부 | DB 조회·LLM 생성 SQL |
| [LANG-003](languages.md#lang-003) | 형식의 문법과 개인 서식 | 조건부 | Makefile·JSON·YAML·shell·문서 |
