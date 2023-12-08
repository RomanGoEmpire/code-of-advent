# https://adventofcode.com/2023/day/2

with open("2.txt", "r") as f:
    lines = f.readlines()

    max_r = 12
    max_g = 13
    max_b = 14

    passed_id = []

    for line in lines:
        line = (
            line.replace(" ", "")
            .replace("\n", "")
            .replace("red", "r")
            .replace("green", "g")
            .replace("blue", "b")
        )
        id, rest = line.split(":")
        games = rest.split(";")
        new_games = []
        for game in games:
            new_games += game.split(",")
        passed = True
        for cubes in new_games:
            if "r" in cubes:
                cubes = cubes.replace("r", "")
                if int(cubes) > max_r:
                    passed = False
            if "g" in cubes:
                cubes = cubes.replace("g", "")
                if int(cubes) > max_g:
                    passed = False
            if "b" in cubes:
                cubes = cubes.replace("b", "")
                if int(cubes) > max_b:
                    passed = False

        id = int(id[4:])
        if passed:
            print(id)
            passed_id.append(id)

    print(sum(passed_id))
