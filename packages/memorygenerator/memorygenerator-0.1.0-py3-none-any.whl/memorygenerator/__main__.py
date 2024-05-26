# memorygenerator/__main__.py
import sys
from memorygenerator.generator import generate_memory

def main():
    if len(sys.argv) != 2:
        print("Usage: memory-generator <theme>")
        print("Available themes: childhood, adventure, dream")
        sys.exit(1)
    
    theme = sys.argv[1]
    try:
        memory = generate_memory(theme)
        print(f"Here's a memory for you: {memory}")
    except ValueError as e:
        print(e)
        sys.exit(1)

if __name__ == '__main__':
    main()
