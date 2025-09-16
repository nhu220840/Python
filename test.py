def generate_language_strings(max_length=5):
    results = set()
    def dfs(current, state):
        if len(current) > max_length: return
        if state == 'S':
            dfs(current + '0', 'A')
            dfs(current + '1', 'A')
        elif state == 'A':
            dfs(current + '0', 'B')
        elif state == 'B':
            results.add(current + '1')
            dfs(current + '1', 'A')
    dfs('', 'S')
    return sorted(s for s in results if len(s) <= max_length)

for s in generate_language_strings(): print(s)