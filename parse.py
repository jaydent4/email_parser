def parse(input):
    emails = []
    try:
        with open(input, 'r') as infile:
            for line in infile:
                data_parts = line.split()
                if data_parts:
                    emails.append(data_parts[-1])
        with open("emails.txt", 'w') as outfile:
            for email in emails:
                outfile.write(email + "\n")

    except FileNotFoundError:
        print("'{input}' was not found")

if __name__ == "__main__":
    input_file = "input.txt"
    parse(input_file)
