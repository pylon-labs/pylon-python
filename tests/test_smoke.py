from usepylon import AsyncPylon, Pylon
from usepylon.environment import PylonEnvironment


def test_clients_expose_nested_resources() -> None:
    for client in (Pylon(token="test", environment=PylonEnvironment.EU), AsyncPylon(token="test")):
        assert callable(client.issues.list)
        assert callable(client.knowledge_bases.articles.get)
