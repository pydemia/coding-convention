# 언어별 추가 근거

<a id="jvm"></a>

## JVM — 직접 작성·설계와 가져온 예제의 구분

Java·Kotlin 파일과 Markdown의 코드 fence를 함께 검색했다. Git author가
본인이어도 외부 예제를 처음 추가한 commit이면 개인 서식으로 집계하지 않았다.

| 자료 | 확인한 내용 | 사전에서의 취급 |
|---|---|---|
| cobalt9-jetbrains의 JParserTest | 작성자 header가 pydemia이고 기능별 read·flatten·dump 메서드, PascalCase·lowerCamelCase·공백 4칸·큰따옴표 사용 | 직접 작성 표기의 보조 관측. 현재 권장 테스트 구현으로 복제하지 않음 |
| cobalt9의 GreetingController | Spring 예제 package와 기본 greeting 동작 | 외부 예제 가능성이 높아 개인 근거에서 제외 |
| cobalt9의 sample.kt | 색상 확인용 문법 모음, wildcard·dynamic·강제 null 해제 등 혼재 | 제품 코드의 설계 선호로 해석하지 않음 |
| kotlin-spring-boot-restful | README에 공식 Kotlin Spring 튜토리얼 명시, 기본 Greeting 예제 | 튜토리얼 이관 자료로 분류 |
| aftersum AGENTS.md | 불변 domain model, 명시적 nullable, 원본·정규화 분리, Android 없는 parser test, suspend·Flow | 개인 Android 설계의 조건부 근거. 실제 구현 완료 근거는 아님 |
| Hadoop·Spark·Scala의 books | 책 코드·기존 저자 정보·책 예제 package | Java 개인 규칙에서 제외 |
| datarobot-test의 Java | DataRobot 배포 SDK 예제와 생성 모델 연동 sample | SDK의 서식과 API를 개인 정책으로 채택하지 않음 |
| 큰 NLP 저장소의 MALLET | 배포된 MALLET 소스와 대학 저작권·원저자 표기 | 개인 Java 코드로 집계하지 않음 |
| Python3의 Java | Python 교재의 언어 비교·연동 예제 | 개인 규칙에서 제외 |
| 로컬 ai-coding-plugin·openclaw | 다른 저자 또는 외부 수집 코드 | 개인 규칙에서 제외 |

공개 revision 고정 근거:

- [JParserTest 작성 표기와 코드](https://github.com/pydemia/cobalt9-jetbrains/blob/d1adfa131a21873f5e6477f45f48e3e908c7162c/samples/sample-1.java)
- [Kotlin 튜토리얼 README](https://github.com/pydemia/kotlin-spring-boot-restful/blob/8002ea5dbe7ddeb5c093c481458370d6185254f4/README.md)

Android 설계 지침은 비공개 저장소의 로컬 수집본 `AGENTS.md` line
150–285에서 확인했다. revision은
`7dd1f8d327b225726aad783fb0adcaa16ef38891`이다. 공개 독자가 원문을
독립적으로 열 수 없으므로 공개 검증 링크로 표시하지 않는다.

JParserTest의 오래된 raw type·unchecked cast·print 위주 검증·주석 처리된
구현·긴 줄은 현재 정책보다 우선하지 않는다. 작성자 header 하나만으로 모든
행의 독창성을 입증하지도 않는다. Java brace 위치·Lombok·Optional 정책,
Kotlin scope function·coroutine dispatcher 정책은 확정할 근거가 부족하다.

## Python·YAML·Markdown

로컬 전체 후보 파일과 수집한 저장소의 내용을 읽어 서식·설정·타입·import
패턴을 검색하고 동일 내용은 SHA-256으로 중복 집계에서 제외했다. 전체
검색의 숫자는 개인 규칙의 투표 수가 아니다. vendor·tutorial·worktree와
생성물의 비중이 커 직접 요청과 소유 경계를 함께 판단했다.

- 최근 Python 설정에는 79·88·100·120자와 Black·Ruff가 공존한다.
- Pydantic model·Settings, NumPy·Google docstring, 절대·상대 import가
  함께 존재한다. 기존 지역 관례를 단일 도구로 정규화하지 않는다.
- Markdown에는 설계 원본·생성 Skill·책 문서·이관 자료가 섞여 있다.
  복사본 여러 개를 독립적인 개인 결정으로 세지 않는다.
- Kubernetes YAML에는 외부 chart·CRD가 많다. 전체 YAML 줄 수로 개인의
  들여쓰기 선호나 업무 정의 방식을 추정하지 않는다.

## 문법 확인에 사용한 공식 자료

개인 취향의 근거와 언어 문법의 근거는 다르다. 공식 문서는 개인이 선택했다고
주장하는 근거로 사용하지 않았다.

- [Kotlin coding conventions][source-link-1]
- [Java method invocation 문법][jls]
- [YAML 1.2.2](https://yaml.org/spec/1.2.2/)
- [CommonMark 0.31.2](https://spec.commonmark.org/0.31.2/)

[source-link-1]: https://kotlinlang.org/docs/coding-conventions.html
[jls]: https://docs.oracle.com/javase/specs/jls/se21/html/jls-15.html#jls-15.12
