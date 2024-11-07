import os
from webexteamssdk import WebexTeamsAPI


api = WebexTeamsAPI(access_token="YzYwZjI0YjktMzJiMC00NWI5LWE1YzItNTkzZjZhNGI4ODZjMWE3YTFjMzYtNTg3_P0A1_60c4241b-f916-4111-96c4-b4c6eecaa22e")  


room_id = "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vMDBhYzhjOTAtOWNkNS0xMWVmLWFmZTItMWRhYjE3MTBlOGJk"  

def list_messages(room_id):
    print("\nListing messages in the room:")
    messages = api.messages.list(room_id)
    
    for message in messages:
        print(f"ID: {message.id}, Text: {message.text}")

    
    delete_message(room_id)

def delete_message(room_id):
    message_id = input("\nEnter the message ID you want to delete: ")
    
    try:
        api.messages.delete(messageId=message_id)
        print(f"Message {message_id} deleted successfully.")
    except Exception as e:
        print(f"Error deleting message {message_id}: {str(e)}")

if __name__ == "__main__":
    list_messages(room_id)