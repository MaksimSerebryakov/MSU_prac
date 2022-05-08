import src.func as func
import src.plots as plots

def main():
    data = func.read_data()

    func.make_plot_sum(data)
    func.defects_monthly(data)
    func.life_time(data)

if __name__ == '__main__':
    # try:
    #     main()
    # except Exception as ex:
    #     print(ex)
    # else:
    #     print('\nSUCCESS\n')
    main()