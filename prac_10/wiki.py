import wikipedia

def main():
    """Prompt the user to enter Wikipedia page titles and display relevant information."""
    title = input("Enter page title: ")
    while title != "":
        try:
            page = wikipedia.page(title, auto_suggest=False)
            print(page.title)
            print(wikipedia.summary(title))
            print(page.url)
            print()

        # Handle disambiguation error and return message
        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
            print()

        # Handle PageError error and return message
        except wikipedia.exceptions.PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')
            print()

        except Exception as e:
            # Handle any other unexpected errors
            print(f"An unexpected error occurred: {str(e)}")
            print()

        title = input("Enter page title: ")

    print("Thank you")

if __name__ == '__main__':
    main()



