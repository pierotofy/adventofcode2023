input = open("input.txt", "r", encoding="utf-8").read()
lines = [l.strip() for l in input.split("\n") if l.strip() != ""]
s = 0
for l in lines:
    digits = "".join(list(filter(lambda c: c.isdigit(), l)))
    if len(digits) == 1:
        digits *= 2
    s += float(digits[0] + digits[-1])
print(s)