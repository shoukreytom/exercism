# I know this solution is stupid but anywho it works

def latest(scores):
    return scores[-1]	#this returns last element is a list


# this is like checking the biggest number is a list
def personal_best(scores):
    best = scores[0]
    for score in scores:
        if score > best:
            best = score
    return best

# this method will affect the original list so you may have to make a copy of it
def personal_top_three(scores):
    copy_scores = scores.copy()  # you have to call a copy method (don't assign it directly it'll affect it)
    if len(scores) == 1:
    	return scores
    best = personal_best(copy_scores)
    copy_scores.remove(best)
    better = personal_best(copy_scores)
    if len(scores) == 2:
        return [best, better]
    else:
        copy_scores.remove(better)
        good = personal_best(copy_scores)
        return [best, better, good]
