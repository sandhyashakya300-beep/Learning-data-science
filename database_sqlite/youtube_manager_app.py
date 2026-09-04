import sqlite3

conn = sqlite3.connect('database_sqlite/youtube_videos.db')

cursor = conn.cursor()
cursor.execute(''' 
CREATE TABLE IF NOT EXISTS videos(
         id INTEGER PRIMARY KEY,
         name TEXT NOT NULL,
         time TEXT NOT NULL

)
''')

def list_videos():
    print("\n")
    print('*'*79)
    cursor.execute("SELECT * from videos")
    for row in cursor.fetchall():
        print(row)
    print("\n")
    print('*'*79)

def add_video(name,time):
    cursor.execute("INSERT INTO videos(name,time) VALUES(?,?)",(name,time))
    conn.commit()

def update_video(video_id,new_name,new_time):
     cursor.execute("UPDATE videos SET name=?,time=? WHERE id=?",(new_name,new_time,video_id))
     conn.commit()

def delete_video(video_id):
      cursor.execute("DELETE FROM videos WHERE id=?",(video_id,))
      conn.commit()
   
def main():
   global conn
   while True:
       print("\n Youtube Manager App with DB")
       print("1. List all youtube videos")
       print("2. Add a  youtube videos")
       print("3. Update a youtube videos details")
       print("4. Delete a  youtube videos")
       print("5.  Exit the app")

       choice = input("Enter your choice :")
       #print(videos)

       if choice == '1':
          list_videos()

       elif choice == '2':
            name = input("Enter the video name :")
            time = input("Enter the video time :")
            add_video(name,time)
       elif choice == '3':
                  video_id = input("Enter the video id to update : ")
                  name = input("Enter the video name :")
                  time = input("Enter the video time :")
                  update_video(video_id ,name,time)
       elif choice == '4':
                        video_id = input("Enter the video id to deleted : ")
                        delete_video(video_id )
       elif choice == '5':
            break
       else:
            print("Invalid Choice ")
    
   conn.close()  

if __name__ == "__main__":
    main()

         

