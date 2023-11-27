from read_fasta import read_fasta
from RCAlg import Rabin_Carp_Alg


def main():
    print("Введите путь к fasta файлу с Вашими данными")
    path = input()

    print("Какую подпоследовательность Вы хотите найти?")
    targ = input()

    name, data = read_fasta(path)
    try:
        results = Rabin_Carp_Alg(data, targ)
    except ValueError:
        print("Your date contains mistakes")
        return
    except TypeError:
        print("Incorrect data format ")
        return

    output = open("output.txt", "w")
    if results:
        output.write(results)
        print("Congratulations!:) Your subsequence was found on positions: \n\n")
        print(results)
    else:
        output.write("")
        print("Nothing was found :(")
    output.close()


if __name__ == "__main__":
    main()


