# 언어별 적용 범위

[사전 색인](dictionary.md) · [근거](evidence.md) · [충돌과 결정](decisions.md)

<a id="lang-001"></a>

## LANG-001 — TypeScript와 프런트엔드의 기존 형식

- 상태: 조건부
- 적용 범위: TS·TSX·JS
- 근거: [G05](evidence.md#g05) · [L02](evidence.md#l02)

함수·변수의 camelCase, 타입·컴포넌트의 PascalCase 등 기존 TS 규칙을 따른다. Python의 snake_case를 TS
로컬 이름에 강제하지 않는다. 서버 wire DTO는 서버의 필드명을 유지한다.

**이유:** TaskLens는 탭·작은따옴표, 최근 선택 프런트엔드는 공백 2칸·큰따옴표를 사용한다. 개인의 단일 TS format을 확정할
증거가 없다.

**예외·한계:** 새 TS 프로젝트의 세미콜론·quote·indent·formatter는 이 사전에서 미확정이다. 인접 코드와 명시적 설정을
우선하며 Pydantic을 프런트엔드에 적용하지 않는다.

<a id="lang-002"></a>

## LANG-002 — SQL 생성과 데이터 값

- 상태: 조건부
- 적용 범위: DB 조회·LLM 생성 SQL
- 근거: [U08](evidence.md#u08) · [L02](evidence.md#l02)

DB 실행 값은 typed bind parameter로 전달한다. 식별자·권한·실행 조건은 서버가 확인한다. SQL 출력의 보존과 재실행
가능성은 입력 revision·schema·데이터 변화 조건을 함께 기록한다.

**이유:** 최근 조회 라이브러리의 검증 경계와 생성 SQL 기록 요구에 근거한다.

**예외·한계:** SQL keyword 대소문자, alias, JOIN 줄바꿈은 개인 공통 규칙을 확정할 증거가 부족하다. 저장소 기준을
따른다. 조회조건 재현과 동일 데이터 결과 보장을 혼동하지 않는다.

<a id="lang-003"></a>

## LANG-003 — 형식의 문법과 개인 서식

- 상태: 조건부
- 적용 범위: Makefile·JSON·YAML·shell·문서
- 근거: [U00](evidence.md#u00) · [L01](evidence.md#l01)

파일 형식의 문법을 우선한다. Make recipe에는 탭을 유지하고 JSON에 trailing comma를 넣지 않는다. Python
예제에는 python fence를 사용한다. 새 설정 파일은 해당 parser와 도구로 검증한다.

**이유:** 현재 요청의 makefile fence 안 코드는 Python 호출·리스트 예제로 해석했다. 개인 서식을 적용하다 파일 형식을
깨뜨리지 않기 위한 보완 규칙이다.

**예외·한계:** YAML 2칸은 제공하는 설정 예시의 선택이며 사용자 개인 취향으로 확정하지 않는다. shell·Go·Rust·Java의
세부 개인 규칙도 이 조사에서 확정하지 않았다.
