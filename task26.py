class Addition:

    def __call__(self, *args, **kwargs):
        s = 0
        for arg in args:
            if isinstance(arg, (int, float)):
                s += arg
        print(f'Сумма переданих чисел {s}')


add = Addition()
add(10, 20)
add(1, 2, 3.4)
add(1, 2, 'hello', [1, 2], 3)


