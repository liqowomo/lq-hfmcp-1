# Main entry point

from src.utilz import header1
from src.m1 import mcp


def main():
    # Call the header1 function from utilz.py
    header1("Welcome to the MCP Server")
    # Add more functionality here as needed

    # Start the MCP server
    print("\nStarting MCP server...")
    mcp.run()




if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nServer stopped by user")
    except Exception as e:
        print(f"\nError occurred: {e}")

