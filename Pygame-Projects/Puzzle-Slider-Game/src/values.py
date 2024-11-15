def give_values(num):

    match num:
        case 3:
            WIDTH = HEIGHT = 60
            LIST = [[1, 2, 3], [4, 5, 6], [7, 8, None]]
            FINAL = [1, 2, 3, 4, 5, 6, 7, 8, None]

        case 4:
            WIDTH = HEIGHT = 60
            LIST = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, None]]
            FINAL = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None]

        case 5:
            WIDTH = HEIGHT = 40
            LIST = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, None]]
            FINAL = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, None]

        case 6:
            WIDTH = HEIGHT = 30
            LIST = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, None]]
            FINAL = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, None]

    return WIDTH, HEIGHT, LIST, FINAL

