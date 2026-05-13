with open("baseball.jpg", "rb") as file:
    image=file.read()

print(file.closed)
with open("baseball-copy.jpg", "wb") as file:
    file.write(image)

with open("sample.mp3", "rb") as file:
    sound=file.read()

print(file.closed)
with open("sample-copy.mp3", "wb") as file:
    file.write(sound*2)