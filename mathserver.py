from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Math")

@mcp.tool()
def add(a:int,b:int)->int:
    """ Add two numbers together """
    return a+b

@mcp.tool()
def subtract(a:int,b:int)->int:
    """ Subtract two numbers """
    return a-b

@mcp.tool()
def multiply(a:int,b:int)->int:
    """ Multiply two numbers """
    return a*b


if __name__=="__main__":
    mcp.run(transport="stdio") # use standard input output to recieve and respond to tool function calls
