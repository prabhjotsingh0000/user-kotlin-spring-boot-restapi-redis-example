import random
import string
import uuid

def generate_random_string(length):
    """Generate a random string of given length"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def generate_non_repeating_uuids(num_uuids):
    uuids = set()
    while len(uuids) < num_uuids:
        new_uuid = uuid.uuid4()
        if new_uuid not in uuids:
            uuids.add(new_uuid)
    return list(uuids)

def generate_redis_commands(file_path, num_users):
    """Generate Redis commands for creating random AppUsers"""
    uuids = generate_non_repeating_uuids(num_users)
    with open(file_path, 'w') as file:
        for i in range(1, num_users + 1):
            idx = uuids[i-1]
            first_name = generate_random_string(5)
            last_name = generate_random_string(6)
            email = f"{first_name}.{last_name}@example.com"
            username = f"{first_name}{last_name}"
            password = generate_random_string(8)
            is_logged_in = random.choice([0,1])
            class_name = "com.andylilfs.userkotlinspringbootgraphqlredisexample.model.AppUser"

            file.write(f"HSET AppUser:{idx} firstName \"{first_name}\"\n")
            file.write(f"HSET AppUser:{idx} lastName \"{last_name}\"\n")
            file.write(f"HSET AppUser:{idx} email \"{email}\"\n")
            file.write(f"HSET AppUser:{idx} username \"{username}\"\n")
            file.write(f"HSET AppUser:{idx} password \"{password}\"\n")
            file.write(f"HSET AppUser:{idx} isLoggedIn {is_logged_in}\n")
            file.write(f"HSET AppUser:{idx} _class \"{class_name}\"\n")
            file.write(f"HSET AppUser:{idx} id \"{idx}\"\n")
            file.write(f"SADD AppUser \"{idx}\"\n\n")

if __name__ == '__main__':
    num_users = 1000000
    file_path = 'create_users_redis_commands_1million.txt'
    generate_redis_commands(file_path, num_users)
    print(f"Redis commands generated and saved to {file_path}")
