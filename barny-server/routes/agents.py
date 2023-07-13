from fastapi import APIRouter
from models.AgentModel import AgentModel

TEST_SET = [
    {
        "name": "DBServer",
        "ip": "10.0.0.5",
        "domain": "emberdb.dori.local",
    },
    {
        "name": "WebServer",
        "ip": "10.0.0.1",
        "domain": "emberweb.dori.local",
    },
    {
        "name": "Backend",
        "ip": "10.0.0.7",
        "domain": "emberbackend.dori.local",
    },
]

router = APIRouter(
    prefix="/agents",
)

@router.get("/")
def get_list():
    return TEST_SET

@router.post("/")
def add_new(agent: AgentModel):
    TEST_SET.append(agent)

@router.put("/{agent_id}")
def update(agent_id: int, agent: AgentModel):
    TEST_SET[agent_id] = TEST_SET[agent_id] | agent.dictionary()

    return TEST_SET[agent_id]

@router.delete("/{agent_id}")
def delete(agent_id: int):
    deleted_agent = TEST_SET[agent_id]
    TEST_SET.pop(agent_id)

    return deleted_agent
