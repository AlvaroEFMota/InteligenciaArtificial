from pomegranate import *
from collections import Counter

dia = Node(DiscreteDistribution({
    "sol": 0.9,
    "chuva": 0.1
}), name="dia")

previsao = Node(ConditionalProbabilityTable([
    ["chuva", "sol", 0.4],
    ["chuva", "chuva", 0.6],
    ["sol", "chuva", 0.1],
    ["sol", "sol", 0.9]
], [dia.distribution]), name="previsao")

previsao2 = Node(ConditionalProbabilityTable([
    ["chuva", "sol", 0.4],
    ["chuva", "chuva", 0.6],
    ["sol", "chuva", 0.1],
    ["sol", "sol", 0.9]
], [previsao.distribution]), name="previsao2")

model = BayesianNetwork()
model.add_states(dia,previsao,previsao2)
model.add_edge(dia, previsao)
model.add_edge(previsao, previsao2)
model.bake()


def generate_sample():
    sample = {}
    parents = {}
    for state in model.states:
        if isinstance(state.distribution, pomegranate.ConditionalProbabilityTable):
            sample[state.name] = state.distribution.sample(parent_values=parents)
        else:
            sample[state.name] = state.distribution.sample()
        parents[state.distribution] = sample[state.name]

    return sample

N = 1000
data = []
for i in range(N):
    sample = generate_sample()
    data.append(sample["previsao2"])
print(Counter(data))