def my_var() -> dict[str, str]:
    d = [
        ('Hendrix' , '1942'),
        ('Allman' , '1946'),
        ('King' , '1925'),
        ('Clapton' , '1945'),
        ('Johnson' , '1911'),
        ('Berry' , '1926'),
        ('Vaughan' , '1954'),
        ('Cooder' , '1947'),
        ('Page' , '1944'),
        ('Richards' , '1943'),
        ('Hammett' , '1962'),
        ('Cobain' , '1967'),
        ('Garcia' , '1942'),
        ('Beck' , '1944'),
        ('Santana' , '1947'),
        ('Ramone' , '1948'),
        ('White' , '1975'),
        ('Frusciante', '1970'),
        ('Thompson' , '1949'),
        ('Burton' , '1939')
    ]
    return d

def gen_dict(d: list[tuple]) -> dict[int, list[str]]:
    # 1. Group names by year
    dictionary = dict()
    for name, year_str in d:
        year = int(year_str)
        if year not in dictionary:
            dictionary[year] = []
        dictionary[year].append(name)
    return dictionary

if __name__ == "__main__":
    diction = gen_dict(my_var())
    for year, names in diction.items():
        for n in names:
            print(year, ":", n)