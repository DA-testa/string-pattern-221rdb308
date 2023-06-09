# python3

def read_input():
    input_type = input().rstrip()
    if input_type == 'I':
       pattern = input().rstrip()
       text = input().rstrip()
    else:
        filename = '06'
        folder = './tests/'
        with open(folder + filename, 'r') as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()
    return (pattern, text)

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    occurrences = []
    p_len = len(pattern)
    t_len = len(text)
    prime = 101
    
    def calculate_hash(l):
        h = 0
        for i in range(len(l)):
            h = (h * prime + ord(l[i])) % t_len
        return h
    p_hash = calculate_hash(pattern)
    t_hash = calculate_hash(text[:p_len])
    for i in range(t_len - p_len + 1):
        if p_hash == t_hash and text[i:i+p_len] == pattern:
            occurrences.append(i)
        if i < t_len - p_len:
            t_hash = (t_hash * prime - ord(text[i])*(prime ** p_len) + ord(text[i+p_len])) % t_len
    return occurrences


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

