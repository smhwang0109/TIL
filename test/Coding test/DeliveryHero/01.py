from typing import List, Text


class NoAgentFoundException(Exception):
    return "There's no agent."


class Agent(object):
    def __init__(self, name, skills, load):
        self._name = name
        self.skills = skills
        self.load = load

    def __str__(self):
        return "<Agent: {}>".format(self._name)


class Ticket(object):
    def __init__(self, id, restrictions):
        self.id = id
        self.restrictions = restrictions


class FinderPolicy(object):
    def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]:
        agents = list(filter(lambda agent: agent.load < 3, agents))
        return agents

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        return


class LeastLoadedAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        agents.sort(key=lambda agent: agent.load)
        if agents:
            return agents[0]
        else:
            NoAgentFoundException


class LeastFlexibleAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        agents.sort(key=lambda agent: len(agent.skills))
        return agents[0]

ticket = Ticket(id="1", restrictions=["English"])
agent1 = Agent(name="A", skills=["English"], load=2)
agent2 = Agent(name="B", skills=["English", "Japanese"], load=0)
least_loaded_policy = LeastLoadedAgent()
# returns the Agent with name "B" because of their currently lower load.
print(least_loaded_policy.find(ticket, [agent1, agent2]))

least_flexible_policy = LeastFlexibleAgent()
# returns the Agent with name "A" because of their lower flexibility.
print(least_flexible_policy.find(ticket, [agent1, agent2]))