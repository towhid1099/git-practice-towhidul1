from datetime import date
import utils

print("Name: Md Towhidul Islam")
print(f"Date: {date.today()}")

print("10 + 5 =", utils.add(10, 5))
print("10 - 5 =", utils.subtract(10, 5))
print("10 / 5 =", utils.divide(10, 5))
print("10 / 0 =", utils.divide(10, 0))
