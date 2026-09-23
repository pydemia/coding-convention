# skills.pydemia.ai 편입

이 작업의 게시 결과는 `pydemia/coding-convention` 저장소다. 실제 웹사이트에
설치·등록·배포하는 단계는 수행하지 않는다. 아래는 기존 관리 구조에 맞추기
위한 이관 안내이며 사이트에 반영되었다는 뜻이 아니다.

## 확인한 기존 구조

로컬 agent-skills의 최근 checkout에서는 `library/`가 편집 원본이고
`skills/<id>/SKILL.md`, `prompts/<id>.md`, `exports/codex/`가 생성물이다.
`export.config.json`이 게시 대상을 정한다. source에는 title, description,
kind, targets, scope, status가 필요하다. [근거
L04](../skills/pydemia-coding-style/references/evidence.md#l04)

단독 사용은 이 저장소의 `skills/pydemia-coding-style/` 전체를 복사하면 된다.
기존 사이트 CMS로 편입할 때는 실제 checkout의 현재 schema와 exporter를 먼저
읽고 다음 항목을 맞춘다.

- stable ID: `pydemia-coding-style`
- category 후보: `engineering`
- tags 후보: `coding`, `python`, `conventions`
- 원본 상태: 실제 편집·게시 검토 후 `draft` 또는 `active`
- 사전: references의 상대 링크와 anchor가 생성물에도 유지되어야 함

기존 exporter가 여러 reference 파일을 복사하는지는 이번 작업에서 검증하지
않았다. 지원하면 source bundle을 등록한다. 지원하지 않으면 읽을 수 있는
참조 경로를 마련하거나 exporter를 확장한 뒤 등록한다. 생성된 SKILL.md만
직접 고치거나 참조가 끊긴 entrypoint를 게시하지 않는다.

편입 후 기존 저장소의 validate·test·export·export:check를 수행하고 실제
사이트와 agent에서 사전의 상대 링크까지 읽히는지 확인한다. 코드·문서 원본과
생성물의 commit 분리는 기존 publish 규칙을 따른다. 사이트 등록을 위해 공개
저장소에 비공개 대화·업무 코드·credential 원문을 복제하지 않는다.
