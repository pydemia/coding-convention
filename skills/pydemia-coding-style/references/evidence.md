# 근거와 조사 범위

조사 기준일: 2026-09-23 (Asia/Seoul). 공개 원문 링크는 commit을 고정했다.
로컬 자료와 대화는 위치·revision·선택에 필요한 요약만 기록했다. 아래의
비공개 자료는 공개 독자가 독립적으로 열 수 없다는 한계가 있다.

## 방법과 한계

최초 표본 조사를 확대했다. 인증된 pydemia 소유 저장소 410개 중 non-fork
239개를 수집했고 로컬 Git root 154개와 Codex 기록 268개, 관련 memory를
조사했다. 자세한 기준·제외·파일별 내용 검사와 수동 검토 범위는 저장소의
`docs/research-coverage.md`에 기록했다. 독립 Skill에는 이 안내와 아래
근거 문서가 포함된다.

[추가 사용자 결정](history-evidence.md)과 [언어별 근거](language-evidence.md)를
함께 읽는다. 전체 목록·내용 검색은 전수 범위를 명시하지만 모든 행의 수동
정독·모든 과거 revision 분석을 뜻하지 않는다. Git author·소유·non-fork만으로
직접 작성이나 개인 선호를 확정하지 않는다. 외부 예제·agent 생성·공동 작업·
이관 자료를 구분했다. 71개 규칙은 현재 요청과 같은 범위의 최신 명시 결정을
우선한 편집 결과다. 미확정·반복 번복은 [결정 기록](decisions.md)에 남겼다.

## 현재 요청과 실제 대화

대화 위치의 line은 JSONL 레코드 번호다. timestamp는 원본 UTC 기준이다.
원문 전체와 인증값·업무 데이터는 배포 bundle에 넣지 않았다.

<a id="u00"></a>

### U00 — 현재 요청

2026-09-23 사용자 요청: 79자, 공백 4칸, LF, UTF-8, 수직 괄호·chain,
trailing comma, 큰따옴표, PascalCase·snake_case, 공개 절대 import·내부
상대 import, mixin 회피, 제한된 모듈 상수 사용. 함께 제공한 작성 지침도
문서 표현의 근거로 사용했다. 이번 사전의 가장 우선하는 자료다.

<a id="u01"></a>

### U01 — 간결한 interface와 추적 가능한 확장

공통 template·interface·필요한 factory를 요청한 뒤 간결한 구조와 추적 가능한 동작을 재강조했다. 과거 함수 20줄
제안은 이후 지침과 대조해 강제하지 않았다.

- UTC: `2026-05-13T12:43:22.074Z`
- Session: `019e20e2-c1cd-7910-b493-45a11f7bc07b`
- Record:
  `rollout-2026-05-13T19-29-52-019e20e2-c1cd-7910-b493-45a11f7bc07b.jsonl` /
  line 746
- UTC: `2026-05-13T14:49:41.202Z`
- Session: `019e20e2-c1cd-7910-b493-45a11f7bc07b`
- Record:
  `rollout-2026-05-13T19-29-52-019e20e2-c1cd-7910-b493-45a11f7bc07b.jsonl` /
  line 972

<a id="u02"></a>

### U02 — 줄별 주석 대신 함수 docstring

함수 docstring을 사용하라는 직접 교정. 특정 NumPy·Google 형식을 선택한 요청은 아니다.

- UTC: `2026-05-31T14:37:39.951Z`
- Session: `019e7e64-ab35-7153-a23d-a70eadaae672`
- Record:
  `rollout-2026-05-31T23-16-27-019e7e64-ab35-7153-a23d-a70eadaae672.jsonl` /
  line 369

<a id="u03"></a>

### U03 — 내부 구현과 사용자 catalog의 경계

내장 기능은 framework 안에서 합성하고 예약된 이름을 docstring으로 알리도록 요청했다. 순환 참조 회피가 명시적 이유다. 이름
충돌 시 framework 우선은 해당 catalog의 결정이다.

- UTC: `2026-06-02T05:55:33.070Z`
- Session: `019e4d23-7969-7242-8065-e7145752c51e`
- Record:
  `rollout-2026-05-22T09-43-51-019e4d23-7969-7242-8065-e7145752c51e.jsonl` /
  line 9914

