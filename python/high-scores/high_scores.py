def latest(scores: list):
    return scores.pop()


def personal_best(scores):
    # return sorted(scores).pop()
    return max(scores)


def personal_top_three(scores):
    # return sorted(scores)[:-4:-1]
    _sortedscores = sorted(scores)
    _sortedscores.reverse()
    return _sortedscores[0:3]
