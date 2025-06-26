import argparse
import os
import shutil

parser = argparse.ArgumentParser(description = "create a backup file")
parser.add_argument("filename", help ="name of the file to create")
parser.add_argument("content", help ="content to write in the file")

args = parser.parse_args()

with open(args.filename, "w") as f:
    f.write(args.content)

print(f"✅ File '{args.filename}' created with content.")

backup_dir = "backup"
os.makedirs(backup_dir, exist_ok=True)

# Step 3: Copy file to backup directory
backup_path = os.path.join(backup_dir, args.filename)
shutil.copy(args.filename, backup_path)
print(f"📁 File backed up to '{backup_path}'")