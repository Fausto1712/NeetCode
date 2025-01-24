from typing import List

def main():
    listA = [0,1,2,3,4]
    listB = ["A","B","C","D","E"]
    listC = []

    for i in range(len(listA)):
        listC.append((listA[i], listB[i]))
        print(f"El valor {listA[i]} corresponde a la letra {listB[i]}")
    print(listC)


if __name__ == "__main__":
    print("Hola papucho")
    main()