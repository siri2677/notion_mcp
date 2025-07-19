import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent
from pydantic import BaseModel
from notion_client import Client

class NotionCreatePageInput(BaseModel):
    notion_token: str
    parent_id: str
    title: str
    content: str

def create_notion_page(notion_token: str, parent_id: str, title: str, content: str) -> str:
    notion = Client(auth=notion_token)
    new_page = notion.pages.create(
        parent={"database_id": parent_id},
        properties={
            "title": [
                {
                    "type": "text",
                    "text": {"content": title}
                }
            ]
        },
        children=[
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {"content": content}
                        }
                    ]
                }
            }
        ]
    )
    return new_page['url']

async def serve() -> None:
    logger = logging.getLogger(__name__)
    server = Server("mcp-notion")

    @server.list_tools()
    async def list_tools():
        return [
            Tool(
                name="notion_create_page",
                description="Notion에 새 페이지를 생성",
                inputSchema=NotionCreatePageInput.schema(),
            ),
        ]

    @server.call_tool()
    async def call_tool(name: str, arguments: dict):
        if name == "notion_create_page":
            url = create_notion_page(
                arguments["notion_token"],
                arguments["parent_id"],
                arguments["title"],
                arguments["content"]
            )
            return [TextContent(type="text", text=f"페이지 생성됨: {url}")]
        raise ValueError(f"Unknown tool: {name}")

    options = server.create_initialization_options()
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, options, raise_exceptions=True)
