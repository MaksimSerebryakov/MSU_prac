import func
import plots

def main():
    data = func.read_data()
    func.total_sword_number(data)

    total_sword_plot = plots.my_plot('Total swords and defects')

if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
        print(ex)
    else:
        print('\nSUCCESS\n')