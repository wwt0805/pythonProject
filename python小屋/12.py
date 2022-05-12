def main(lst):
    return sorted(lst, key=lambda x: len(x), reverse=True)[0]
