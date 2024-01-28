


class Rule:
    def __init__(self):
        self.premise = list()
        self.conclusion: str


    def add_premise(self, prem: str):
        self.premise.append(prem)



def test_rule(r: Rule, bdf: list[str]) -> bool:
    for prop in r.premise:
        if not(prop in bdf):
            return False
    return True


def infer(knowl_base: list[Rule], bdf: list[str]) -> list[str]:
    ret_bdf = []
    for prop in bdf:
        ret_bdf.append(prop)

    for rule in knowl_base:
        if test_rule(rule, bdf) and not(rule.conclusion in bdf):
            ret_bdf.append(rule.conclusion)

    return ret_bdf


def engine(knowl_base: list[Rule], bdf: list[str]) -> list[str]:
    new_bdf = infer(knowl_base, bdf)

    while new_bdf != bdf:
        bdf = new_bdf
        new_bdf = infer(knowl_base, bdf)

    return bdf



if __name__ == "__main__":
    new_rule = Rule()
    new_rule.add_premise("Deus est Deus")
    new_rule.conclusion = "Deus est"

    knowledge = []
    knowledge.append(new_rule)

    bdf = ["Deus est Deus"]
    bdf = engine(knowledge, bdf)
    print(bdf)