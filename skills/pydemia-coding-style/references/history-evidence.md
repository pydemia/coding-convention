# 추가 대화·memory 근거

전체 대화 원문은 저장소에 게시하지 않는다. 아래는 사용자 요청의 의미와
로컬 재확인용 위치다. 날짜는 JSONL 기록 시각이며 이관된 대화의 최초 작성
시각을 보증하지 않는다. 같은 session의 순서와 실제 후속 교정을 함께 본다.

<a id="u11"></a>

## U11 — 구체적인 타입

factory의 Any 대신 호출 가능한 base/interface 타입을 요청했다.

- 기록 `ed06b96aa21fbd87`: 2026-05-21, session
  `019e20e2-c1cd-7910-b493-45a11f7bc07b`, JSONL line 15274.
- 기록 `101032d131a9bd60`: 2026-05-21, session
  `019e20e2-c1cd-7910-b493-45a11f7bc07b`, JSONL line 15355.
<a id="u12"></a>

## U12 — DTO와 직렬화

DTO를 Pydantic으로 통일하고 이중 파싱을 줄이며 intent의 enum화를 요청했다. 내부 값 전체의 Pydantic 전환은 아니다.

- 기록 `f716189fa871df92`: 2026-05-18, session
  `019e20e2-c1cd-7910-b493-45a11f7bc07b`, JSONL line 3378.
- 기록 `2f5b0d1780149f01`: 2026-06-13, session
  `019e646c-f362-7d82-a331-b228e6beca44`, JSONL line 43906.
- 기록 `c2664b7f1900d08f`: 2026-06-13, session
  `019e646c-f362-7d82-a331-b228e6beca44`, JSONL line 44121.
- 기록 `fa10fe43f9f3c661`: 2026-05-29, session
  `019e646c-f362-7d82-a331-b228e6beca44`, JSONL line 20259.
- 기록 `a092e80311094560`: 2026-06-23, session
  `019ed694-be26-7000-9337-a428f370378c`, JSONL line 1879.
<a id="u13"></a>

## U13 — runtime 환경값

설치 시 환경값 고정을 교정하고 Pydantic Settings 기반 runtime 설정을 요청했다.

- 기록 `c35affd452082b9b`: 2026-05-06, session
  `019dfd97-32b2-7a01-be6b-28fb1d97a94f`, JSONL line 537.
- 기록 `e37f507ddaab7806`: 2026-06-24, session
  `019ed694-be26-7000-9337-a428f370378c`, JSONL line 4444.
<a id="u14"></a>

## U14 — 오류의 발견 시점

lazy import가 실패를 늦추는 문제와 필수 credential의 lifespan 검증을 지적했다. 선택 library의 import
부작용 허가는 아니다.

- 기록 `2b0effede7271b38`: 2026-05-19, session
  `019e20e2-c1cd-7910-b493-45a11f7bc07b`, JSONL line 8047.
- 기록 `10222e99014a7f21`: 2026-05-26, session
  `019e4d23-7969-7242-8065-e7145752c51e`, JSONL line 1730.
<a id="u15"></a>

## U15 — 기본값의 소유자

반복 timeout을 field 기본값으로 옮기고 변경된 옵션만 설정에 적도록 요청했다. is_resume=False는 해당 API의
결정이다.

- 기록 `b789abb9bdf7677e`: 2026-06-09, session
  `019e646c-f362-7d82-a331-b228e6beca44`, JSONL line 40174.
- 기록 `c3960821dfdf5b11`: 2026-06-01, session
  `019e646c-f362-7d82-a331-b228e6beca44`, JSONL line 27517.
- 기록 `72e6e8f2ead152e0`: 2026-06-01, session
  `019e646c-f362-7d82-a331-b228e6beca44`, JSONL line 27571.
- 기록 `f97de9e6aabec4be`: 2026-05-19, session
  `019e20e2-c1cd-7910-b493-45a11f7bc07b`, JSONL line 9890.
<a id="u16"></a>

## U16 — 재현성

query rewrite와 scoring의 반복 결과 불안정을 문제로 제기했다. 후속 작업에서 temperature를 설정하지 않겠다고
명시했다.

- 기록 `3a031c16cb180681`: 2026-06-25, session
  `019ed694-be26-7000-9337-a428f370378c`, JSONL line 10030.
- 기록 `f6fd95ae3a16b49b`: 2026-09-13, session
  `01a0991f-a214-73d3-9cf7-3daea1bc40e8`, JSONL line 3618.
- 기록 `1c6b500ef34ed4cb`: 2026-09-13, session
  `01a0991f-a214-73d3-9cf7-3daea1bc40e8`, JSONL line 7002.
