# Java

Java에 대한 개인 명명·괄호 규칙은 직접 작성 표본이 제한적이다.
아래 조건부 규칙은 현재 공통 지침을 Java 문법에 맞춘 적용안이다. 책 예제나
색상 테스트용 코드의 형식을 개인 취향으로 확정하지 않는다.

<a id="java-001"></a>

## JAVA-001 — 명명과 공통 서식의 적용 범위

- 상태: 조건부
- 적용 범위: 기존 지침이 없는 새 Java 코드
- 근거: [JVM 조사](language-evidence.md#jvm), [U00](evidence.md#u00)

79자·공백 4칸·LF·UTF-8을 공통 기본으로 적용한다. 클래스는 PascalCase,
메서드·변수는 기존 Java API와 맞는 lowerCamelCase를 유지한다. Python의
snake_case를 기존 Java 공개 API에 강제하지 않는다. 문자열은 큰따옴표,
문자는 작은따옴표라는 문법을 지킨다.

**이유:** 공통 서식은 명시됐지만 JParserTest에서 lowerCamelCase가 관찰되지만 전역 선호를
확정하기에는 표본이 작다. API 일관성을 보존하는 조건부 적용안이다.

**예외·한계:** Java 고유의 개인 명명 정책은 미확정이다. 프로젝트 formatter와 기존
공개 메서드 이름이 우선한다.

<a id="java-002"></a>

## JAVA-002 — 여러 줄 인자와 chain

- 상태: 조건부
- 적용 범위: Java 호출·선언·fluent API
- 근거: [JVM 조사](language-evidence.md#jvm)

긴 인자는 한 줄에 하나씩 놓고 닫는 괄호를 시작 구문의 들여쓰기에 맞춘다.
여러 줄 chain은 각 호출을 별도 줄에 두되 Python의 바깥 괄호를 문법 확인
없이 복사하지 않는다. 메서드 인자 마지막에 trailing comma를 넣지 않는다.

**이유:** 현재 수직 배치 선호를 Java 문법에 맞춰 적용한다. Java 인자 목록은 끝의
comma를 허용하지 않는다.

**예외·한계:** 배열 초기화의 trailing comma와 호출 인자 문법은 다르다. brace 위치는
개인 고유 근거가 부족하므로 기존 formatter를 따른다.
[Java 인자 문법][jls]

<a id="java-003"></a>

## JAVA-003 — 타입·상태·설정의 공통 설계 기준

- 상태: 조건부
- 적용 범위: Java model·service·설정
- 근거: [L01](evidence.md#l01), [JVM 조사](language-evidence.md#jvm)

구체적인 입출력 타입, 의미 있는 오류·상태, 추적 가능한 composition을
사용한다. 기본 설정과 실행 중 바뀌는 상태를 구분하고 공유 mutable state를
무분별하게 두지 않는다. 설정 때문에 불필요한 상속 계층을 만들지 않는다.

**이유:** 언어와 무관한 개인 개발 지침을 Java에 적용한 것이다.

**예외·한계:** Lombok, record, Optional, DI framework, checked exception 정책은
이번 자료로 개인 기본을 확정하지 않는다. 지원 Java 버전과 현재 API를
따른다.

## 적용 예

서식과 타입 예제다. 특정 DI framework나 Java 버전을 개인 정책으로 정한
예제가 아니다. 입력 검증·예외 타입은 실제 API 규칙에 맞춘다.

```java
public final class QueryOptions {
    private final String tableName;
    private final int limit;

    public QueryOptions(
        String tableName,
        int limit
    ) {
        this.tableName = tableName;
        this.limit = limit;
    }

    public String getTableName() {
        return tableName;
    }

    public int getLimit() {
        return limit;
    }
}
```

[jls]: https://docs.oracle.com/javase/specs/jls/se21/html/jls-15.html#jls-15.12
