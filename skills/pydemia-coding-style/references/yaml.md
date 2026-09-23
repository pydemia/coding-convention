# YAML

Python의 문법을 YAML에 옮기지 않는다. 편집하는 YAML과 렌더링된 설정값을
함께 확인한다. 현재 프로젝트의 schema와 loader가 적용 기준이다.

<a id="yaml-001"></a>

## YAML-001 — 들여쓰기와 block 구조

- 상태: 조건부
- 적용 범위: 직접 관리하는 YAML
- 근거: [U00](evidence.md#u00), [추가 대화 U20](history-evidence.md#u20)

탭 대신 공백을 쓰고 같은 mapping·sequence 깊이는 동일하게 맞춘다. 기존
저장소의 2칸 또는 4칸 규칙을 보존한다. 별도 규칙이 없는 새 개인 파일은
공통 기본인 4칸을 사용한다. Python trailing comma를 block list에 넣지
않는다.

**이유:** 현재 요청의 공백 기준을 YAML 문법에 맞춰 적용한다. 기존 Helm 파일에서는
별도의 들여쓰기와 template 구조가 관찰된다.

**예외·한계:** YAML 전체를 4칸으로 바꾸는 일괄 재서식 지시는 아니다. 렌더링 결과도
파싱해서 구조가 유지되는지 확인한다. [YAML 명세](https://yaml.org/spec/1.2.2/)

<a id="yaml-002"></a>

## YAML-002 — 문자열의 실제 값 보존

- 상태: 조건부
- 적용 범위: scalar·prompt·환경변수 placeholder
- 근거: [추가 대화 U21](history-evidence.md#u21)

문자열을 인용할 때 큰따옴표를 기본으로 하되 escape가 값에 미치는 영향을
확인한다. 숫자처럼 보이는 ID·버전·코드는 schema가 문자열이면 문자열로
유지한다. 여러 줄은 줄바꿈을 보존할지 공백으로 접을지에 따라 `|`와 `>`를
선택하고 끝 개행도 확인한다.

**이유:** 설정의 모양보다 loader가 읽는 값이 실제 동작을 결정한다. prompt의 불필요한
줄바꿈을 줄여 달라는 요청이 있었다.

**예외·한계:** `${NAME}`은 이 프로젝트 loader가 지원할 때만 환경변수 참조다. YAML
자체의 치환 기능으로 설명하지 않는다. 줄 수 감소를 측정된 token 절감으로
표현하지 않는다.

<a id="yaml-003"></a>

## YAML-003 — 환경별 값과 credential 분리

- 상태: 선호
- 적용 범위: 애플리케이션 config·Kubernetes 설정
- 근거: [추가 대화 U22](history-evidence.md#u22)

환경에 따라 달라지는 값은 설정으로 분리하고 credential은 배포 환경의
secret 주입 경로를 사용한다. ConfigMap에 secret 원문을 복사하지 않는다.
예제에는 실제 계정·주소 대신 용도가 드러나는 placeholder를 사용한다.

**이유:** 일반 DB 접속 설정과 사용자명·비밀번호의 주입 경로를 구분하도록 요청했다.

**예외·한계:** 설정 형식·prefix는 해당 loader를 따른다. 기존 시스템의 보안·로깅 요구를
확인하며 모든 로그를 무조건 숨기거나 원문으로 남기는 규칙으로 확대하지
않는다.

<a id="yaml-004"></a>

## YAML-004 — schema와 업무 정의의 책임 분리

- 상태: 선호
- 적용 범위: 설정 model·validator·업무 정의·테스트
- 근거: [추가 대화 U23](history-evidence.md#u23)

schema와 validator는 구조·타입·허용 조합을 검사한다. 운영자가 관리하는
업무 의미를 validator 상수와 YAML 양쪽에 복제하지 않는다. 실행 코드와
테스트는 같은 업무 정의 원본을 참조한다. 테스트 전용 복사본이 운영 규칙의
실질 원본이 되지 않게 한다.

**이유:** validator의 업무 상수를 정의 파일로 옮기고 테스트도 같은 원본을 보도록
여러 차례 교정했다.

**예외·한계:** 업무 정의 원본이 Markdown으로 바뀐 프로젝트는 최신 결정을 따른다. 이
항목은 YAML을 영구적인 업무 원본으로 지정하지 않는다.

<a id="yaml-005"></a>

## YAML-005 — override 우선순위와 최소 설정

- 상태: 선호
- 적용 범위: 기본값·환경변수·config 파일·사용자 override
- 근거: [추가 대화 U24](history-evidence.md#u24)

설정 소스의 우선순위를 문서화하고 충돌 사례로 검증한다. 기본값과 다른
항목만 적는 설정과 실행 전체를 고정한 snapshot을 구분한다. 이름이 같은
환경변수가 암묵적으로 모든 설정을 덮게 하지 않고 지원 prefix를 명확히 한다.

**이유:** home 설정 이후 cwd override, .env.local override, 지정 prefix 환경변수
참조 등 여러 요청에서 명시적인 우선순위가 필요했다.

**예외·한계:** 어느 소스가 항상 최상위인지는 개인 전역으로 확정하지 않는다. 각 프로젝트의
최신 결정과 실제 loader가 기준이다. demian에서 확인한 한 사례는
`.env` → `.env.local` → `process.env` 순서로 뒤의 값이 덮어쓰는 방식이다.
[U35](history-evidence.md#u35)

<a id="yaml-006"></a>

## YAML-006 — prompt와 코드의 판정 책임

- 상태: 조건부
- 적용 범위: LLM prompt·업무 의미 해석·서버 검증
- 근거: [추가 대화 U25](history-evidence.md#u25)

prompt는 기대하는 행동과 선택 조건을 구체적으로 설명한다. 같은 지시의
반복과 과도한 부정문을 줄인다. 서버의 권한·게시·실행 완료 검증은 prompt의
자기 보고로 대신하지 않는다. 정해진 상태·오류 코드는 prose와 구분한다.

**이유:** prompt 제어를 선호한 요청과 서버의 검증된 증거를 요구한 후속 설계는
서로 다른 판정 경계를 다룬다.

**예외·한계:** 모든 if/else를 LLM에 맡기거나 모든 언어 해석을 정규식으로 바꾸는 전역
규칙은 없다. 번복 이력은 [결정 기록](decisions.md)에 둔다.

<a id="yaml-007"></a>

## YAML-007 — upstream 기본값과 배포 override

- 상태: 조건부
- 적용 범위: Helm chart·환경별 values·렌더링 manifest
- 근거: [추가 대화 U26](history-evidence.md#u26)

환경별 변경은 해당 환경의 values·override에 둔다. 가져온 chart의 기본
values와 template를 수정하기 전에 실제 변경 소유자를 확인한다. YAML
파싱뿐 아니라 template 렌더링 후의 값·타입·들여쓰기를 검증한다.

**이유:** 외부 chart의 기본 파일을 수정한 작업을 되돌리고 환경 전용 extraEnv로
설정하도록 반복 교정했다.

**예외·한계:** chart 자체의 기능 수정이 요청된 경우 template 변경을 막지 않는다. 환경별
설정과 upstream 코드 변경을 구분하는 규칙이다.

## 적용 예

아래는 schema가 `endpoint`를 문자열, `timeout_ms`를 정수로 받는 예다.
이 프로젝트의 기존 YAML 설정은 2칸이므로 그 간격을 유지했다.
`${QUERY_ENDPOINT}`의 치환은 별도 loader가 지원해야 한다.

```yaml
query:
  endpoint: "${QUERY_ENDPOINT}"
  timeout_ms: 30000
  allowed_formats:
    - "table"
    - "text"
  prompt: |-
    요청한 조건과 데이터의 의미를 확인한다.
    확인되지 않은 내용은 미확인으로 구분한다.
```

`prompt`의 두 문장 사이에는 실제 개행이 있고 마지막 개행은 제거된다.
`timeout_ms`가 model 기본값과 같다면 일반 운영 설정에서 생략할 수 있다.
재현용 설정 snapshot에서는 명시적으로 남길 수 있다.
