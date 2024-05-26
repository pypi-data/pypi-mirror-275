# clipy_chat/cli.py

import sys
from clipy_chat.client import main as start_client

def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'suru':
        start_client()
    else:
        print("Usage: clipy-chat suru")

if __name__ == "__main__":
    main()
