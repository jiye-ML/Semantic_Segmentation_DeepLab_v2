
with open("val2.txt", "r") as f:
    with open("val.txt", "w") as f2:
        for x in range(1449):
            now = f.readline().strip()
            result = "/JPEGImages/{}.jpg /SegmentationClass/{}.png".format(now, now)
            f2.write(result + "\n")
    pass
