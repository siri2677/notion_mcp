# mcp-server-notion

Notion과 연동되는 Model Context Protocol(MCP) 서버 툴입니다. 이 서버는 외부 시스템 또는 LLM 기반 에이전트가 Notion 데이터베이스에 자동으로 내용을 추가하거나, 다양한 노션 자동화 작업을 수행할 수 있도록 지원합니다.

## 주요 기능
- Notion 데이터베이스에 자동으로 콘텐츠 생성
- MCP 표준 프로토콜 기반의 툴 등록 및 호출
- Python 기반의 간단한 확장성

## 설치 방법

1. 패키지 설치 (PyPI 배포 후)
```bash
pip install mcp-server-notion
```

2. 의존성 설치 (개발 환경)
```bash
pip install -r requirements.txt
```

## 실행 방법

### uvx 또는 python -m 으로 실행
```bash
uvx mcp-server-notion
# 또는
python -m mcp_server_notion
```

### MCP 서버 등록 예시 (mcp.json)
```json
{
  "mcpServers": {
    "notion": {
      "command": "uvx",
      "args": ["mcp-server-notion"]
    }
  }
}
```

## 사용 예시

- 노션 API 토큰과 parent_id(페이지/데이터베이스 ID)를 준비합니다.
- MCP 툴 프롬프트 예시:

```
notion_create_page 툴을 사용해서 노션에 페이지를 만들어줘.
notion_token: [YOUR_NOTION_TOKEN]
parent_id: [YOUR_PAGE_OR_DATABASE_ID]
title: 예시 제목
content: 예시 내용
```