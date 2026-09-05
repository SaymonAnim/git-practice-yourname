from datetime import date
from utils import add, subtract
def main():
 print("Saymon Sorowar")
 print(f"Today's date: {date.today()}")

print(f"5 + 3 = {add(5, 3)}")
print(f"5 - 3 = {subtract(5, 3)}")
if __name__ == "__main__":
 main()