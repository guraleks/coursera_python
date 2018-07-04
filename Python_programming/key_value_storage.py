import argparse
import os
import tempfile
import json


parser = argparse.ArgumentParser()
parser.add_argument("-k", "--key", type=str)
parser.add_argument("-v", "--val", type=str)
args = parser.parse_args()

key = args.key
val = args.val

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


def get_data():
    if not os.path.exists(storage_path):
        return {}

    with open(storage_path, 'r') as f:
        raw_data = f.read()
        if raw_data:
            return json.loads(raw_data)
    return {}


def put(key, value):
    data = get_data()

    if key in data:
        data[key].append(value)
    else:
        data[key] = [value]

    with open(storage_path, 'w') as f:
        f.write(json.dumps(data))


def get(key):
    data = get_data()
    return data.get(key)


if key is not None  and val is not None:
    put(args.key, args.val)
elif key is not None:
    print(get(args.key))