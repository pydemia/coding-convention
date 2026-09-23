---
name: pydemia-coding-style
description: >-
  Apply pydemia's coding conventions when creating, editing, or reviewing code
  in their style. Use scoped Python formatting and design preferences while
  preserving repository conventions.
---

# pydemia coding style

코드를 새로 작성하거나 수정·검토할 때 pydemia의 선택 기준을 적용한다.
서식 기본값과 프로젝트별 구조 결정을 구분한다.

## 적용 순서

현재 요청, 프로젝트 지침, 관련 코드·호출자·테스트·formatter 설정을
확인한다. [사전의 우선순위와 상태](references/dictionary.md)를 기준으로
변경 대상에 해당하는 규칙만 적용한다. 현재 명시적 요청이 우선하며 기존
formatter와 공개 API를 Skill 적용만으로 바꾸지 않는다.

- Python 작성·수정: [서식과 Python](references/python.md).
- 구조·비동기·의존성 변경: [구조와 상태](references/design.md).
- 문서·테스트·변경 범위 판단: [문서와 작업](references/workflow.md).
- Python 이외의 파일: [언어별 적용 범위](references/languages.md).
- 근거 또는 충돌 확인이 필요할 때만 [근거](references/evidence.md)와
  [결정 기록](references/decisions.md)을 읽는다.

개인 기본 서식은 79자, 공백 4칸, LF, UTF-8, 큰따옴표다. 여러 줄의
Python 인자·컨테이너에는 마지막 comma를 두고 닫는 괄호를 시작 구문의
들여쓰기에 맞춘다. 수직 chain은 수신 객체와 각 `.method()`를 나눈다.
formatter가 이 모양을 바꿀 수 있으므로 FMT-005의 예외를 함께 적용한다.

mixin·깊은 상속과 불필요한 간접 호출을 피하고 값과 실행 흐름을 추적할 수
있게 작성한다. 실제 확장 지점의 interface까지 없애지는 않는다. DTO의
검증에는 Pydantic을 우선 검토하되 모든 내부 값에 의존성을 추가하지 않는다.
오류·미확인·빈 값·실행 완료를 같은 값으로 합치지 않는다.

`관측`은 강제 규칙이 아니며 `조건부`는 해당 조건에서만 적용한다. 과거
assistant 제안을 사용자 확정으로 취급하지 않는다. 기존 파일 전체의
재서식, 별도 framework·도구 도입, 공개 이름 변경으로 범위를 넓히지 않는다.

변경한 동작에 맞는 검사를 실행한다. 규칙 충돌이 있었다면 적용한 기준과
이유, 실행한 검증과 미검증 범위를 결과에 남긴다. 이 Skill 자체는 commit,
push, 배포, 설치, 외부 메시지를 별도로 허가하지 않는다.
