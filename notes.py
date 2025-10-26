from datetime import datetime
import os

def main():
    main_folder_name = "notes"

    if not os.path.exists(main_folder_name):
        os.makedirs(main_folder_name)
        print(f"Folder {main_folder_name} created")

    today = datetime.now()
    month_folder = today.strftime("%Y %B")
    filename = today.strftime("%d-%m-%Y.txt")

    month_path = os.path.join(main_folder_name, month_folder)
    os.makedirs(month_path, exist_ok=True)

    file_path = os.path.join(month_path, filename)
    with open(file_path, "w") as f:
        f.write("Notes for {today.strftime('%d-%m-%Y')}")

    print(f"Note saved to {file_path}")


if __name__ == "__main__":
    main()
    