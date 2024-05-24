import sys
from .summary import get_weather

def main():
    if len(sys.argv) != 2:
        print("Usage: simpleweather <city>")
        sys.exit(1)
    
    city = sys.argv[1]
    get_weather(city)
