# -*- coding: utf-8 -*-


if __name__ == '__main__':

    with open(r'/package.json', 'r') as file:
    # read all content of a file
        content = file.read()
        print(content)
        # check if string present in a file
        if '-rc.0' in content:
            raise ValueError("Release Candidate found in package.json! Use only live versions of packages.")