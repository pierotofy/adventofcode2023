input = open("input.txt", "r", encoding="utf-8").read()
lines = [l.strip() for l in input.split("\n") if l.strip() != ""]
s = 0
m = {
    'one': '1',
    'two': '2',
    'six': '6',
    'four': '4',
    'five': '5',
    'nine': '9',
    'three': '3',
    'seven': '7',
    'eight': '8',
}
d = m.keys()

for l in lines:
    first = ""
    second = ""

    for c in range(len(l)):
        if not first:    
            for k,v in m.items():
                if c >= len(k):
                    if l[c-len(k):c] == k:
                        first = v
                        break
        if not first:
            if l[c].isdigit():
                first = l[c]

        if not second:
            for k,v in m.items():
                if c >= len(k):
                    if l[-c:][:len(k)] == k:
                        second = v
                        break
        if not second:
            if l[-c - 1].isdigit():
                second = l[-c - 1]
        
    digits = first + second 
    
    if len(digits) == 1:
        digits *= 2

    count = float(digits[0] + digits[-1])
    s += count
print(s)