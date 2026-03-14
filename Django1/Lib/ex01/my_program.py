from path import Path

def main():
    d = Path("test_directory")
    if not d.exists():
        d.mkdir()
    
    f = d / "hello.txt"

    f.write_text("Hello, this file was created using the path library!")

    print(f.read_text())

if __name__ == "__main__":
    main()