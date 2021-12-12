import util


delimiters = [
    ('(',')'),
    ('[',']'),
    ('{','}'),
    ('<','>')
]
delims_by_open  = {o:c for o,c in delimiters}
delims_by_close = {c:o for o,c in delimiters}


ERROR_SCORE = {
    '(' :     1,
    '[' :    2,
    '{' :  3,
    '<' : 4
}


def run():
    data = util.read_file("day10/input.txt", str)
    return calc(data)


def calc(data):
    scores = []
    for line in data:
        openned_delims = get_unclosed_delims(line)
        if openned_delims:
            line_score = 0
            for d in reversed(openned_delims):
                line_score = line_score * 5 + ERROR_SCORE[d]    
            scores.append(line_score)
    
    return sorted(scores)[len(scores)//2]


def get_unclosed_delims(line):
    stack = []
    for c in line:
        if c in delims_by_open:
            stack.append(c)
        else:
            if not stack:
                return []
            
            if delims_by_close[c] != stack.pop():
                return []
    
    return stack
