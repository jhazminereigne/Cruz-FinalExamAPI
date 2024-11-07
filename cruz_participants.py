import os
from webexteamssdk import WebexTeamsAPI


api = WebexTeamsAPI(access_token="YzYwZjI0YjktMzJiMC00NWI5LWE1YzItNTkzZjZhNGI4ODZjMWE3YTFjMzYtNTg3_P0A1_60c4241b-f916-4111-96c4-b4c6eecaa22e") 

def create_room_and_send_message():

    room_name = input("Enter the room name: ")
    message = input("Enter the welcome message: ")

    
    room = api.rooms.create(room_name)

    
    api.messages.create(room.id, text=message)

    
    print(f"Room created: {room.title}")
    print(f"Message sent: {message}")

 
    participant_emails = input("Enter the participant emails (comma-separated): ").split(",")
    
    
    add_participants(room.id, participant_emails)

def add_participants(room_id, participant_emails):
    for email in participant_emails:
        email = email.strip()  # Remove any leading/trailing whitespace
        try:
            api.memberships.create(roomId=room_id, personEmail=email)
            print(f"Added {email} to the room.")
        except Exception as e:
            print(f"Error adding {email}: {str(e)}")

if __name__ == "__main__":
    create_room_and_send_message()