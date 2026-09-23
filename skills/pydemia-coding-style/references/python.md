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
