from fastmcp import FastMCP
import os
mcp = FastMCP("My MCP Book Server")

temp_zuoye ="今天的作业是：老师还没发\n"
@mcp.tool()
def save_zuoye(content: str) -> str:
    """保存今天的作业.

    Args:
        name (str): 作业内容
    """  
    global temp_zuoye
    temp_zuoye = content
    return "收到作业了，谢谢！"
@mcp.tool()
def get_zuoye() -> str:
    """获取今天的作业.

    Args:
        name (str): 作业内容
    """  
    global temp_zuoye
    print("temp_zuoye=", temp_zuoye)
    return  "今天的作业是：" + temp_zuoye

@mcp.tool()
def get_page(name: str,page: int ) -> str:
    """Get 书的第几页.

    Args:
        name (str): 书名,六年级英语，六年级数学，六年级语文
        page (int): 页码
    """  
    try:
        # 处理name参数：替换空格为下划线并转为小写
        processed_name = name.replace(' ', '_').lower()
        print("processed_name=", processed_name)
        original_page = int(page)
        calculated_page = original_page 
        
        if calculated_page < 0:
            raise ValueError("页码不能小于0")

        # 使用处理后的名称构建路径
        data_path = os.getenv("DATA_PATH", "/Users/huazhuang/Documents/data2025")
        filename = f"/home/ubuntu/data2025/{processed_name}/txt/image{calculated_page:05d}.txt"
        filename = f"{data_path}/{processed_name}/txt/image{calculated_page:05d}.txt"
        
        print(f"filename={filename}")
        
        if not os.path.exists(filename):
            print("file no exists")
            raise FileNotFoundError(f"文件 {filename} 不存在")

        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()

        return content

    except ValueError as ve:
        error_msg = f"参数错误: {str(ve)}"
    except FileNotFoundError as fe:
        error_msg = f"文件错误: {str(fe)}"
    except Exception as e:
        error_msg = f"系统错误: {str(e)}"



if __name__ == "__main__":
  mcp.run(
        transport="sse",
        host="127.0.0.1",
        port=8002,
        path="/sse",
        log_level="debug",
    )
