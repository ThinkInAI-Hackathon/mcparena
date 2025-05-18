from fastmcp import FastMCP
import os
mcp = FastMCP("My MCP Book Server")

#temp_zuoye ="今天的作业是：老师还没发\n"
temp_chats={}
@mcp.tool()
def save_chat(name: str , content: str) -> str:
    """保存name的答辩
    Args:
        name (str): 人名
        content (str): 发言内容
    """  
    global temp_chats
    temp_chats[name] = content
    return "收到你的答辩"
@mcp.tool()
def get_chat(name:str) -> str:
    """获取某人的发言.

    Args:
        name (str): 人名
    """  
    global temp_chat
    print("temp_chats=", temp_chats)
    print("name=", name)
    if name not in temp_chats:
        return f"没有找到{name}的答辩记录"
    return  f"{name}的答辩是：" + str(temp_chats[name])
@mcp.tool()
def chatplayers() -> str:
    """获取竞技场的人员名.

    Args:
        name (str): 人名列表
    """  
    global temp_chat
    print("temp_chats=", temp_chats)
    names = list(temp_chats.keys())
    names_str = str(names)
    return  f"当前的竞技场上的大咖：" + names_str
if __name__ == "__main__":
  mcp.run(
        transport="sse",
        host="0.0.0.0",
        port=8003,
        path="/sse",
        log_level="debug",
    )
