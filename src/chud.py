import sys

def run(source):
    print(source)
    print("Scanner Not Implemented Yet")

def run_file(filename):
    with open(filename, 'r') as f:
        source = f.read()

    run(source)

def run_the_repl():
    print("----CHUD Interactive Shell----")
    try:
        while True:
            source = input("> ")
            run(source)
    except KeyboardInterrupt:
        print()

def main():
    if len(sys.argv) > 2:
        print("Correct Usage: python src/chud.py [script]")
    elif len(sys.argv) == 2:
        run_file(sys.argv[1])
    else:
        run_the_repl()

main()