import decor
if __name__ == "__main__":
    @decor.repeat(6)
    def sum2(x, y):
        print(x + y)

    sum2(4, 5)