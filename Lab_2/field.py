def field(items: list[dict], *args: list): return [dict([[arg, elem[arg]] for arg in args]) for elem in items]


if __name__ == "__main__":
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}]
    print(field(goods, 'title'))
    print(field(goods, 'title', 'price'))
