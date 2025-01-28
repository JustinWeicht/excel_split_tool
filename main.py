import math
import pandas as pd

def main(input_file, num_splits):
    input_file_name = input_file.split('.')[0]
    # Read the Excel file
    df = pd.read_excel(input_file)

    # Calculate the number of rows per split
    num_rows = len(df)
    rows_per_split = math.ceil(num_rows / num_splits)

    # Split the DataFrame and save to new Excel files
    for i in range(num_splits):
        start_row = i * rows_per_split
        end_row = start_row + rows_per_split
        split_df = df.iloc[start_row:end_row]

        # Save the split DataFrame to a new Excel file
        output_file = f'{input_file_name}_split_{i+1}.xlsx'
        split_df.to_excel(output_file, index=False)

if __name__ == "__main__":
    input_file = r'C:\Users\Justin\Documents\Programming\Projects\output_test\mifile_case_number\Redacted S&C Diary.xlsx'  # Replace with your input file path
    num_splits = 10  # Replace with the desired number of splits

    main(input_file, num_splits)