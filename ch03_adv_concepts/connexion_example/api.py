from pathlib import Path

data_file = '../../data/celebrity_100.csv'
data = [line.strip().split(',') for line in Path(data_file).open(encoding='unicode_escape')][1:]


def get_celebrities():
    return {'celebs': data[:50]}


def create_celebrity(celebrity):
    status = 200
    name, pay, category, year = celebrity.get('name'), celebrity.get('pay'), celebrity.get('category'), celebrity.get('year')
    data.append([name, pay, category, year])

    return {'celeb': celebrity}, status


def get_celebrity(name):
    status = 200
    matches = [celeb for celeb in data if celeb[0].casefold() == name.casefold()]
    print(f'GET celeb.  Searching for: {name}')
    print(f'Matches: {matches}')
    if not matches:
        status = 404
    return {'name': matches}, status


def put_celebrity(name, celebrity):
    match_idx = -1
    status = 200
    for idx, celeb in enumerate(data):
        if celeb[0].casefold() == name.casefold():
            match_idx = idx
            break

    if match_idx != -1:
        data[match_idx] = [name, celebrity.get('pay'), celebrity.get('year'), celebrity.get('category')]
        message = f'Updated: {data[match_idx][0]}'
    else:
        message = 'No one updated.'
        status = 404

    return {'message': message, 'status': status}, status


def delete_celebrity(name):
    match = None
    status = 200
    for celeb in data:
        if celeb[0].casefold() == name.casefold():
            match = celeb
            break
    if match:
        data.remove(match)
        message = f'Removed: {match}'
    else:
        message = 'No one removed.'
        status = 404

    return {'message': message, 'status': status}, status
