def generate_language_a():
    return ["abbb"]

def generate_language_b(max_steps=3):
    results = set()
    def dfs(current, steps):
        if steps > max_steps: return
        if all(c in 'ab' for c in current): results.add(current)
        for r in [('S', 'AB'), ('S', 'aA'), ('A', 'aB'), ('A', 'a'), ('B', 'ba')]:
            if r[0] in current: dfs(current.replace(r[0], r[1], 1), steps + 1)
    dfs('S', 0)
    return results

def generate_language_c(max_steps=3):
    results = set()
    def dfs(current, steps):
        if steps > max_steps: return
        if all(c in 'ab' for c in current): results.add(current)
        for r in [('S', 'AB'), ('S', 'AA'), ('A', 'aB'), ('A', 'a'), ('B', 'ab'), ('B', 'b')]:
            if r[0] in current: dfs(current.replace(r[0], r[1], 1), steps + 1)
    dfs('S', 0)
    return results

def generate_language_d(max_steps=3):
    results = set()
    def dfs(current, steps):
        if steps > max_steps: return
        if all(c in 'ab' for c in current): results.add(current)
        for r in [('S', 'AA'), ('S', 'B'), ('A', 'aaA'), ('A', 'aa'), ('B', 'bB'), ('B', 'b')]:
            if r[0] in current: dfs(current.replace(r[0], r[1], 1), steps + 1)
    dfs('S', 0)
    return results

def generate_language_e(max_depth=2):
    results = set()
    def expand_X(depth, pre, post):
        if depth == 0: return ['']
        return [pre + s + post for s in expand_X(depth - 1, pre, post)] + ['']
    for a in expand_X(max_depth, 'a', 'b'):
        for b in expand_X(max_depth, 'b', 'a'):
            results.add(a + b)
    return results

for i, func in enumerate([generate_language_a, generate_language_b, generate_language_c, 
                        generate_language_d, generate_language_e], 1):
    print(f"\nStrings generated in language (Problem 3{'abcde'[i-1]}):")
    for s in func(): print(s)