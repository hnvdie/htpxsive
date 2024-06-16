import os
import sys

def run_httpx(input_file):
    cmd = f"""cat {input_file} | sort | uniq | httpx -debug-resp -mr 'href="([^"/]+)/"' -er 'href="([^"/]+)/"' | sed 's/href="//g; s/"//g' > extract.txt"""
    os.system(cmd)

def process_extracted():
    with open('extract.txt', 'r') as file:
        lines = file.readlines()

    if not lines:
        print("No output from httpx.")
        return False

    with open('hostsDepth.txt', 'w') as output_file:
        for line in lines:
            try:
                url_part, dirs_part = line.split(' [')
                url_part = url_part.strip()
                dirs_part = dirs_part.strip(']\n')
                output_file.write(f"{url_part}\n")

                dirs = dirs_part.split(',')
                for dir in dirs:
                    output_file.write(f"{url_part}/{dir}\n")
            except ValueError:
                # Handle cases where line does not split correctly
                print(f"Skipping line: {line.strip()}")
                continue

    os.remove('extract.txt')
    return True

def recursive_scan(input_file, depth):
    temp_input = input_file
    for i in range(1, depth + 1):
        print(f"Running iteration {i}")
        run_httpx(temp_input)
        success = process_extracted()
        if not success:
            print("Stopping recursion due to empty output.")
            break
        temp_input = f"hostsDepth{i}.txt"
        os.rename('hostsDepth.txt', temp_input)

    with open('result.txt', 'w') as result_file:
        for i in range(1, depth + 1):
            temp_input = f"hostsDepth{i}.txt"
            if os.path.exists(temp_input):
                with open(temp_input, 'r') as temp_file:
                    result_file.write(temp_file.read())
                os.remove(temp_input)

if __name__ == "__main__":
    try:
        raw_host = sys.argv[1]
        depth = int(sys.argv[2].split('=')[1])
    except Exception as e:
        sys.exit('Usage: python htpxsive.py [input_file] -r=[depth]')

    if depth < 1:
        run_httpx(raw_host)
        process_extracted()
    else:
        recursive_scan(raw_host, depth)
