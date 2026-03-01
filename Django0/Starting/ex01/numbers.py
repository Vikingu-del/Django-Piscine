def process_file(filename: str) -> None:
    with open(filename) as f:
        for n in f.readline().split(","):
            print(n)

def main():
    process_file("numbers.txt")


if __name__ == "__main__":
    main()