<a id="u04"></a>

### U04 — tracing 문자열의 수동 동기화 문제

함수명을 바꿀 때 tracing 문자열까지 바꿔야 하는 구조를 유지보수 문제로 지적했다. 구현 참조 사용을 검토하라는 선호로 반영했다.

- UTC: `2026-06-01T17:03:40.502Z`
- Session: `019e646c-f362-7d82-a331-b228e6beca44`
- Record:
  `rollout-2026-05-26T22-15-22-019e646c-f362-7d82-a331-b228e6beca44.jsonl` /
  line 29859

<a id="u05"></a>

### U05 — Pydantic model convention

해당 Python 구현에서 Pydantic model convention이 적용되지 않았다고 교정했다. 모든 언어·모든 내부 구조를
Pydantic으로 바꾸는 지시는 아니다.

- UTC: `2026-06-09T04:24:19.644Z`
- Session: `019ea468-8916-7e32-8240-f4d5c8d75490`
- Record:
  `rollout-2026-06-08T08-26-14-019ea468-8916-7e32-8240-f4d5c8d75490.jsonl` /
  line 8304

<a id="u06"></a>

### U06 — memory·checkpoint의 중복 소유 제거

기존 runtime의 memory·checkpoint를 재사용하고 단독 호출에서도 persistence가 유지되도록 요청했다.

- UTC: `2026-06-09T15:55:58.492Z`
- Session: `019eacb2-2825-7b11-97ad-51d7ca9af065`
- Record:
  `rollout-2026-06-09T23-03-37-019eacb2-2825-7b11-97ad-51d7ca9af065.jsonl` /
  line 460

<a id="u07"></a>

### U07 — 의존성의 이득 비교 후 설계 채택

별도 인가 엔진의 이득을 질문했다. assistant는 인증·인가 책임 분리, 조회 권한 계획, 운영 비용을 비교했고 사용자는 그 구조의
설계서 작성을 요청했다. 응답의 제품 성능 주장을 이번 사전에서 재검증하거나 보편적 사실로 전재하지 않았다. assistant 답변은 같은
파일 line 343, 후속 사용자 채택은 line 351이다.

- UTC: `2026-07-16T04:48:01.758Z`
- Session: `019f6826-8016-7b42-a3a6-035b86a83af9`
- Record:
  `rollout-2026-07-16T08-39-41-019f6826-8016-7b42-a3a6-035b86a83af9.jsonl` /
  line 330
- UTC: `2026-07-16T04:59:35.785Z`
- Session: `019f6826-8016-7b42-a3a6-035b86a83af9`
- Record:
  `rollout-2026-07-16T08-39-41-019f6826-8016-7b42-a3a6-035b86a83af9.jsonl` /
  line 351

<a id="u08"></a>

### U08 — Markdown 원본·결정 이유·생성 결과

관리하기 어려운 YAML 정의로 돌아간 제안을 교정했다. 충돌·선택 이유와 SQL 기록을 요구했고 inspect용 playground는 운영
prompt·동작과 분리하도록 요청했다. 교정에 대한 assistant 수용은 같은 파일 line 430·444에서 확인했다.

- UTC: `2026-09-21T07:10:06.589Z`
- Session: `01a0c271-61e5-7d00-ad71-790b24e3d190`
- Record:
`rollout-2026-09-21T15-17-09-01a0c271-61e5-7d00-ad71-790b24e3d190_01a0c29c-78a0-71e3-8264-784fccb8633f.jsonl`
  / line 427
- UTC: `2026-09-21T07:33:41.314Z`
- Session: `01a0c271-61e5-7d00-ad71-790b24e3d190`
- Record:
`rollout-2026-09-21T15-17-09-01a0c271-61e5-7d00-ad71-790b24e3d190_01a0c29c-78a0-71e3-8264-784fccb8633f.jsonl`
  / line 554
