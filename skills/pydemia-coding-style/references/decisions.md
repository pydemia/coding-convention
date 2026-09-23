# 충돌과 결정

현재 사용자 요청은 개인 기본값을 새로 명시한 자료다. 기존 코드의 빈도만으로
그 요청을 덮어쓰지 않는다. 다음은 사전을 만들며 채택한 기준과 유보 범위다.

| 쟁점 | 관측한 차이 | 이번 선택과 이유 | 근거 |
|---|---|---|---|
| 79·100·120자 | 현재 요청·개인 지침은 79, 최근 Python은 100, 과거 backend는 120 | 개인 기본은 79. 기존 설정은 별도 마이그레이션 요청 전까지 보존 | [U00](evidence.md#u00), [L01](evidence.md#l01), [L03](evidence.md#l03), [G04](evidence.md#g04) |
| 괄호 들여쓰기 | 오래된 batcher는 선언 인자·닫는 괄호 정렬이 현재 예제와 다름 | 현재 사용자가 준 형태를 채택. 예전 파일을 정답 예제로 복사하지 않음 | [U00](evidence.md#u00), [G01](evidence.md#g01) |
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

Python 버전, build backend, package manager, docstring 형식,
TS formatter, SQL 서식, Go·Rust·Java 세부 관례는 개인 전역 규칙으로 확정하지
않았다. 이 저장소의 Python 3.11 검사 기준은 사전을 실행·검증하기 위한
선택이다. 특정 과거 프로젝트의 toolchain을 모든 저장소에 강제하지 않는다.
2026-09-23 사용자 결정에 따라 포맷터 선택은 프로젝트에 맡기고 특정 포맷터의
설정·검증 명령·출력 비교는 사전에서 제외한다.

## 최신 기준을 적용한 변경 이력

이 표는 같은 범위에서 확인되는 사용자 결정을 시간순으로 비교한다. 단순한
정책 변경과 반복 번복은 구분한다. 최신 사용자 결정이 이전 문서에 아직
반영되지 않았다면 문서가 오래된 것이며 사용자 결정의 효력이 사라지는 것은
아니다. 기록 시각이 이관 시점인 대화는 session 내부 순서도 함께 확인한다.

| 항목·범위 | 이전 → 후속 결정 | 현재 적용 기준 | 판단 |
|---|---|---|---|
| 개인 기본 서식 | 과거 저장소별 88·100·120자 → 현재 요청 79자 | 새 개인 기본은 79자. 기존 프로젝트 설정은 명시적 변경 범위 확인 | 최신 개인 기준. 서로 다른 저장소 수치는 번복이 아님 |
| 같은 context 압축 설정 | 2026-05-08 비율 0.7 → 05-11 비율 0.5와 config 지원 | 해당 설계에서는 후속 0.5. 새 제품의 전역 기본으로 고정하지 않음 | 단방향 조정 |
| adaptive memory | 05-26 compact/window 계획 → 05-29 work-memory는 window만, context-memory는 압축 | 서로 다른 데이터 성격에 맞춘 후속 구분 | 범위 구체화 |
| adaptive singleton 주입 | 05-26 ServiceFactory 전달 검토 → 같은 날 app.state와 router Depends 명시 | 그 요청의 수명 관리에는 후속 주입 경로 | 특정 경로의 교정. 모든 factory 폐기 아님 |
| adaptive direct_answer | 차단 동작 교정 → 06-04 금지 백지화 → 같은 날 허용과 policy 검증 재강조 | 허용하되 근거·goal·policy 조건 검증 | 최신 결정 명확. 두 번의 허용 요청은 재확인 |
| adaptive fallback | 06-02 필수 제어만 요구 → run_failed 외 조건 해제 재확인 | 당시 root final-result 경로의 제한 | 다른 formatter의 생성 실패 fallback과 구분 |
| recipe | 06-04 step·policy 보강 → 06-10 recipe 제거 예정, 재사용 tool 이관 | 뒤의 이관·제거 방향 | 기능 폐기 전 재사용 범위 보존 |
| 업무 정의 원본 | 06월 YAML 중앙화 → 09월 Markdown 문서 중심 선택·YAML 회귀 교정 | 최신 semantic-query에서는 Markdown Skill·revision | 사용자 번복보다 agent의 과거 방식 회귀가 반복된 사례 |
| DTO | Pydantic 요청 반복, 일부 내부 dataclass·framework TypedDict 공존 | DTO·검증 경계는 Pydantic 선호. 내부 값·framework 명세는 별도 | 적용 범위 차이 |

근거: [U34 시계열](history-evidence.md#u34),
[U12 DTO](history-evidence.md#u12), [U08 원본 선택](evidence.md#u08),
[U30 최신 기준](history-evidence.md#u30).

## 반복 충돌·재결정 검토 목록

보완 검색에서 config root key의 agent→agents→agent 번복을 확인했다.
다음 표의 앞부분은 실제 되돌림·정정이며 뒤의 표는 재발한 충돌이다. 이미
최신 결정이 명확한 항목은 그 기준으로 계속 적용하고 새 승인을 요구하지
않는다. 개인 전역으로 확장할지 여부만 별도 판단 대상으로 남긴다.

| 범위 | 결정 순서·이유 | 현재 기준 | 향후 의사결정 쟁점 |
|---|---|---|---|
| adaptive config root | 05-27 adaptive→agent, 6분 뒤 agents로 통합, 12분 뒤 다른 구현체명과 통일하려 agent로 복귀 | 단수 agent가 마지막 명시 결정 | 모든 설정 root에 단수를 강제할 근거는 없음. 소유 객체 하나인지 목록인지로 새 이름을 결정할지 검토 |
| adaptive memory schema | 06-12 public 추가→제거→agent로 정정, 06-13 agentcontext로 변경하고 context 설정 위치로 이동 | 조사한 요청 중 마지막 기준은 06-13의 agentcontext | DB 이름·schema 이름·config field를 구분. 이 값을 다른 배포 환경으로 복제하지 않음 |
| tool timeout 위치 | 05-29 config 요청→06-09 14:34 UTC tool 선언에 30초→같은 날 16:05 Field 기본값 30_000으로 통합 | 마지막 요청인 ToolSpec field 기본값, 중복 호출부 값 제거 | 운영 중 조정 가능한 override와 반복 선언을 구분. 과거 선언부 지정 요청을 최신으로 되살리지 않음 |

근거: [U35 보완 시계열](history-evidence.md#u35).

아래는 사용자 번복이라고 확정하지 않은 반복 충돌이다.

| 항목 | 반복된 충돌·이유 | 현재 작업에 적용할 기준 | 다시 결정할 때의 선택지 |
|---|---|---|---|
| Markdown 업무 원본과 YAML 정의 | YAML의 편집 난이도·중복 때문에 문서 원본을 선택했으나 과거 방식 제안이 재등장 | Markdown 원본, 생성 결과는 파생물 | 운영자가 YAML을 다시 직접 관리할지. 재선택 요청 전에는 변경하지 않음 |
| prompt 제어와 코드 검증 | 업무 해석의 과한 차단·정규식은 제거 요청, 실행·권한은 서버 증거 요구 | 의미 해석과 신뢰 경계를 구분 | 새 기능의 판정이 언어 해석인지 권한·실행 검증인지 먼저 결정 |
| 평탄화와 하위 module | 지나친 분리는 추적을 어렵게 하고 구현이 많은 단일 module도 읽기 어려움 | 책임·실제 의존성에 맞춰 배치 | 새 module의 독립 책임·확장 지점·테스트 필요성을 비교 |
| Java·Kotlin의 언어별 세부 | 직접 작성 표본과 설계 예제는 있으나 brace·scope function 등의 전역 정책 근거 부족 | 확인된 관측과 공통 기준만 적용 | 특정 프로젝트에서 실제 예제로 선택한 뒤 개인 사전으로 승격 |

수치 기본값·provider·model·DB schema·UI 기본 배치 등은 해당 프로젝트의
시점별 결정이다. 최신이라는 이유만으로 다른 저장소의 기본값까지 바꾸지 않는다.

## 실제 선택 응답과 그때 제시된 이유

선택지는 assistant가 제시한 이유와 사용자가 고른 값을 구분한다. 사용자가
추천 옵션을 선택했다고 해서 그 설명의 모든 기술적 주장을 사용자가 직접
말했거나 이번 조사에서 다시 검증한 것으로 보지 않는다.

| 시점·범위 | 확인된 사용자 선택 | 선택지에 제시됐던 이유 | 개인 정책에 반영한 범위 |
|---|---|---|---|
| 2026-05-13 agent 이관 설계 | Supervisor Tool | root가 권한·goal을 소유하는 기존 구조 유지 | 상태 소유와 책임을 비교하는 사례. 모든 agent의 고정 패턴 아님 |
| 같은 설계 | SSE over POST | token·event·interrupt 전송과 HTTP streaming 요구 | 실제 인터페이스 요구에 맞춘 선택. WebSocket 금지 아님 |
| 같은 설계 | Postgres | resume·audit·다중 worker의 상태 저장 | persistence 요구에 맞춘 선택. 모든 prototype에 DB 강제 안 함 |
| 2026-09-09 리뷰 분석 | 병렬 분석 4개로 시작 | assistant 제안은 2개, 사용자 답변은 4개 | assistant 추천을 확정값으로 사용하면 안 된다는 사례 |
| 2026-09-10 모델 선택 점검 | 터미널 TUI | 질문으로 문제가 발생하는 화면을 확인 | 실제 사용한 입력 경로에서 실행 설정을 검증 |
| 2026-09-21 개인 Skill hub | 설명·예시 중심 Markdown 또는 문서 | 현재 관리 형식을 묻는 질문에 직접 답변 | 문서 중심 원본을 선택한 명시 근거 |

동기 선택 응답은 session `019e2026-7b64-7933-b31b-415d0227487a`의
JSONL line 94에서 확인했다. 비동기 응답은 사용자 메시지 안의 실제 `answer`
값을 읽었다. tool의 `accepted: true`는 질문 전달 성공이므로 사용자의 승인이나
선택으로 세지 않았다. 빈 `answers`에도 확정 선택을 부여하지 않았다.
