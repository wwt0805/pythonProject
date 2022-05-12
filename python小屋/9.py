def main(lst):
    return sorted(lst, key=lambda x: len(x))


if __name__ == '__main__':
    main(["location", "py", "baseline", "run", "1"])
