# import module for csv
import csv
# import module for sys functions
import sys

# declare filename constant
FILENAME = "movies_test.csv"

# define exit function
def exit_program():
    # display exit message
    print("Terminating program.")
    # exit program
    sys.exit()

# define read movies function
def read_movies():
    # exception handling
    try:
        # create list for movies
        movies = []
        # open file
        with open(FILENAME, newline="") as file:
            # create reader object
            reader = csv.reader(file)
            # loop through rows 
            for row in reader:
                # append to movies list
                movies.append(row)
        # return movies
        return movies
    # file not found error
    except FileNotFoundError as e:
        # print error if file not found
        #print(f"Could not find {FILENAME} file.")
        # call exit program function
        #exit_program()
        return movies
    # catch other exceptions
    except Exception as e:
        # display the exception type to user
        print(type(e), e)
        # call exit function
        exit_program()

# define write movies function
def write_movies(movies):
    # start exception handling
    try:
        ## test raise OSerror
        #raise BlockingIOError("test the OSerror exception")
        # try to open file to write
        with open(FILENAME, "w", newline="") as file:
            # create writer object
            writer = csv.writer(file)
            # write rows to movies
            writer.writerows(movies)
    # catch OS errors
    except OSError as e:
        # print exception message
        print(type(e), e)
        # call exit function
        exit_program()
    # catch generic exceptions
    except Exception as e:
        # print exception message to user
        print(type(e), e)
        # call exit function
        exit_program()

# define list movies function
def list_movies(movies):
    # loops through movies
    for i, movie in enumerate(movies, start=1):
        # display movie list contents
        print(f"{i}. {movie[0]} ({movie[1]})")
    # blank line
    print()

# define add movies function    
def add_movie(movies):
    # assigns name variable
    name = input("Name: ")
    # while loop
    while True:
        # start exception handling
        try:
            # assigns year variable and checks if int
            year = int(input("Year: "))
        # if not int raise value error exception
        except ValueError:
            # print error message
            print("Year must be an integer. Try again.")
            # continue
            continue
        # checks of year is too low
        if year <= 0:
            # print error message if so
            print("Year must be greater than 0. Try again.")
            # continue
            continue
        # else break
        else:
            break
    # assigns variables to movie list
    movie = [name, year]
    # appends to the list
    movies.append(movie)
    # write to the file
    write_movies(movies)
    # confirmation message
    print(f"{name} was added.\n")

# define delete movies function
def delete_movie(movies):
    # while loop to ask user for what movies to delete
    while True:
        # check if number is an integer
        try:
            number = int(input("Number: "))
        # if not, raise value error exception
        except ValueError:
            # display error message
            print("Invalid integer. Please try again.")
            # continue to prevent crash
            continue
        # check to see if number given is outside range
        if number < 1 or number > len(movies):
            # error message if so
            print("There is no movie with that number. Please try again.")
        # else break
        else:
            break
    # remove movie selected from list
    movie = movies.pop(number - 1)
    # write to file
    write_movies(movies)
    # confirmation message
    print(f"{movie[0]} was deleted.\n")

# define menu function
def display_menu():
    # program name
    print("The Movie List program")
    # blank line
    print()
    # menu name
    print("COMMAND MENU")
    # list option
    print("list - List all movies")
    # add options
    print("add -  Add a movie")
    # delete option
    print("del -  Delete a movie")
    # exit option
    print("exit - Exit program")
    # blank line
    print()    

# define main function
def main():
    # call menu function
    display_menu()
    # call read movies function and assign to movies list
    movies = read_movies()
    # loop to accept commands
    while True:
        # prompt for command        
        command = input("Command: ")
        # if list command call list function
        if command.lower() == "list":
            list_movies(movies)
        # if add command, call add function
        elif command.lower() == "add":
            add_movie(movies)
        # if del command call delete function
        elif command.lower() == "del":
            delete_movie(movies)
        # if exit command, exit loops
        elif command.lower() == "exit":
            break
        # if invalid command display error message
        else:
            print("Not a valid command. Please try again.\n")
    # exit message
    print("Bye!")

# if run as main module call main
if __name__ == "__main__":
    main()
