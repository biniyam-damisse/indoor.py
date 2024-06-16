def main():
    face = input()
    print(convert(face))

def convert(face):
    face = face.replace(":)", "happy")
    face = face.replace(":(", "sad") 
    return face 

main() 