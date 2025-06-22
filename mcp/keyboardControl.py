from mcp.server.fastmcp import FastMCP
from pynput import keyboard


mcp = FastMCP("keyboardControl")

nowkey=-1
def on_release(key):
    print(f'{key} 被释放')
    nowkey=key

def operation():
    if(nowkey==-1):
        return
    try:
        key=nowkey.char
    except:
        return
    nowkey=-1
    if(key=='w'):
        return {"name": "self.otto.walk_forward", "arguments": {}}
    if(key=='s'):
        return {"name": "self.otto.walk_forward", "arguments": {"dirction":"-1"}}
    if(key=='a'):
        return {"name": "self.otto.turn_left", "arguments": {}}
    if(key=='d'):
        return {"name": "self.otto.turn_left", "arguments": {"dirction":"-1"}}
    if(key=='j'):
        return {"name": "hands_down", "arguments": {"dirction":"1"}}
    if(key=='u'):
        return {"name": "hands_up", "arguments": {"dirction":"1"}}
    if(key=='l'):
        return {"name": "hands_down", "arguments": {"dirction":"-1"}}
    if(key=='o'):
        return {"name": "hands_up", "arguments": {"dirction":"-1"}}
with keyboard.Listener(on_release=on_release) as listener:
    listener.join()


@mcp.tool()
def keyboard_control(parameter: str) -> dict:
    """通过键盘控制小智的移动
        wasd分别前后左右 
        ju为左手上举放下 
        lo为右手上举放下"""
    
    logger.info(f"{nowkey}按下，执行指令")
    return operation()

if __name__ == "__main__":
    mcp.run(transport="stdio")