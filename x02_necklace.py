#!python3

""" 
Necklace numbers are a number sequence.  You start with 2 digits. The 3rd digit is created by adding the previous 2 digits, but if it's greater than 10, you add the sum of those 2 digits again.  You keep repeating this process until you get back to the 2 digits you started with

extra: What is the shortest necklace number sequence that can be made?
"""

def necklace(a, b):
    s = ""
    s += str(a)
    s += str(b)
    u = True
    while u:
        c = a + b
        if c < 10:
            s += str(c)
        elif c >= 10:
            s += str(int(str(c)[0]) + int(str(c)[1]))
            if s[0] == s[-2] and s[1] == s[-1]:
                return s
        a, b = int(s[-2]), int(s[-1])

def main():
  assert necklace(9,4) == "94483257314595516742685494"
  assert necklace(1,3) == "13472922461786527977538213"
  assert necklace(5,1) == "51674268549448325731459551"
  assert necklace(3,4) == "34729224617865279775382134"

if __name__ == "__main__":
  main()
  
  