- UTC: `2026-09-21T08:38:13.162Z`
- Session: `01a0c271-61e5-7d00-ad71-790b24e3d190`
- Record:
`rollout-2026-09-21T15-17-09-01a0c271-61e5-7d00-ad71-790b24e3d190_01a0c29c-78a0-71e3-8264-784fccb8633f.jsonl`
  / line 765

<a id="u09"></a>

### U09 — 채택 전 호환성 검증

UI framework를 구현계획에 넣기 전에 호환성 검증을 요청했다. 그 요청만으로 최종 framework 선택을 확정하지 않았다.

- UTC: `2026-09-21T15:59:37.436Z`
- Session: `01a0c271-61e5-7d00-ad71-790b24e3d190`
- Record:
`rollout-2026-09-21T15-17-09-01a0c271-61e5-7d00-ad71-790b24e3d190_01a0c29c-78a0-71e3-8264-784fccb8633f.jsonl`
  / line 2223

<a id="u10"></a>

### U10 — 현재 문제에 한정한 마무리

현재 문제만 해결해 commit하고 이후 기획·설계는 별도로 재검토하겠다고 범위를 명시했다.

- UTC: `2026-09-21T06:02:38.698Z`
- Session: `01a0c271-61e5-7d00-ad71-790b24e3d190`
- Record:
  `rollout-2026-09-21T14-30-05-01a0c271-61e5-7d00-ad71-790b24e3d190.jsonl` /
  line 368

## 공개 코드 표본

<a id="g01"></a>

### G01 — dynamic-batcher

로컬과 원격 HEAD가 일치했다. 내부 상대 import·__all__·기본 설정·명명·Google식 docstring을 확인했다. 선언
괄호·긴 줄·빈 반환 오류 처리는 현재 지침과 다른 관측으로 남겼다. 해당 파일의 최근 작성자는 Youngju Kim 또는 Youngju
Jaden Kim이다.

