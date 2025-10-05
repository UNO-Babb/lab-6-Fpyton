#WordCount.py
#Name:
#Date:
#Assignment:

def main():
  textFile = open("gettysberg.txt", 'r')
  # textFile = open("fish.txt", 'r')
  lineCount = 0
  wordCount = 0
  letterCount = 0

  for line in textFile:
    lineCount = lineCount + 1
    words = line.split()
    for w in words:
      wordCount = wordCount + 1
      letterCount = letterCount + len(w)
    #print(line)

  print("Lines:", lineCount)
  print("words:", wordCount)
  print("character", letterCount)

if __name__ == '__main__':
  main()
