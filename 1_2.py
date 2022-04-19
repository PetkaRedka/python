time = int(input("Enter your time in seconds: "))

hours = time // 3600
seconds = time % 3600
minutes = seconds // 60
seconds %= 60

print(f"{hours:02}:{minutes:02}:{seconds:02}")
