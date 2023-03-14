#Geração de hierarquia pai e filho
#Generation of parent and child hierarchy”

test_database = [(1, 1), (2, 1), (2, 8), (2, 3), (3, 5), (5, 1), (6, 7), (7, 6), (7, 9), (8, 1), (9, 6)]

def get_path(database, paths = []):
    for child, parent in database:
        current_id = child
        parent_id = parent
        current_path = [current_id]
        while parent_id != 0:
            current_path.insert(0, parent_id)
            parent_id = next((p for c, p in database if c == parent_id and p not in current_path), 0)
        paths.append({current_id: current_path[::-1]})
    return paths

print(get_path(test_database))