import csv

# Open the input CSV file
with open('shooting_stats.csv', newline='', encoding='utf-8') as input_file:

    # Create a CSV reader object
    reader = csv.reader(input_file)

    # Create a list to hold the tokenized rows
    rows = []

    # Loop through the rows in the CSV file
    for row in reader:

        # Replace empty values with 0
        cleaned_row = [value if value else '0' for value in row]

        # Add the cleaned row to the list of tokenized rows
        rows.append(cleaned_row)

# Open the output CSV file
with open('shooting_stats_cleaned.csv', 'w+', newline='', encoding='utf-8') as output_file:

    # Create a CSV writer object
    writer = csv.writer(output_file)

    # Write the cleaned rows to the output CSV file
    writer.writerows(rows)

