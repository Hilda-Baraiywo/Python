import os

def process_file():
    input_file = input("Enter the name of the file to read: ")

    # Check file extension
    if not input_file.lower().endswith('.txt'):
        print("❌ Error: Only text files (.txt) are supported.")
        return

    try:
        # Read the file with explicit encoding
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Modify content: Add line numbers and convert text to uppercase
        modified_lines = [f"{i+1}: {line.upper()}" for i, line in enumerate(lines)]

        # Ask user for the output filename
        output_file = input("Enter the name for the new file: ")

        # Write modified content to the new file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.writelines(modified_lines)

        print(f"\n✅ Success! Modified content written to '{output_file}'")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_file}' does not exist.")
    except PermissionError:
        print(f"❌ Error: You do not have permission to read or write the file.")
    except UnicodeDecodeError:
        print(f"❌ Error: Cannot decode '{input_file}'. Make sure it's a plain text file.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


# Run the program
process_file()
