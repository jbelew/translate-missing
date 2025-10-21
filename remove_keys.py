
import json
import random
import sys

def flatten_dict(d, parent_key='', sep='.'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            # For lists, we'll treat each item as a separate key for removal purposes
            # This might not be ideal if the list order matters, but for simple key removal it works
            for i, item in enumerate(v):
                if isinstance(item, dict):
                    items.extend(flatten_dict(item, f"{new_key}{sep}{i}", sep=sep).items())
                else:
                    items.append((f"{new_key}{sep}{i}", item))
        else:
            items.append((new_key, v))
    return dict(items)

def unflatten_dict(flat_dict, sep='.'):
    result = {}
    for flat_key, value in flat_dict.items():
        parts = flat_key.split(sep)
        d = result
        for i, part in enumerate(parts):
            if i == len(parts) - 1:
                d[part] = value
            else:
                if part not in d:
                    d[part] = {}
                d = d[part]
    return result

def remove_keys_from_json(file_path, percentage_to_remove=0.02):
    with open(file_path, 'r') as f:
        data = json.load(f)

    flat_data = flatten_dict(data)
    all_keys = list(flat_data.keys())
    num_keys_to_remove = max(1, int(len(all_keys) * percentage_to_remove))
    keys_to_remove = random.sample(all_keys, num_keys_to_remove)

    for key in keys_to_remove:
        parts = key.split('.')
        current_level = data
        for i, part in enumerate(parts):
            if i == len(parts) - 1:
                if isinstance(current_level, dict) and part in current_level:
                    del current_level[part]
                elif isinstance(current_level, list) and part.isdigit() and int(part) < len(current_level):
                    # This is a simplification. Removing from a list by index can shift elements.
                    # For this task, we'll just set it to None or a placeholder if it's a simple value.
                    # If it's a dict in a list, we'd need more complex logic.
                    # For now, let's assume we only remove top-level keys or keys within nested dicts.
                    pass # We'll only remove keys from dicts, not list elements directly
            else:
                if isinstance(current_level, dict) and part in current_level:
                    current_level = current_level[part]
                elif isinstance(current_level, list) and part.isdigit() and int(part) < len(current_level):
                    current_level = current_level[int(part)]
                else:
                    break # Key path not found, move to next key_to_remove

    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python remove_keys.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    remove_keys_from_json(file_path)
    print(f"Removed approximately 2% of keys from {file_path}")
