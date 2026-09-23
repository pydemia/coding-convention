# skills.pydemia.ai 게시

2026-09-23에 `pydemia-coding-style` Skill과 13개 참조 문서를 게시했다.

- [Skill 페이지](https://skills.pydemia.ai/skills/pydemia-coding-style)
- [71개 규칙 전체 목록](https://skills.pydemia.ai/skills/pydemia-coding-style/references/dictionary.md)

## 게시 원본과 생성물

사이트의 편집 원본은 `pydemia/agent-skills` 저장소의
`library/references/pydemia-coding-style/skill.md`와 `references/`다.
이 저장소의 `c91059cc34579dde845a3d6dc21c7f219787f5a8` revision에서
Skill 본문과 규칙을 가져왔고 사이트 schema의 frontmatter를 추가했다.

`export.config.json`에 active Skill과 참조 문서를 등록했다. 같은 원본에서
`skills/pydemia-coding-style/`와 Codex 호환용
`exports/codex/skills/pydemia-coding-style/`를 생성한다.
기존 software-engineering 지침에도 사이트의 Skill 링크를 연결했다.

사이트에 게시할 후속 수정은 agent-skills의 원본에서 관리한다. 이 저장소의
조사 기록과 사전을 갱신해 가져갈 때는 해당 원본과 diff를 확인한다.
두 저장소 사이에 자동 동기화는 설정하지 않았다. 생성물만 직접 수정하거나
서로 다른 정책을 두 곳에서 독립적으로 유지하지 않는다.

## 확인한 범위

사이트는 배포 manifest에 등록된 Markdown 참조 문서만 제공한다. 파일의
SHA-256을 확인한 뒤 렌더링하며 규칙 anchor와 상대 링크를 보존한다.
71개 목록 링크의 도착 항목, 참조 문서 13개의 응답과 본문을 확인했다.
미등록 참조 파일은 404로 응답한다.

로컬 임시 경로에 Skill을 설치해 본문과 참조 파일의 일치를 검증했다.
사용자의 전역 Skill 설치나 ChatGPT 설정은 변경하지 않았다. 실제 agent가
모든 개발 상황에서 규칙을 적용하는지에 대한 행동 검증은 별도 범위다.
