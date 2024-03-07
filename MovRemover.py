import os


def remove_mov(folder_path):
    try:
        # verify the folder_path
        if not os.path.isdir(folder_path):
            print("Eroare: Calea specificată nu este un director valid.")
            return

        # iterate trhough all the files from the directory
        for filename in os.listdir(folder_path):
            filepath = os.path.join(folder_path, filename)
            # verify if the folder has the .mov extension
            if filename.endswith(".MOV"):
                # delete the file
                os.remove(filepath)
                print(f"Fișierul {filename} a fost șters.")

        print("Ștergerea fișierelor .mov a fost finalizată.")
    except Exception as e:
        print(f"A intervenit o eroare: {str(e)}")


if __name__ == "__main__":
    folder_path = input("Introduceți calea către directorul dorit: ")
    remove_mov(folder_path)
