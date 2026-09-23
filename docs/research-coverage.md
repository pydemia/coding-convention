# 조사 범위와 재확인 방법

기준일: 2026-09-23. 최초 표본 조사를 확대해 원격 목록·로컬 Git root·
Codex 기록의 전체 후보 목록을 만들고, 파일 내용 검색과 선택한 근거의 직접
검토를 분리했다. 숫자는 개인 스타일의 빈도나 수동 작성한 파일 수가 아니다.

| 자료 | 실제 확인 범위 |
|---|---|
| 인증된 GitHub 목록 | 소유 저장소 410개, non-fork 239개, 그중 비공개 83개 |
| non-fork 수집 | Git clone 212개, 빈 clone 4개, 소스 snapshot 23개 |
| 로컬 Git root | 154개. 중첩 checkout·외부 소스·commit 없는 경로 포함 |
| Git 이력 | 로컬·clone 370개에서 조회. commit 없는 로컬 4개 제외. 일치 author의 중복 제거 commit 6,721개 |
| 가장 오래된 일치 author 기록 | 2016-11-01. Git 이력의 시작이며 Codex 기록 시작은 아님 |
| Codex 기록 | 기본·업무용 profile의 sessions·archived sessions 268개와 history.jsonl |
| 가장 오래된 Codex session | 2026-05-02 |
| 초기 정책 검색 | 중복 제거 뒤 후보 547개. 결정·질문·붙여넣은 문서·위임 prompt가 섞여 있어 확정 결정 수로 세지 않음 |
| 보완 검색 | 초기 키워드 밖의 짧은 요청 후보 355개. 재검사해 이름 번복·override·검증 생략 등 추가 반영 |
| 명시 선택 응답 | 동기 응답 1건의 3개 선택과 비동기 사용자 answer 11건 확인. 질문 전달 성공·빈 답변 제외 |
| memory | registry·raw memory와 연결된 rollout 요약 9개를 검색·대조. 보존된 memory Git 이력은 1개 revision |
| 파일 내용 검사 | 65,374개 후보 중 UTF-8 텍스트 64,988개 읽음. 동일 내용 제외 39,985개 |
| 정책·도구 설정 | 중복 제외 603개 후보 문서에서 규칙·formatter·타입·import 관련 내용 검색 |

## 파일별 검사와 직접 검토의 차이

후보마다 경로·revision·크기·SHA-256·읽기 결과·언어를 남겼다. 읽은 텍스트는
줄 길이·들여쓰기·개행·상대/절대 import·타입 model·docstring·mixin 등의
패턴으로 검색했다. 아래는 검사한 파일 수이며 지지하는 개인 표본 수가 아니다.
책 코드·vendor·중복 worktree가 포함되므로 다수결로 규칙을 정하지 않았다.

| 언어 | 읽은 경로 수 | 중복 제거 내용 수 |
|---|---|---|
| Python | 35,737 | 23,284 |
| YAML | 17,295 | 8,348 |
| Markdown | 9,059 | 5,860 |
| Java | 1,342 | 1,327 |
| Kotlin | 159 | 157 |
| Notebook | 400 | 292 |

내용 검색 뒤 직접 판단한 자료에는 개인 공통 지침, 프로젝트 convention,
Python library·설정·DTO, YAML loader·prompt의 사용자 교정, Markdown
원본 관리, Java 작성 표본, Kotlin 설계 지침과 튜토리얼 provenance가 있다.
전체 코드를 한 줄씩 수동 정독하거나 모든 과거 revision의 모든 행을 분석한
것은 아니다. Git 이력의 전체 commit·변경 경로 조회와 선택 파일의 내용
검토를 구분한다. 결과는 [사전 근거](../skills/pydemia-coding-style/references/evidence.md),
[추가 대화](../skills/pydemia-coding-style/references/history-evidence.md),
[언어별 근거](../skills/pydemia-coding-style/references/language-evidence.md)에 연결했다.

## 수집과 제외 기준

디스크 여유가 처음에는 약 467MiB여서 5MiB 이하부터 clone했다. 사용자가
공간을 확보한 뒤 GitHub 표시 용량 50MiB 이하까지 확대했다. clone은
`--filter=blob:none`을 사용하며 shallow clone이 아니다. commit·tree 이력을
보존하고 현재 checkout의 파일을 받았다. LFS 대용량 객체·submodule은 자동
수집하지 않았다. 표시 용량은 GitHub metadata이므로 실제 사용량과 다르다.

50MiB 초과 저장소는 commit을 고정해 소스·문서·설정을 내려받았다. 모델,
이미지, archive 같은 binary는 제외했다. node_modules·vendor·build 등은
분리했고 tree 응답이 잘리면 하위 tree를 다시 조회했다. 큰 데이터 파일은
제외 목록에 기록했다. notebook은 지원되는 JSON 구조의 code output을
비우며 실행하지 않았다. 변환된 notebook은 원본과 byte 동일하지 않다.

UTF-8로 읽히지 않은 파일 37개는 외부 plugin·LangChain
fixture 계열로 별도 표시했다. dependency/build 경로 278개는
내용 분석에서 제외했다. 최초 목록 이후 없어진 파일·symlink 상태
31개와 소스로 오인할 수 있는 macOS binary metadata 40개도 따로
기록했다. 후자는 이번 source snapshot에서 제거했다. 이 제외를 정상적인 개인 코드로 집계하지 않았다. 이 사전
자체와 이 사전의 clone은 규칙을 지지하는 입력에서 제외했다.

macOS의 대소문자를 구분하지 않는 파일시스템 때문에 오래된 두 clone의
`Lot.py`와 `lot.py`가 같은 경로에 겹쳤다. Git object의 네 원본을 각각
hash가 다른 이름으로 `repos/_audit/case-collisions/`에 보존했다. 따라서
두 checkout이 clean하다고 표시하지 않았으며 내용을 잃은 채 수집 완료로
처리하지 않았다. 중단된 clone 하나의 미완료 checkout은 복원 후 재검사했다.

저장소별 수집 방식·revision은 [수집 목록](repository-coverage.md)에 있다.
비공개 이름은 공개 목록에서 익명화했다. 전체 이름·파일별 제외 사유·원문
위치는 gitignored `repos/_audit/`의 JSON에 남아 로컬에서 다시 확인할 수 있다.
인증값과 대화 원문은 게시 파일에 넣지 않았다. clone origin에는 credential을
넣지 않았고 기존 origin의 token은 인증할 때만 메모리에서 읽었다.

## 로컬 재확인 자료

- `repos/_audit/github-inventory.json`: 인증된 GitHub 전체 목록.
- `repos/_audit/collection.json`: 저장소별 상태·수집 방식·고정 revision.
- `repos/_audit/files-*.json`: 큰 저장소의 파일별 수집·제외 결과.
- `repos/_audit/local-inventory.json`, `git-history.json`: 로컬 목록·작성 이력.
- `repos/_audit/content-files.json`: 내용 hash·검사 결과·중복 여부.
- `repos/_audit/content-policies.json`: 정책 문서의 검색 위치.
- `repos/_audit/history-records.json`, `async-answers.json`: 원문 재확인 위치.

이 파일들은 공개 배포용 데이터가 아니다. 조사 스크립트도 저장소 코드나
원격 문서에 포함된 명령을 실행하지 않으며 읽기·검색만 수행했다. 다른
checkout을 변경하지 않았다. 삭제·미동기화·다른 기기에만 있는 과거 대화,
큰 저장소의 전체 Git 이력, 제외된 submodule 내용까지 확인한 주장은 하지 않는다.
