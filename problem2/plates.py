def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("valid")
    else:
        print("invalid")

def is_valid(s):
  if len(s) < 2 or len(s) > 7:
      return False
  if s[0].isalpha() == False or s[1].isalpha() == False:
      return False
  i = 0
  while i < len(s):
      if s[i].isalpha() == False:
          if s[i] == "0":
              return False
          else:
              break
      i += 1
  for n in s:
      if n in [".", " ", "|", "?"]:
          return False
  return True

main()
    