
from functools import reduce

scoring_dict = {
    "Not at all": 0, "Not difficult at all": 0, "Never or almost never": 0,
    "Quite difficult": 1, "A little": 1, "Sometimes": 1,
    "Often": 2,  "Very difficult": 2,
    "Always": 3, "Impossible": 3, "Always or nearly always": 3
}

def get_total_score(values):
  result = reduce(
                  (lambda x, y: x + y), 
                  [scoring_dict[v] for v in values]
                )
  return result



