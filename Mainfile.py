import multiprocessing


def Python_File1():
    import add_members

def Python_File2():
    import add_members2

def Python_File3():
    import add_members3


if __name__ == "__main__":
    P1 = multiprocessing.Process(target=Python_File1)
    P2 = multiprocessing.Process(target=Python_File2)
    P3 = multiprocessing.Process(target=Python_File3)

    P1.start()

    P2.start()

    P3.start()



    P1.join()
    P2.join()
    P3.join()

