# 충돌과 결정

현재 사용자 요청은 개인 기본값을 새로 명시한 자료다. 기존 코드의 빈도만으로
그 요청을 덮어쓰지 않는다. 다음은 사전을 만들며 채택한 기준과 유보 범위다.

| 쟁점 | 관측한 차이 | 이번 선택과 이유 | 근거 |
|---|---|---|---|
| 79·100·120자 | 현재 요청·개인 지침은 79, 최근 Python은 100, 과거 backend는 120 | 개인 기본은 79. 기존 설정은 별도 마이그레이션 요청 전까지 보존 | [U00](evidence.md#u00), [L01](evidence.md#l01), [L03](evidence.md#l03), [G04](evidence.md#g04) |
| 괄호 들여쓰기 | 오래된 batcher는 선언 인자·닫는 괄호 정렬이 현재 예제와 다름 | 현재 사용자가 준 형태를 채택. 예전 파일을 정답 예제로 복사하지 않음 | [U00](evidence.md#u00), [G01](evidence.md#g01) |
| method chain | Ruff 0.16.8 기본 formatter가 수직 chain을 한 줄로 합침 | 사전 예제는 수직형 유지. lint와 format을 구분하고 최소 범위 suppression 또는 기존 formatter 우선 적용 | [T01](evidence.md#t01) |
| quote | unipy의 작은따옴표와 최근 큰따옴표 혼재 | 큰따옴표 중심, escape·외부 문법 예외. TS로 일괄 확장하지 않음 | [U00](evidence.md#u00), [G03](evidence.md#g03), [G05](evidence.md#g05) |
| 절대·상대 import | 공개 package와 내부 module에서 둘 다 사용 | 공개 접근은 절대, 내부 캡슐화는 상대. 패키징과 상대 import는 양립 | [U00](evidence.md#u00), [G01](evidence.md#g01), [G02](evidence.md#g02) |
| Pydantic·dataclass | Pydantic 요청과 IAM의 frozen dataclass가 공존 | 입력 검증·DTO는 Pydantic 선호. 내부 값까지 전환하지 않음 | [U05](evidence.md#u05), [G04](evidence.md#g04) |
| 추상화·상속 | 공통 template·factory·상속 요청과 mixin 회피·추상화 제한이 공존 | 실제 확장 지점에는 간결한 interface. 간접 계층 자체가 목적이면 만들지 않음 | [U01](evidence.md#u01), [L01](evidence.md#l01) |
| 함수 20줄 | 과거 설계 요청에 짧은 함수 기준이 포함됨 | 이후 개인 지침의 의미 있는 책임 추출을 우선. 강제 길이 검사는 추가하지 않음 | [U01](evidence.md#u01), [L01](evidence.md#l01) |
| docstring | NumPy식·Google식이 모두 존재 | 신규 library의 후보 기본은 NumPy식 관측, 기존 형식 유지 | [G01](evidence.md#g01), [G03](evidence.md#g03), [G04](evidence.md#g04) |
| YAML 원본 폐기 | 특정 업무조건 정의를 Markdown으로 관리하도록 교정 | 관리 원본의 중복을 제한. YAML·JSON 파일 전체를 금지하지 않음 | [U08](evidence.md#u08), [L04](evidence.md#l04) |

## 과거 Q&A에서 확인한 선택

- 공통 agent·tool interface를 요청한 뒤 다시 간결한 factory 흐름과
  유지보수를 강조했다. 추상화의 존재보다 확장 방법과 실행 경로를 읽기
  쉬운지가 선택 기준이다. [U01](evidence.md#u01)
- 인가 엔진을 따로 추가하는 이득을 질문하고 설명을 받은 뒤 그 구조의
  설계서 작성을 요청했다. 인증·인가 책임 분리와 조회 권한 처리의 이득을
  비교한 결정이며 해당 제품의 전역 채택 근거는 아니다.
  [U07](evidence.md#u07)
- assistant가 업무조건 원본을 YAML·JSON으로 되돌린 안을 사용자가
  교정했다. Markdown을 편집 원본으로 삼는 방향은 이 교정으로 확인된다.
  SQL 생성물과 선택 이유는 실행 이력으로 남기도록 별도 요청했다.
  [U08](evidence.md#u08)
- UI framework의 호환성은 구현계획에 포함하기 전에 검증하도록 요청했다.
  비교 질문만으로 최종 제품 선택이 확정됐다고 해석하지 않았다.
  [U09](evidence.md#u09)

## 현재 기본으로 채택하지 않은 패턴

unipy의 wildcard import·주석 처리된 구현, 오래된 batcher의 광범위한 예외
처리 후 빈 반환, 초기 설정 예제의 과도한 모듈 설정은 과거 구현 관측이다.
최근 명시 지침과 충돌하므로 권장 예제로 복제하지 않았다. 기존 코드에 이
패턴이 존재한다는 사실만으로 이번 작업에서 결함 수정이나 재서식을 하지는
않았다. [G01](evidence.md#g01), [G03](evidence.md#g03),
[G06](evidence.md#g06), [L01](evidence.md#l01)

Python 버전, build backend, package manager, Ruff rule 전체, docstring 형식,
TS formatter, SQL 서식, Go·Rust·Java 관례는 개인 전역 규칙으로 확정하지
않았다. 이 저장소의 Python 3.11 검사 기준과 Ruff 설정은 사전을 실행·검증하기
위한 선택이다. 특정 과거 프로젝트의 toolchain을 모든 저장소에 강제하지 않는다.