- [dynamic_batcher/__init__.py](https://github.com/pydemia/dynamic-batcher/blob/77a309990ddd79b51452d5e6b6244710bc462e57/dynamic_batcher/__init__.py#L1-L30)
- [dynamic_batcher/batcher.py](https://github.com/pydemia/dynamic-batcher/blob/77a309990ddd79b51452d5e6b6244710bc462e57/dynamic_batcher/batcher.py#L17-L195)
- [pyproject.toml](https://github.com/pydemia/dynamic-batcher/blob/77a309990ddd79b51452d5e6b6244710bc462e57/pyproject.toml#L1-L64)

<a id="g02"></a>

### G02 — unipy_dto

GitHub 원문으로 내부 상대 import·Pydantic DTO·설정 클래스를 확인했다. 기본값 보정 정책과 Pydantic v1
API까지 현재 규칙으로 채택하지 않는다. HEAD author login은 pydemia다.

- [unipy_dto/dto/base.py](https://github.com/pydemia/unipy_dto/blob/f4522346cfffe098f0e5aedc54b1f22d91c3f43f/unipy_dto/dto/base.py#L1-L30)
- [unipy_dto/config/base.py](https://github.com/pydemia/unipy_dto/blob/f4522346cfffe098f0e5aedc54b1f22d91c3f43f/unipy_dto/config/base.py#L1-L145)
- [unipy_dto/__init__.py](https://github.com/pydemia/unipy_dto/blob/f4522346cfffe098f0e5aedc54b1f22d91c3f43f/unipy_dto/__init__.py#L1-L4)

<a id="g03"></a>

### G03 — unipy

절대 import·공개 API 집계·NumPy식 docstring template를 확인했다. wildcard·작은따옴표·주석 처리 구현은
현재 요청에 우선하지 않는다. HEAD author login은 pydemia다.

- [unipy/__init__.py](https://github.com/pydemia/unipy/blob/804dd0d8e717aba2544092c5532235a5a3a38e9d/unipy/__init__.py#L56-L87)
- [docstring.py](https://github.com/pydemia/unipy/blob/804dd0d8e717aba2544092c5532235a5a3a38e9d/docstring.py#L1-L82)
- [unipy/stats/api.py](https://github.com/pydemia/unipy/blob/804dd0d8e717aba2544092c5532235a5a3a38e9d/unipy/stats/api.py#L1-L12)

<a id="g04"></a>

### G04 — keycloak-iam

로컬과 원격 HEAD가 일치했다. 절대 import·좁은 Protocol·명시적 타입·keyword-only·선택 FastAPI
extra·frozen dataclass·NumPy식 docstring을 확인했다. 100자·Python 3.13은 프로젝트 설정이다.

- [pyproject.toml](https://github.com/pydemia/keycloak-iam/blob/719c00fbbfb3fad504d3ce26e34062d77f9f8beb/pyproject.toml#L1-L67)
- [src/iam/runtime.py](https://github.com/pydemia/keycloak-iam/blob/719c00fbbfb3fad504d3ce26e34062d77f9f8beb/src/iam/runtime.py#L1-L188)
- [src/iam/bindings/protocols.py](https://github.com/pydemia/keycloak-iam/blob/719c00fbbfb3fad504d3ce26e34062d77f9f8beb/src/iam/bindings/protocols.py#L1-L100)
- [src/iam/models.py](https://github.com/pydemia/keycloak-iam/blob/719c00fbbfb3fad504d3ce26e34062d77f9f8beb/src/iam/models.py#L1-L50)

<a id="g05"></a>

### G05 — tasklens

로컬과 원격 HEAD가 일치했다. 실행별 상태·오래된 fetch 무효화·공유 snapshot·cleanup을 확인했다. 탭·작은따옴표는 이
TS 저장소의 지역 서식이다. AGENTS의 요약보다 실제 코드의 상태 구분을 근거로 삼았다.

- [src/runner/registry.ts](https://github.com/pydemia/tasklens/blob/5962388b98c574f21891a521721a23f6f667a362/src/runner/registry.ts#L1-L155)
- [src/taskCatalog.ts](https://github.com/pydemia/tasklens/blob/5962388b98c574f21891a521721a23f6f667a362/src/taskCatalog.ts#L1-L92)

<a id="g06"></a>

### G06 — pydantic-config

초기 타입·설정 실험 표본이다. 오래된 설정·모듈 전역 사용을 신규 기본으로 채택하지 않았다. 원문의 환경별 설정값을 사전 예제로 복제하지
않는다. HEAD author login은 pydemia다.

- [accucfg/api.py](https://github.com/pydemia/pydantic-config/blob/a1cd71f365c04b912fd617b17630e320e401444b/accucfg/api.py#L36-L42)
- [accucfg/types/base.py](https://github.com/pydemia/pydantic-config/blob/a1cd71f365c04b912fd617b17630e320e401444b/accucfg/types/base.py#L1-L45)

<a id="g07"></a>

### G07 — errorcode

PascalCase·snake_case·대문자 enum·__all__을 확인했다. enum 구현 세부와 case-insensitive 보정을
개인 공통 규칙으로 올리지 않았다. HEAD author login은 pydemia다.

- [src/enums.py](https://github.com/pydemia/errorcode/blob/daf50d56eb840cb171fad409f71ef170da43fd88/src/enums.py#L1-L69)

## 로컬 지침·설정

다음 경로는 로컬 git 폴더 기준이다. 비공개 원문은 복제하지 않았다.
SHA-256은 읽은 파일의 식별용이며 원문을 복원하거나 접근 권한을 제공하지
않는다. Git revision과 파일 hash를 함께 사용한다.

<a id="l01"></a>

### L01 — agent-skills-model-recommendations

보관된 개인 소프트웨어 개발 지침. 기존 규칙 우선·작은 완결 변경·추적 가능한 구조·타입·오류·79자·문서·검증을 직접 읽었다. 모델별
추천은 변동성이 크고 코드 스타일이 아니므로 이 사전에 복제하지 않았다.

- 경로:
`agent-skills-model-recommendations/library/instructions/software-engineering.md`
- HEAD: `b1f1122275b45179cbb6cd69c16d9dd8399d55a4`
- SHA-256: `597ae1c32b8a7b3a3668370b62b6f9f3ae8631946b8c58480873768ed9253dea`
- 파일 상태: 해당 파일은 HEAD와 동일

<a id="l02"></a>

### L02 — semantic-query

현재 라이브러리의 개발 가이드. 호스트 자원 소유·선택 web·서버 검증·실행 증거·API와 UI 상태·테스트 구분의 조건부 근거다.

- 경로: `semantic-query/docs/code-conventions.md`
- HEAD: `591e86640349d84ce41e44a179b7789c7f09f30c`
- SHA-256: `53737b8df941bb66965b537f4a8d271fa7cd55315d21445a8f0827a1f7274fce`
- 파일 상태: 해당 파일은 HEAD와 동일

<a id="l03"></a>

### L03 — template-backend

과거 backend의 Python 서식 설정. 해당 설정 추가 commit 5e967b2의 author는
Youngju Kim이다. 현재 파일에는
미커밋 변경이 있으므로 HEAD와 동일한 원문이라고 주장하지 않는다. 공백 4칸·큰따옴표·120자·auto 개행을 확인했다.

- 경로: `template-backend/pyproject.toml`
- HEAD: `af5722e7321cf5f0719debcde06410488180ca93`
- SHA-256: `e0b4f04b2312c4720b1a06f1918bb2d22da211a028911fc1d07b40dc1b31c684`
- 파일 상태: 미커밋 변경 포함

<a id="l04"></a>

### L04 — agent-skills-model-recommendations

사이트 편입을 위한 원본·생성물·publish 규칙. 로컬 main보다 최근인 별도 checkout을 읽었다. GitHub API에서는
agent-skills가 404여서 원격 공개 검증을 하지 못했다.

- 경로: `agent-skills-model-recommendations/docs/conventions.md`
- HEAD: `b1f1122275b45179cbb6cd69c16d9dd8399d55a4`
- SHA-256: `c6b90b22f34052628a6d49ee00a53018709c97e49009008cdeead7e99a18b464`
- 파일 상태: 해당 파일은 HEAD와 동일

<a id="l05"></a>

### L05 — semantic-query

Python 100자·mypy strict·optional extras를 확인했다. 현재 프로젝트 설정이며 개인 전체의
toolchain으로 일반화하지 않았다.

- 경로: `semantic-query/pyproject.toml`
- HEAD: `591e86640349d84ce41e44a179b7789c7f09f30c`
- SHA-256: `6863e72a722da81a9829bacc38d83443af19e68763352fcef2cb2cb06a9dd388`
- 파일 상태: 해당 파일은 HEAD와 동일

<a id="l06"></a>

### L06 — agent-skills-model-recommendations

ancestor·common ancestor·merge base를 다른 의미로 유지하는 활성 용어 항목. line 185–256을 현재 로컬
자료로 재확인했다.

- 경로:
`agent-skills-model-recommendations/terminology/glossary/software-engineering.yaml`
- HEAD: `b1f1122275b45179cbb6cd69c16d9dd8399d55a4`
- SHA-256: `e2f41b8faeb347488dcd4e35ba99978ed087ceb9b35db5677b4eb3a016b74dec`
- 파일 상태: 해당 파일은 HEAD와 동일

<a id="l07"></a>

### L07 — tasklens 로컬 작업 지침

로컬 AGENTS.md는 작업 경계를 이해하는 보조 자료로 읽었다. 해당 파일은
공개 commit의 contents API에서 조회되지 않아 공개 코드 링크에서 제외했다.
G05의 동작 판단은 실제 TypeScript 파일을 기준으로 한다.

- 경로: `tasklens/AGENTS.md`
- checkout HEAD: `5962388b98c574f21891a521721a23f6f667a362`
- SHA-256: `855b7f3e158e07051bb61f9a1a30ac14a51e632a788f8d094544b52d8a04db74`
- 파일 상태: 공개 commit에 포함된 자료로 검증되지 않은 로컬 파일

공동 작업 저장소인 SDK·backend는 작성 이력도 표본 확인했다. SDK의 서버와
CLI 파일 일부는 다른 author의 변경이어서 pydemia 고유 서식의 증거로
채택하지 않았다. git-code-reviewer는 로컬과 원격 HEAD가 달라 해당 코드를
고정된 공개 근거로 사용하지 않았다. GitHub non-fork 여부만으로 원작성자를
확정하지 않는 이유다.