<a id="u17"></a>

## U17 — 의존성과 모듈 경계

과도한 하위 모듈을 줄이는 한편 구현체가 많은 agents 디렉터리는 유지했다. 범용 package에서 업무 데이터 의존성 제거를 요청했다.

- 기록 `f74f5f653791e01c`: 2026-05-26, session
  `019e646c-f362-7d82-a331-b228e6beca44`, JSONL line 5064.
- 기록 `700414659255e5e8`: 2026-06-13, session
  `019e646c-f362-7d82-a331-b228e6beca44`, JSONL line 43961.
- 기록 `6826bbed134b0183`: 2026-06-07, session
  `019ea468-8916-7e32-8240-f4d5c8d75490`, JSONL line 169.
- 기록 `de51c90c99ee63c5`: 2026-06-24, session
  `019ed694-be26-7000-9337-a428f370378c`, JSONL line 7087.
<a id="u18"></a>

## U18 — 문자열 구현의 유지보수

실제 함수 대신 소스 문자열을 병합하거나 거대한 string concatenation으로 조립하는 구조를 문제로 지적했다.

- 기록 `260d1d610ab2f42c`: 2026-05-03, session
  `019def9f-92aa-7a32-9dc9-d0906e8b9036`, JSONL line 1184.
- 기록 `cf68084c2aba4e0f`: 2026-06-09, session
  `019ea468-8916-7e32-8240-f4d5c8d75490`, JSONL line 8043.
<a id="u19"></a>

## U19 — 사용자 선택의 실행 반영

계정 인증을 이용한 모델 목록과 실행 경로를 확인하도록 요청했다. 실제 사용 화면이 터미널 TUI라는 직접 선택 응답도 확인했다.
실행값 전파 수정의 상세 이력은 memory를 보조 근거로 사용했다.

- 기록 `7e11bb384cb5b69d`: 2026-09-09, session
  `01a0605c-06e7-7fe3-8a88-30c274d7df65`, JSONL line 1230.
- 기록 `fd4aa1e2f771bbab`: 2026-09-09, session
  `01a0841a-68a2-7b13-9cac-106c1399f306`, JSONL line 9.
- TUI 응답 `92519b56be628742`: 2026-09-09, session
  `01a08886-f74c-78f3-b34b-d3f0158d2e44`, JSONL line 53.

<a id="u20"></a>

## U20 — YAML 렌더링

ConfigMap의 text syntax가 잘못 렌더링되는 문제를 조사·수정하도록 요청했다. 당시 원인을 들여쓰기로 확정했다는 뜻은 아니다.

- 기록 `a94e9bf94f3fc48d`: 2026-06-18, session
  `019edbdb-081a-7cf2-87a4-7d702485ef86`, JSONL line 6.
<a id="u21"></a>

## U21 — prompt 줄바꿈과 env 참조

prompt YAML의 과도한 줄바꿈을 지적하고 환경변수 placeholder로 설정값을 받도록 요청했다. token 감소는 측정하지 않았다.

- 기록 `f2b45179838f6506`: 2026-06-18, session
  `019ed694-be26-7000-9337-a428f370378c`, JSONL line 1622.
- 기록 `d280a1ab6c50c060`: 2026-06-24, session
  `019ed694-be26-7000-9337-a428f370378c`, JSONL line 4591.
<a id="u22"></a>

## U22 — credential 주입

일반 설정과 credential의 ConfigMap/Secret 경로를 분리하고 공개 예제의 실제 저장소 이름을 익명화하도록 요청했다.

- 기록 `4500675c6d646d09`: 2026-05-27, session
  `019e646c-f362-7d82-a331-b228e6beca44`, JSONL line 11051.
- 기록 `3a0715ca0a2dbe4b`: 2026-09-07, session
  `01a05b6c-e021-7ce1-8696-fcead528058c`, JSONL line 10289.
<a id="u23"></a>

## U23 — 업무 규칙의 관리 원본

업무 의미를 validator·test에 중복 정의하지 않고 운영 정의 원본을 참조하도록 교정했다. 이후 Markdown 원본 선택은 U08을
따른다.

- 기록 `884025952e7f34ab`: 2026-06-21, session
  `019eea5c-da7b-7373-9f43-d22a49d45512`, JSONL line 8161.
- 기록 `4d7bc1ded2e17321`: 2026-06-21, session
  `019eea5c-da7b-7373-9f43-d22a49d45512`, JSONL line 8206.
- 기록 `0c8d10f3e41a16a7`: 2026-06-21, session
  `019eea5c-da7b-7373-9f43-d22a49d45512`, JSONL line 8520.
