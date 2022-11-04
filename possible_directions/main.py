import src.solving as solve

if __name__ == "__main__":
    print('Please, edit file "src/parameters.py according to your problem" and restart the program')
    print()
    try:
        solution = solve.main_algorithm()
    except:
        print('An error occured, check or change parameters')
    else:
        print('The solution according to eps accuracy is:', solution[0], '\nFunciton value is:', solution[1])
