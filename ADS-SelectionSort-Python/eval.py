import subprocess
import os
import threading

# Function to execute the program
def execute(file, input_file):
    ext = file.split('.')[-1]
    base = os.path.splitext(file)[0]

    try:
        # Read input file content
        with open(input_file, 'r') as f:
            input_data = f.read()

        if ext == "java":
            subprocess.run(["javac", "*.java"], check=True)  # Compiling the Java code
            result = subprocess.run(["java", base], input=input_data, capture_output=True, text=True)
        elif ext == "c":
            subprocess.run(["gcc", "-o", base, file], check=True)  # Compiling C code
            result = subprocess.run([f"./{base}"], input=input_data, capture_output=True, text=True)
        elif ext == "py":
            result = subprocess.run(["python3", file], input=input_data, capture_output=True, text=True)
        else:
            raise ValueError("Unsupported file extension")
        
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return e.stderr.strip()

# Function to run tests
def run_tests(file):
    inputs = sorted([f for f in os.listdir() if f.startswith('input') and f.endswith('.txt')])
    outputs = sorted([f for f in os.listdir() if f.startswith('output') and f.endswith('.txt')])

    total = len(inputs)
    threads = []

    def test_case(i):
        # Execute the program with the input file
        your_output = execute(file, inputs[i])
        expected_output = open(outputs[i]).read().strip()
        
        # Compare the outputs and print "Pass" or "Fail"
        if your_output == expected_output:
            print(f"Testcase {i+1} Passed")
        else:
            print(f"Testcase {i+1} Failed")

    # Create threads for parallel execution of test cases
    for i in range(total):
        thread = threading.Thread(target=test_case, args=(i,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish by calling join
    for thread in threads:
        thread.join()

# Main script logic
if __name__ == "__main__":
    import sys

    if len(sys.argv) == 2:
        file = sys.argv[1]
        if os.path.isfile(file):
            run_tests(file)
        else:
            print(f"File not found: {file}")
            sys.exit(1)
    else:
        print("Usage: python3 script.py <filename>")
        sys.exit(1)
