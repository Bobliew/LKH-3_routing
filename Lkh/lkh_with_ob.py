

def perform():
    with open('../File/outputFile/tourFile/lkh_output0.txt', 'r') as f:
        content = f.read()
    lines = content.splitlines()
    index = lines.index("TOUR_SECTION")
    section = lines[index+1:-1]
    section = [int(x) for x in section if x != "-1"]
    print(section)
    return 0

def main():
    perform()

if __name__ == '__main__':
    main()
