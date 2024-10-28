from dotenv import load_dotenv
import discogs_client
import os


def check_env():
    """
    WIP
    checks if the user has added their token to the .env
    """
    pass


def user_input(client: discogs_client.Client) -> discogs_client.Release:
    """
    This functions asks the users to select a release from discogs
    It searches their databse via the users input and outputs a selection for the use to select
    The usere selects using the top 5 results
    """
    user_search_query = input("Enter in the name of the album: ")

    serach_results = client.search(user_search_query, type="release")

    print("\nDisplaying top 5 results for your search:")

    for i in range(5):
        print(f"{i+1}. {serach_results.page(1)[i].title}")

    while True:
        try:
            user_selection = eval(input("\nEnter the number of the release you want: "))

            while user_selection < 1 or user_selection > 5:
                print("please input within the range 1-5")
                user_selection = eval(
                    input("\nEnter the number of the release you want: ")
                )

            break

        except Exception as e:
            print(e)
            print("invalid input, please input a number")

    return serach_results.page(1)[user_selection - 1]


def print_to_format(user_release: discogs_client.Release) -> None:
    """
    Takes the users input and prints the selected release in this desired format
    """
    print("\n==========================================")
    print("\nDescription:")
    print(f"\nReleased - {user_release.year}")
    print(f"\nLabel - {user_release.labels[0].name}\n")
    for i, track in enumerate(user_release.tracklist):
        print(f"{i+1}. {track.title}")


def main():
    """
    Main Functions
    """

    # check_env()

    user_release = user_input(client)

    print_to_format(user_release)

    """
    Prompts the user if they want to use the program again
    """
    rerun_program = input("\nDo you want to rerun program [y/n]: ")

    while rerun_program.lower() != "y" and rerun_program.lower() != "n":
        rerun_program = input(
            "\nInccorect Input!\nDo you want to rerun program [y/n]: "
        )

    if rerun_program.lower() == "y":
        main()
    else:
        pass


"""
Loads the token from .env
Creates the API client before running main
"""
load_dotenv()
TOKEN = os.environ["TOKEN"]
client = discogs_client.Client("TestApp", user_token=TOKEN)

main()