- 기록 `bdd851790692f121`: 2026-06-21, session
  `019eea5c-da7b-7373-9f43-d22a49d45512`, JSONL line 8675.
- 기록 `ce08ab7f3ba61f58`: 2026-06-21, session
  `019eea5c-da7b-7373-9f43-d22a49d45512`, JSONL line 8887.
- 기록 `18a962a04750e630`: 2026-06-23, session
  `019eeb54-8c04-70e0-b46d-cac5e2ca2c0d`, JSONL line 986.
<a id="u24"></a>

## U24 — 설정 우선순위

home/cwd와 env/local override를 명시적으로 다루도록 요청했다. 프로젝트가 달라 전역적인 단일 소스 순서는 도출하지
않았다.

- 기록 `01571542a8657844`: 2026-05-10, session
  `019e10bc-09a4-7441-acaa-a3e38b75d8d1`, JSONL line 6.
- 기록 `b375e05feba70078`: 2026-06-01, session
  `019e646c-f362-7d82-a331-b228e6beca44`, JSONL line 26168.
- 기록 `74d6b59a59c6075d`: 2026-06-01, session
  `019e646c-f362-7d82-a331-b228e6beca44`, JSONL line 27642.
<a id="u25"></a>

## U25 — prompt와 코드 판정

특정 업무 흐름의 과한 코드 차단·정규식과 부정문 prompt를 교정했다. 권한·게시 검증까지 prompt에 위임한다는 결정은 아니다.

- 기록 `00c3853a91e508dd`: 2026-06-01, session
  `019e646c-f362-7d82-a331-b228e6beca44`, JSONL line 27271.
- 기록 `742a8e7553b17ca4`: 2026-05-29, session
  `019e4d23-7969-7242-8065-e7145752c51e`, JSONL line 4878.
- 기록 `5366334b592a76de`: 2026-06-04, session
  `019e8c50-6bc0-70a2-97af-95b77ca88486`, JSONL line 37188.
- 기록 `9cf4079a05b3ee0f`: 2026-06-21, session
  `019eeb12-8b0f-70e0-96c4-35b7d8452db0`, JSONL line 3139.
<a id="u26"></a>

## U26 — Helm override

upstream values/template 보존과 환경 전용 override 사용을 반복 명시했다.

- 기록 `85cc5e1428345a43`: 2026-06-26, session
  `019effd1-fe62-7c53-8609-271e8c5683bc`, JSONL line 1360.
- 기록 `f1c7d7ceaa519e1c`: 2026-06-26, session
  `019effd1-fe62-7c53-8609-271e8c5683bc`, JSONL line 1462.
- 기록 `5d9fc8dd7b9fb49d`: 2026-06-26, session
  `019f0342-c471-77d3-a5d1-44c0219a3ff1`, JSONL line 982.
<a id="u27"></a>

## U27 — 요약과 상세 문장

요약은 목록으로 줄이고 자세한 설명은 산문으로 유지하도록 요청했다. 특정 보고서의 개조식 요구를 모든 산출물에 강제하지 않는다.

- 기록 `ef44eae054802fff`: 2026-09-09, session
  `01a07fdc-bf9f-7d21-bfed-4f35d4057a8f`, JSONL line 4794.
- 기록 `3792d78e9b168927`: 2026-09-13, session
  `01a0991f-a214-73d3-9cf7-3daea1bc40e8`, JSONL line 7271.
<a id="u28"></a>

## U28 — 공개 예제와 근거

공개 예제를 익명화하고 리뷰 내용이 있는 항목 위주로 읽기 쉽게 게시하도록 요청했다.

- 기록 `3a0715ca0a2dbe4b`: 2026-09-07, session
  `01a05b6c-e021-7ce1-8696-fcead528058c`, JSONL line 10289.
- 기록 `aee52b8a8bc46895`: 2026-09-09, session
  `01a07fdc-bf9f-7d21-bfed-4f35d4057a8f`, JSONL line 4411.
<a id="u29"></a>

## U29 — 설계 결정 갱신

구조와 선택의 이유를 architecture 문서 및 관련 시각 자료에 함께 반영하도록 요청했다.

- 기록 `1899396e5c77356a`: 2026-05-05, session
  `019df8ac-6ca8-76c0-bd10-3e6aef271945`, JSONL line 394.
- 기록 `a48550adb6170339`: 2026-05-29, session
  `019e4d23-7969-7242-8065-e7145752c51e`, JSONL line 3997.
<a id="u31"></a>

## U31 — 이관 뒤 호환 코드

이관을 끝낸 import shim과 이전 구현을 정리하고 안정성을 검증하도록 요청했다.

