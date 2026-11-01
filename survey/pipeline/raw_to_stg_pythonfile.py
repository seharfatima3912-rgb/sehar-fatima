# Install this package once in the environment if needed:
# pip install pandas

import pandas as pd  # Import pandas so the public Google Sheet can be loaded into a DataFrame.

from pathlib import Path  # Import Path to reference the project folders without creating new ones.
import shutil  # Import shutil so we can move failed files.


# Public Google Sheet URL: replace this with your actual public sheet link.
url = "https://docs.google.com/spreadsheets/d/1OzDHmE7ts9aI2fmqPUTJYUCLTCGTtHuQBYF2tquoRrg/export?format=csv"

# Read the public Google Sheet directly into a pandas DataFrame.
df = pd.read_csv(url)  # This fetches the sheet as CSV data and stores it in the variable df.

raw_folder = Path("D:/survey/raw")  # Use the existing raw folder in the project root.
error_folder = Path("D:/survey/error")  # Use the existing error folder in the project root.
output_file = raw_folder / "df_export.csv"  # Name the CSV file that will be created from the DataFrame.

# Replace these with the exact custom column names you want in the exported CSV.
custom_columns = ["timstamp", "python_skill", "career", "future_goal", "python_topics", "interests", "learning_style", "expectations", "pace", "difficulty", "balance"]

# If the DataFrame has a different number of columns, this will raise an error so you can fix it.
if len(df.columns) != len(custom_columns):
    raise ValueError(f"Expected {len(custom_columns)} columns but DataFrame has {len(df.columns)} columns.")
print("Hello World")

print("hamza")
# Apply the custom names to the DataFrame before writing.
df.columns = custom_columns

try:  # Protect the save step so an error can trigger a fallback.
    df.to_csv(output_file, index=False)  # Write the DataFrame to the CSV file without the index.
    print(f"Saved DataFrame to: {output_file}")  # Print a success message with the full file path.

except Exception as e:  # Catch any problem during the save step.
    if output_file.exists():  # Only move the file if it was created before the failure.
        moved_file = error_folder / output_file.name  # Build the destination path in the error folder.
        shutil.move(str(output_file), str(moved_file))  # Move the saved file into the error folder.
        print(f"Error detected. File moved to: {moved_file}")  # Tell the user where the failed CSV went.
    print(f"Failed to save DataFrame: {e}")  # Print the actual error for debugging.
    raise  # Re-raise the exception so the notebook shows the failure clearly.