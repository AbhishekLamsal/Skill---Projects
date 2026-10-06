# Turn seconds into hours, minutes and seconds with divmod(). The function returns 3 values, so unpack them like Day 05.
# Your job:
# 1. ask the user for seconds with int(input())
# 2. write to_seconds(h, m, s) that goes the other way

def convert(seconds):
    minutes, secs = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return hours, minutes, secs

def to_seconds(h, m, s):
    return h * 3600 + m * 60 + s

seconds = int(input("Enter seconds: "))

h, m, s = convert(seconds)

print(f"{h} h {m} m {s} s")

print(f"Back to seconds: {to_seconds(h, m, s)}")