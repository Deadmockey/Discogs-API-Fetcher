from dotenv import load_dotenv
import discogs_client
import os


def user_input(client: discogs_client.Client):
    user_search_query = input("Enter in the name of the album: ")

    serach_results = client.search(user_search_query)
    
    print("\nDisplaying top 5 results for your search:")

    for i in range(5):
        print(serach_results.page(1)[i].title)

    user_selection = input("Enter the number of release")

def main():
    load_dotenv()
    TOKEN = os.environ["TOKEN"]
    client = discogs_client.Client("TestApp", user_token=TOKEN)

    user_search = user_input(client)


main()
