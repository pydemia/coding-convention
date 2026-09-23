# Python과 텍스트 서식

[사전 색인](dictionary.md) · [근거](evidence.md) · [충돌과 결정](decisions.md)

<a id="fmt-001"></a>

## FMT-001 — 79자 줄 길이

- 상태: 명시
- 적용 범위: 소스·주석·docstring·일반 Markdown·설정
- 근거: [U00](evidence.md#u00) · [L01](evidence.md#l01) · [L03](evidence.md#l03)
  · [G04](evidence.md#g04)

기본 최대 줄 길이는 79자다. 일반 Markdown 문장도 문단 안에서 줄을 나눈다. Python 식은 괄호 안에서 줄바꿈하고 불필요한
역슬래시 연속 행은 만들지 않는다.

**이유:** 현재 요청과 기존 개인 개발 지침이 일치한다. 특정 숫자의 효율을 측정한 결과는 아니다.

**예외·한계:** URL, hash, 분리할 수 없는 식별자·문자열, 의미가 바뀌는 명령, Markdown 표는 억지로 자르지 않는다. 기존
프로젝트의 100·120자 설정을 이 Skill만으로 일괄 변경하지 않는다.

<a id="fmt-002"></a>

## FMT-002 — 공백 4칸 들여쓰기

- 상태: 명시
- 적용 범위: Python과 별도 규칙이 없는 새 텍스트 설정
- 근거: [U00](evidence.md#u00) · [L03](evidence.md#l03) · [G05](evidence.md#g05)

Python 들여쓰기는 공백 4칸이다. 연속 행은 현재 블록보다 한 단계 들여쓴다. 탭과 공백을 혼용하지 않는다.

**이유:** 현재 요청이며, 과거 직접 추가한 Ruff 설정에도 indent-width = 4와 space가 있다.

**예외·한계:** Make recipe의 탭, YAML 등 형식 규칙과 기존 TS 저장소의 들여쓰기는 보존한다. 모든 언어의 기존 파일을
4칸으로 바꾸지 않는다.

<a id="fmt-003"></a>

## FMT-003 — LF와 UTF-8

- 상태: 명시
- 적용 범위: 직접 관리하는 텍스트 파일
- 근거: [U00](evidence.md#u00) · [L02](evidence.md#l02)

줄바꿈은 LF, 인코딩은 UTF-8을 사용한다. 요청의 /LF는 LF를 뜻하는 것으로 정리한다. 이 저장소의 새 파일에는 마지막 개행을 둔다.

**이유:** 운영체제에 따라 동일 파일이 다른 바이트로 저장되는 일을 줄이는 적용 기준이다. 마지막 개행은 이 사전을 위한 보완 선택이다.

**예외·한계:** 바이너리·외부 원본·생성물은 변환하지 않는다. UTF-8을 사용한다는 이유만으로 모든 Python 파일에 encoding
cookie를 추가하지 않는다.

<a id="fmt-004"></a>

## FMT-004 — 수직 인자와 닫는 괄호

- 상태: 명시
- 적용 범위: 여러 줄 Python 선언·호출·컨테이너
- 근거: [U00](evidence.md#u00) · [G01](evidence.md#g01) · [G02](evidence.md#g02)

여러 줄로 나누면 항목을 한 줄에 하나씩 배치한다. 마지막 항목 뒤에 comma를 두고 닫는 괄호는 시작 구문의 들여쓰기 위치에 맞춘다.

```python
def build_report(
    records,
    options,
):
    return render_report(
        records,
        options,
    )

columns = [
    "name",
    "status",
]
```

**이유:** 사용자가 직접 제시한 형태다. 항목 추가 시 인접 항목을 다시 편집할 필요가 적다.

**예외·한계:** 짧은 단일 행까지 모두 펼칠 필요는 없다. tuple의 원소 수와 쉼표 의미, generator expression 문법을
보존한다. JSON에는 trailing comma를 넣지 않는다.

<a id="fmt-005"></a>

## FMT-005 — 수직 method chain

- 상태: 명시
- 적용 범위: 줄을 나누어 작성하는 Python chain
- 근거: [U00](evidence.md#u00) · [T01](evidence.md#t01)

chain 전체를 괄호로 감싸고 수신 객체를 별도 줄에 둔다. 각 method 호출은 점으로 시작하며 같은 들여쓰기에 둔다.

```python
result = (
    instance
    .method1()
    .method2()
)
```

**이유:** 현재 요청의 표기를 그대로 채택한다. formatter의 기본 출력에서 추론한 취향이 아니다.

**예외·한계:** Ruff 0.16.8 기본 formatter는 위 예제를 한 줄로 합친다. 개인 형식을 유지하는 프로젝트는 lint만
적용하거나 해당 문장을 최소 범위의 fmt off/on으로 보호한다. 기존 formatter가 기준인 프로젝트에서는 충돌을 알리고 그 기준을
따른다. 전체 파일의 formatter를 끄지 않는다.

<a id="fmt-006"></a>

## FMT-006 — 큰따옴표 기본값

- 상태: 명시
- 적용 범위: Python 문자열과 docstring
- 근거: [U00](evidence.md#u00) · [L03](evidence.md#l03) · [G03](evidence.md#g03)

일반 문자열은 큰따옴표를 기본으로 한다. docstring은 큰따옴표 세 개를 사용한다. 같은 파일에서 특별한 이유 없이 quote를 바꾸지
않는다.

**이유:** 현재 요청과 직접 작성한 과거 Ruff 설정에서 확인했다.

**예외·한계:** escape가 늘거나 원문·외부 문법이 손상되는 경우 작은따옴표를 쓸 수 있다. 과거 unipy의 작은따옴표를 현재
기본으로 재채택하지 않는다.

<a id="py-001"></a>

## PY-001 — 이름의 형태와 의미

- 상태: 명시
- 적용 범위: Python 클래스·함수·변수·모듈
- 근거: [U00](evidence.md#u00) · [U01](evidence.md#u01) · [L01](evidence.md#l01)

클래스는 PascalCase, 함수는 snake_case다. 변수와 모듈도 snake_case를 기본으로 한다. data1, helper처럼
범위가 불분명한 이름보다 실제 대상과 동작이 드러나는 이름을 쓴다. 동일 개념은 코드·테스트·문서에서 같은 용어를 사용한다.

**이유:** 형태는 현재 요청, 의미가 드러나는 이름은 반복된 설계 요청과 개인 개발 지침에 근거한다.

**예외·한계:** 프레임워크 hook, wire field, 외부 API, 공개 이름은 호환성 검토 없이 개명하지 않는다.
manager·service 같은 단어 자체를 금지하지 않는다.

bool 판정 함수는 실제로 bool을 반환하며 `is_...`처럼 판정임이 드러나는
이름을 사용한다. `validate_...`가 값·예외·bool 중 무엇을 제공하는지
호출자와 일치시킨다. [U35](history-evidence.md#u35)

<a id="py-002"></a>

## PY-002 — 배포 패키지의 절대 import

- 상태: 명시
- 적용 범위: 배포 패키지의 공개 사용 경로와 패키지 수준 참조
- 근거: [U00](evidence.md#u00) · [G03](evidence.md#g03) · [G04](evidence.md#g04)

설치된 패키지 이름을 기준으로 절대 import를 우선한다. 실행 cwd나 sys.path 수정에 의존하는 사용법을 기본으로 만들지 않는다.

```python
from mypackage import build_report
from mypackage.models import ReportRequest
```

**이유:** 공개 사용 경로를 식별하기 쉽다. unipy와 최근 IAM 패키지에서 실제 절대 import를 확인했다.

**예외·한계:** 패키징 여부만으로 내부 상대 import까지 금지하지 않는다. 패키지 안의 캡슐화 경계는 PY-003을 적용한다.

<a id="py-003"></a>

## PY-003 — 내부 상대 import와 공개 API

- 상태: 명시
- 적용 범위: 외부 공개를 제한하는 subpackage 내부
- 근거: [U00](evidence.md#u00) · [U03](evidence.md#u03) · [G01](evidence.md#g01)
  · [G02](evidence.md#g02) · [G03](evidence.md#g03)

내부 구현을 묶는 subpackage에서는 상대 import를 사용하고 외부가 사용할 이름만 __init__.py 등에서 노출한다.
__all__을 쓰면 실제 공개 심볼과 일치시킨다.

```python
# mypackage/reports/__init__.py
from .builder import build_report

__all__ = [
    "build_report",
]
```

**이유:** 현재 요청과 dynamic-batcher·unipy_dto의 패키지 구성에 근거한다. 내부 변경과 사용자 import 경로의
관계를 명시할 수 있다.

**예외·한계:** 상대 import가 의존성 접근을 기술적으로 차단하지는 않는다. 외부 사용자가 내부 경로에 결합하지 않게
API·문서·검사를 함께 관리한다. wildcard export와 순환 import는 과거 코드에서 보였어도 기본으로 채택하지 않는다.

<a id="py-004"></a>

## PY-004 — 상수와 실행 설정의 구분

- 상태: 명시
- 적용 범위: 모듈 수준 이름·런타임 설정
- 근거: [U00](evidence.md#u00) · [L01](evidence.md#l01) · [G01](evidence.md#g01)

필요한 모듈 상수는 UPPER_SNAKE_CASE로 작성한다. 모듈 고정값은 주로 시스템 기본 설정처럼 제한된 경우에만 둔다. 요청별 값,
사용자 선택, client·connection·cache 상태를 전역 상수처럼 보관하지 않는다.

```python
DEFAULT_TIMEOUT_SECONDS = 30
```

**이유:** 현재 요청은 대문자 표기와 사용 범위의 제한을 함께 요구한다. 값이 고정이라는 이유만으로 모든 literal을 전역으로
끌어올리지 않는다.

**예외·한계:** 기존 프로토콜 enum·공개 오류 코드 등은 그 의미를 유지한다. module global로 환경변수를 읽던 과거 구현은
관측 사례이며 신규 설정 설계의 의무가 아니다.

<a id="py-005"></a>

## PY-005 — 타입이 있는 데이터 구조

- 상태: 선호
- 적용 범위: Python 입력·출력 DTO와 검증 경계
- 근거: [U05](evidence.md#u05) · [G02](evidence.md#g02) · [G04](evidence.md#g04)
  · [L01](evidence.md#l01) · [L02](evidence.md#l02)

구조가 안정적이고 검증이 필요한 데이터는 Pydantic model을 우선 검토한다. 공개 함수의 인자·반환 타입을 드러낸다. 이미
Pydantic을 쓰는 프로젝트에서 같은 DTO만 무타입 dict로 우회하지 않는다.

**이유:** 사용자가 Pydantic model을 convention이라고 직접 교정했고 DTO 패키지와 최근 라이브러리에서도 구조화된
타입을 사용했다.

**예외·한계:** 모든 값에 Pydantic 의존성을 추가하지 않는다. 단순 내부 값은
dataclass·NamedTuple·TypedDict도 가능하다. IAM의 dataclass 사례처럼 프로젝트 요구를 따른다. Python
버전에 맞는 typing 문법을 사용한다.

<a id="py-006"></a>

## PY-006 — 호출 인자의 의미

- 상태: 관측
- 적용 범위: 옵션이 여러 개인 새 Python API
- 근거: [G04](evidence.md#g04) · [L01](evidence.md#l01) · [L02](evidence.md#l02)

서로 혼동하기 쉬운 옵션은 이름을 명시해 전달한다. keyword-only는 호출 의미와 호환성에 도움이 되는 API에서 사용한다. None,
생략, 빈 목록, False의 의미가 다르면 타입과 분기로 구분한다.

**이유:** 최근 라이브러리의 공개 메서드와 개발 가이드에서 확인한 방식이다. positional boolean의 의미를 추측할 필요를
줄인다.

**예외·한계:** 기존 positional API를 일괄 keyword-only로 바꾸지 않는다. 모든 함수에 별표 인자를 강제하지 않는다.

<a id="py-007"></a>

## PY-007 — import 부작용과 선택 의존성

- 상태: 조건부
- 적용 범위: 재사용 라이브러리와 선택 adapter
- 근거: [U06](evidence.md#u06) · [G04](evidence.md#g04) · [L02](evidence.md#l02)

core는 선택 웹·DB adapter를 import해야만 동작하는 구조를 피한다. 외부 자원은 인자로 전달받고 생성·연결·종료의 소유자를
명시한다. import 시 연결·DDL·실행을 시작하지 않는다.

**이유:** 호스트에 붙는 라이브러리에서 기존 자원과 수명 관리를 중복 소유하지 않게 한다. 선택 extra와 core의 경계가 최근
패키지에 존재한다.

**예외·한계:** 모든 애플리케이션에 동일한 host 구조나 Protocol을 강제하지 않는다. CLI 진입점이 자원을 생성하는 경우에도 그
책임이 진입점에 드러나면 된다.

<a id="py-008"></a>

## PY-008 — import 정리의 범위

- 상태: 관측
- 적용 범위: Python import 목록
- 근거: [G03](evidence.md#g03) · [G04](evidence.md#g04) · [L01](evidence.md#l01)
  · [L02](evidence.md#l02)

새 파일의 import는 저장소 linter가 정한 표준 라이브러리·외부 패키지·프로젝트 순서를 따른다. 사용하지 않는 import와 추적을
어렵게 하는 wildcard import를 추가하지 않는다.

**이유:** 최근 Ruff I 설정과 명시적 의존성 지침에 부합한다. 오래된 파일의 import 순서를 개인 표준으로 고정하지 않는다.

**예외·한계:** 순환 참조 회피나 선택 의존성 때문에 함수 안에서 import할 때는 그 이유와 동작을 확인한다. unrelated 파일
전체를 import 정리 대상으로 넓히지 않는다.

<a id="py-009"></a>

## PY-009 — Any 대신 호출 가능한 범위를 표현

- 상태: 선호
- 적용 범위: 안정적인 함수·factory·service 입출력
- 근거: [추가 대화 U11](history-evidence.md#u11)

호출자가 사용하는 속성과 메서드를 타입으로 드러낸다. 반환값의 실제 범위가
알려져 있으면 구체 타입이나 기존 base type을 쓰고, 여러 구현의 공통 동작만
필요하면 작은 Protocol을 검토한다. 무타입 dict나 Any로 API 설명을 대신하지
않는다. type ignore를 추가하기 전에 실제 불일치를 확인한다.

**이유:** 사용자가 factory의 Any 때문에 안전한 호출과 코드 탐색이 어렵다고 교정했다.

**예외·한계:** 동적 외부 입력은 검증 전까지 넓은 타입일 수 있다. 타입 표기를 위해 의미 없는
새 interface를 만들지는 않는다.

<a id="py-010"></a>

## PY-010 — 구조화된 값과 직렬화 경계

- 상태: 선호
- 적용 범위: DTO·context·설정·공개 응답
- 근거: [추가 대화 U12](history-evidence.md#u12)

검증이 필요한 DTO에는 Pydantic을 우선한다. 구조화된 배열·객체를 내부에서
JSON 문자열로 바꾸어 반복 파싱하지 않는다. 전송·저장 경계에서 직렬화하고
내부에서는 타입이 있는 값으로 다룬다. 한정된 분기 값은 enum 또는 Literal로
의미와 허용 범위를 드러낸다.

**이유:** Pydantic convention 누락과 context의 이중 파싱을 사용자가 지적했다.

**예외·한계:** LangGraph의 상태 규약, 기존 TypedDict·dataclass 사용처와 wire format은
확인 후 변경한다. Python의 DTO 선택을 Kotlin data class 금지로 확장하지
않는다.

<a id="py-011"></a>

## PY-011 — 환경 설정을 실행 시점에 읽기

- 상태: 선호
- 적용 범위: 환경변수를 지원하는 Python package·application
- 근거: [추가 대화 U13](history-evidence.md#u13)

설치나 빌드 중 읽은 환경값을 배포 코드에 박아 넣지 않는다. 실행 시점에
설정 객체를 구성하고 Python에서는 기존 Pydantic Settings 사용을 우선
검토한다. 설정 생성 시점과 재로딩 여부를 명확히 한다. import 시 읽은 값이
영구히 고정되는 구조가 의도한 수명인지 확인한다.

**이유:** 설치 시 .env 값이 고정되는 문제를 직접 교정하며 runtime 로딩을 요청했다.

**예외·한계:** 모든 라이브러리에 설정 패키지를 추가하는 규칙은 아니다. 호스트가 전달하는
설정은 호스트의 수명과 책임을 따른다.

<a id="py-012"></a>

## PY-012 — 필수 설정과 import 오류의 조기 검증

- 상태: 선호
- 적용 범위: 애플리케이션 시작·선택 adapter 활성화
- 근거: [추가 대화 U14](history-evidence.md#u14)

필수 설정과 의존성 오류는 개발 검사와 애플리케이션 초기화 단계에서 드러낸다.
순환 import를 감추기 위해 함수 안으로 import만 옮기고 실행 시 실패하도록
남겨 두지 않는다. 선택 기능은 해당 기능을 활성화할 때 의존성을 검증한다.

**이유:** 사용자가 lazy import로 오류를 실행 시점까지 미룬 것을 문제로 지적했다.

**예외·한계:** 조기 검증이 reusable library의 import에서 DB 연결이나 DDL을 실행하라는
뜻은 아니다. 선택 의존성 누락으로 무관한 core 기능을 막지 않는다.

<a id="py-013"></a>

## PY-013 — 기본값의 선언 위치를 하나로

- 상태: 선호
- 적용 범위: Pydantic model·tool spec·설정 호출부
- 근거: [추가 대화 U15](history-evidence.md#u15)

의미가 같은 기본값은 model field 또는 해당 설정의 소유자에 선언한다.
호출마다 같은 timeout·기본 옵션을 전달하지 않는다. 호출부에는 기본값과
다른 선택을 적는다. 생략·None·빈 값·False의 의미는 기존 API대로 유지한다.

**이유:** 반복된 tool timeout을 Field 기본값으로 옮기고 설정의 중복을 줄이도록
요청했다.

**예외·한계:** None이 별도의 의미를 갖는 API를 단순 bool 기본값으로 합치지 않는다.
재현을 위해 값 전체를 고정하는 실행 snapshot은 별도 목적이다. 같은 날 먼저 요청한 선언부
timeout 지정은 후속 Field 기본값 통합 요청으로 대체됐다. 과거 요청만 읽고
다시 호출부에 값을 복제하지 않는다. [U35](history-evidence.md#u35)