- 기록 `98d629c649291205`: 2026-06-02, session
  `019e4d23-7969-7242-8065-e7145752c51e`, JSONL line 8713.
- 기록 `61106dbd135614c2`: 2026-06-08, session
  `019ea468-8916-7e32-8240-f4d5c8d75490`, JSONL line 6130.
- 기록 `adb3cd573811cc9e`: 2026-06-25, session
  `019ed694-be26-7000-9337-a428f370378c`, JSONL line 10560.
<a id="u32"></a>

## U32 — 실제 배포 artifact

개발 workspace 의존성을 배포 package에 남기지 않도록 교정했고 OS별 실제 검증과 보존 범위를 명시했다.

- 기록 `8cfff6911ed45d49`: 2026-05-19, session
  `019e3e93-b658-77a2-82da-8313f4bb1102`, JSONL line 1783.
- 기록 `9a1e4d4be5878896`: 2026-05-19, session
  `019e3fc7-8ed6-7212-bdf3-af8c347db1bd`, JSONL line 6.
- 기록 `5a11e61a7753d21c`: 2026-09-16, session
  `01a09445-6477-7e43-ab1c-f2590ddf58cd`, JSONL line 57471.
<a id="u33"></a>

## U33 — commit 메시지

사용자가 제공한 생성 prompt: 제목 [Type]과 동사 원형, 제목 50자, 본문 300자, bullet 50자 미만, 무엇과 왜를
설명. 당시 제품 규칙이므로 전역 명시가 아닌 선호로 반영했다.

- 기록 `54b24cd53ad3b9a5`: 2026-05-06, session
  `019dfd97-32b2-7a01-be6b-28fb1d97a94f`, JSONL line 7371.
<a id="u34"></a>

## U34 — 변경·충돌의 시계열

수치·DI 경로·direct_answer·fallback·recipe·formatter의 변경 이력을 비교했다. 같은 범위에서 최신 사용자가
명시한 결정을 기준으로 판단한다.

- 기록 `e21c7bf4648920e9`: 2026-05-08, session
  `019e08db-a373-7b80-ba73-edae5455b11f`, JSONL line 213.
- 기록 `e6bf50ffeb08590d`: 2026-05-11, session
  `019e17c2-46a6-7d92-8c90-c7757e9270c6`, JSONL line 6.
- 기록 `9f4ea3d4343edc71`: 2026-05-26, session
  `019e6167-5704-71e0-8510-1c249b39b435`, JSONL line 585.
- 기록 `b43489f99dae3e92`: 2026-05-26, session
  `019e4d23-7969-7242-8065-e7145752c51e`, JSONL line 2105.
- 기록 `d9f71fa6bfead541`: 2026-05-29, session
  `019e646c-f362-7d82-a331-b228e6beca44`, JSONL line 25365.
- 기록 `aa4f442bed55dd97`: 2026-06-02, session
  `019e4d23-7969-7242-8065-e7145752c51e`, JSONL line 10837.
- 기록 `c0df3a2e3f922248`: 2026-06-02, session
  `019e4d23-7969-7242-8065-e7145752c51e`, JSONL line 13029.
- 기록 `74eb8a33e149bcfb`: 2026-06-02, session
  `019e646c-f362-7d82-a331-b228e6beca44`, JSONL line 35555.
- 기록 `c513026c5101835c`: 2026-06-04, session
  `019e8c50-6bc0-70a2-97af-95b77ca88486`, JSONL line 37059.
- 기록 `5366334b592a76de`: 2026-06-04, session
  `019e8c50-6bc0-70a2-97af-95b77ca88486`, JSONL line 37188.
- 기록 `f6ca987b221e40bd`: 2026-06-09, session
  `019eacb2-2825-7b11-97ad-51d7ca9af065`, JSONL line 2018.
- 기록 `d44b4c65dc94d8ba`: 2026-06-17, session
  `019ed694-be26-7000-9337-a428f370378c`, JSONL line 866.

<a id="u30"></a>

## U30 — 현재 정책의 시간 우선순위

2026-09-23 이번 대화에서 동일 범위의 충돌은 최신 기준을 우선하고 결정이
반복해서 바뀐 경우 따로 정리해 의사결정할 수 있게 제시하도록 요청했다.
이 요청이 과거 선택을 분류하는 현재 기준이다.

<a id="m01"></a>

## M01 — 리뷰 근거와 심각도

로컬 memory registry의 line 57–67 및 해당 복구·리뷰 요약을 읽었다.
자동 리뷰의 원래 번호·범위, 결함과 조건부 위험의 구분, 서로 다른 심각도
체계의 구분이 기록되어 있다. memory는 원문 대화를 찾는 보조 근거이며
모든 항목을 개인 명시 규칙으로 승격하지 않았다.

