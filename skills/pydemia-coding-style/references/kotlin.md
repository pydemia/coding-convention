# Kotlin

개인 Android 설계 지침과 현재 공통 지침을 함께 적용한다. 설계 문서의
Kotlin 예제는 실행된 제품 코드와 구분한다. 공식 튜토리얼을 복사한 저장소는
개인 고유 서식의 근거로 사용하지 않는다.

<a id="kt-001"></a>

## KT-001 — 명명과 서식

- 상태: 조건부
- 적용 범위: 새 Kotlin 코드와 기존 코드의 지역 수정
- 근거: [JVM 조사](language-evidence.md#jvm)

공통 기본은 79자·공백 4칸·LF·UTF-8이다. 클래스는 PascalCase, 함수와
property는 lowerCamelCase를 사용한다. Python snake_case를 옮기지
않는다. 큰따옴표 문자열과 기존 package·파일 명명 규칙을 유지한다.

**이유:** 개인 Android 설계 예제에서 이 명명과 서식이 관찰되고 공식 Kotlin 관례와
맞는다.

**예외·한계:** 실행 코드 전체에서 검증된 개인 규칙은 아니다. test·Compose 이름과
ktlint 설정은 해당 프로젝트의 규칙을 따른다.

<a id="kt-002"></a>

## KT-002 — 불변 model과 명시적인 null

- 상태: 선호
- 적용 범위: Kotlin domain model·parser 결과
- 근거: [JVM 조사](language-evidence.md#jvm)

data class와 val을 우선 검토하고 필요한 값만 nullable로 선언한다.
원본 이벤트와 정규화 결과를 분리하고 원본을 덮어쓰지 않는다. 파싱 실패와
저신뢰 결과를 빈 정상 결과로 바꾸지 않는다.

**이유:** 개인 Android 설계 지침에 immutable domain model, nullable field,
원본 보존과 parser 오류 검토를 명시했다.

**예외·한계:** val은 참조 재할당을 막을 뿐 객체 전체의 불변성을 보장하지 않는다. 모든
nullable을 제거하거나 비즈니스 실패를 !!로 바꾸지 않는다.

<a id="kt-003"></a>

## KT-003 — 여러 줄 선언과 trailing comma

- 상태: 선호
- 적용 범위: 지원 Kotlin 버전의 model·호출·chain
- 근거: [JVM 조사](language-evidence.md#jvm)

여러 줄 선언은 인자별로 줄을 나누고 닫는 괄호를 시작 들여쓰기에 맞춘다.
지원 버전과 formatter가 허용하면 마지막 comma를 유지한다. 긴 chain은
호출 단위로 나누되 의미 없는 괄호와 forwarding 함수를 추가하지 않는다.

**이유:** 개인 설계 문서의 RawEvent·Transaction 예제가 수직 인자와 trailing
comma를 사용한다.

**예외·한계:** 오래된 Kotlin 1.3 튜토리얼에 새 문법을 그대로 적용하지 않는다. 버전과
formatter를 확인한다. [Kotlin 관례][source-link-1]

<a id="kt-004"></a>

## KT-004 — Android 경계와 비동기 소유자

- 상태: 조건부
- 적용 범위: Android ingestion·parser·persistence
- 근거: [JVM 조사](language-evidence.md#jvm)

domain에 Android framework 타입이 침투하지 않게 한다. parser는 Android
없이 테스트할 수 있게 만들고 가능한 한 결정적으로 처리한다. 비동기 데이터
접근은 기존 suspend function·Flow 규칙을 일관되게 적용한다.

**이유:** 개인 Android 기획의 코드 품질·파싱·테스트 지침에 명시된 방향이다.

**예외·한계:** 가상의 iOS 지원을 위해 미리 공통 framework를 만들지 않는다. Room·Compose
등 특정 제품 선택은 그 Android 프로젝트에 한정한다.

## 적용 예

개인 Android 설계에서 관찰된 immutable model과 수직 선언을 사용한 예다.
외부 입력을 검증하는 책임은 실제 입력 경계에 둔다.

```kotlin
data class QueryOptions(
    val tableName: String,
    val limit: Int = 20,
    val category: String? = null,
)

fun selectNames(names: List<String>): List<String> =
    names
        .filter { it.isNotBlank() }
        .distinct()
        .sorted()
```

[source-link-1]: https://kotlinlang.org/docs/coding-conventions.html
