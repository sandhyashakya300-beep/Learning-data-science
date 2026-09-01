#Title: YouTube Video Manager CLI
# A Python-based command-line interface (CLI) application for storing, 
# viewing, and managing a personal list of YouTube videos using JSON for data persistence.
import json

def load_data():
    try:
        with open('python_Project/youtube.txt', 'r') as file:
            test = json.load(file)
            #print(test)
            return test
    except FileNotFoundError:
        return []

def save_data(videos):
   with open('youtube.txt','w') as file:
      json.dump(videos,file)
      

def List_all_videos(videos):
    print("\n")
    print('*'*79)

    for index , video in enumerate(videos,start=1):
       print(f"{index}.{video['name']},Duration:{video['time']} ")

    print("\n")
    print('*'*79)

def add_video(videos):
    name = input("Enter the video name :")
    time = input("Enter the video time :")
    videos.append({'name': name , 'time':time})
    save_data(videos)

def update_video(videos):
    List_all_videos(videos)
    index = int(input("Enter the video number to update"))
    if 1 <= index <= len(videos):
       name = input("Enter the new video name :")
       time = input("Enter the new video time :")
       videos[index-1] = {'name': name , 'time':time}
       save_data(videos)
    else:
       print("Invalid index selected")


def delete_video(videos):
    List_all_videos(videos)
    index = int(input("Enter the video number to be deleted"))

    if 1 <= index <= len(videos):
       del videos[index-1]
       save_data(videos)

    else:
       print("Invalid index deleted")
         

def main():
   videos = load_data()
   while True:
       print("\n Youtube Manager | choose an option")
       print("1. List all youtube videos")
       print("2. Add a  youtube videos")
       print("3. Update a youtube videos details")
       print("4. Delete a  youtube videos")
       print("5.  Exit the app")

       choice = input("Enter your choice :")
       #print(videos)

       match choice:
           case "1":
              List_all_videos(videos)
           case "2":
              add_video(videos)
           case "3":
              update_video(videos)
           case "4":
              delete_video(videos)
           case "5":
              break
           case _:
              print("Invalid Choice")

if __name__ == "__main__":
   main()
     