- Memory session: `01a0b8db-9091-7031-8bb6-38d7240e656d`.
- 연결된 요약: `2026-09-19T08-49-52-Wcax`로 시작하는 복구 기록.

<a id="m02"></a>

## M02 — 검증 범위·긴 게시물·실행 설정

registry의 line 202–215, raw memory의 실행 모델 선택 기록과 관련 요약을
읽었다. 실제 OS 검증·artifact 보존·게시 내용 단위의 생략 기준을 조사에
반영했다. 특정 작업의 실제 모델 호출 0회나 quota 중지 조건을 모든 개발
작업의 고정 규칙으로 일반화하지 않았다.

- Regression session: `01a09445-6477-7e43-ab1c-f2590ddf58cd`.
- Runtime selection session: `01a08886-f74c-78f3-b34b-d3f0158d2e44`.

<a id="u35"></a>

## U35 — 보완 검색에서 확인한 결정과 번복

config의 agent→agents→agent, memory schema 제거→정정, timeout의
선언 위치 변경을 원문 순서로 확인했다. 같은 이름을 한 번 바꾼 사례와 실제
되돌린 사례를 구분한다. process.env까지의 override 순서, bool을 반환하는
함수의 is 이름, 독립 package의 테스트 환경, 동일 코드 재검증의 생략 요구도
추가 확인했다. 이 자료는 초기 convention 키워드 검색 밖에서 발견됐다.

- `392f79dd9375e98b`: 2026-05-27T23:34:06, session
  `019e646c-f362-7d82-a331-b228e6beca44`, JSONL line 10549.
- `e3bab55de689dd28`: 2026-05-27T23:39:52, session
  `019e646c-f362-7d82-a331-b228e6beca44`, JSONL line 10667.
- `f032aa3b7a8e7294`: 2026-05-27T23:51:34, session
  `019e646c-f362-7d82-a331-b228e6beca44`, JSONL line 10899.
- `bce0390fcd9125e5`: 2026-06-09T14:34:50, session
  `019e4d23-7969-7242-8065-e7145752c51e`, JSONL line 17161.
- `b789abb9bdf7677e`: 2026-06-09T16:05:13, session
  `019e646c-f362-7d82-a331-b228e6beca44`, JSONL line 40174.
- `0158701db27fd0d5`: 2026-06-12T11:44:19, session
  `019e646c-f362-7d82-a331-b228e6beca44`, JSONL line 40656.
- `e84ac6de6558cef0`: 2026-06-12T11:45:05, session
  `019e646c-f362-7d82-a331-b228e6beca44`, JSONL line 40666.
- `e5eebb5bdebf6e53`: 2026-05-20T07:40:09, session
  `019e440b-d30a-7420-bc2b-35adc41f69c9`, JSONL line 507.
- `800b51b69937d9f5`: 2026-06-25T04:13:50, session
  `019ed694-be26-7000-9337-a428f370378c`, JSONL line 10374.
- `1e79e2ac62de70dc`: 2026-06-02T05:49:07, session
  `019e4d23-7969-7242-8065-e7145752c51e`, JSONL line 9738.
- `817efe344d76e6ac`: 2026-06-21T19:53:30, session
  `019eea5c-da7b-7373-9f43-d22a49d45512`, JSONL line 4981.
- `a097c33cfd51491f`: 2026-09-13T06:57:31, session
  `01a0991f-a214-73d3-9cf7-3daea1bc40e8`, JSONL line 1032.

같은 날의 timeout 요청은 시각까지 비교했다. 선언부 지정(14:34 UTC)보다
Field 기본값 통합(16:05 UTC)이 나중이다. memory schema도 06-12의
정정 뒤 06-13 후속 요청까지 비교해 아래 기록을 최신 기준에 포함했다.

- `cb5ed6ebd9f72e80`: 2026-06-12T11:36:40, session
  `019e646c-f362-7d82-a331-b228e6beca44`, JSONL line 40479.
- `d8e6532513481c77`: 2026-06-12T11:39:42, session
  `019e646c-f362-7d82-a331-b228e6beca44`, JSONL line 40546.
- `d8c1f0a43c2eb2ea`: 2026-06-13T08:28:41, session
  `019e646c-f362-7d82-a331-b228e6beca44`, JSONL line 45298.
- `fecfbaad25690e24`: 2026-06-13T08:50:41, session
  `019e646c-f362-7d82-a331-b228e6beca44`, JSONL line 45460.
