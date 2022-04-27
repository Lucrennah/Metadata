from os import scandir

route = './'
l_archive = sorted([archive.name for archive in scandir(route) if archive.is_file()])


def test():
    for c in range(0, len(l_archive)):
        b = "Episode {} = {}".format(c, l_archive[c])
        print(b)
