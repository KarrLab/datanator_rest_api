import connexion
import pytest
import datanator_rest_api.core as core


AutoResolver = core.AutoResolver
app = connexion.FlaskApp(__name__)
app.add_api('../datanator_rest_api/spec/DatanatorAPI.yaml', resolver=AutoResolver(
    "datanator_rest_api.routes"), validate_responses=False)


@pytest.fixture()
def client():
    with app.app.test_client() as c:
        yield c


def test_routes_implemented(client):
    response = client.get('/datanator/')
    print(type(response.data))
    print(response.data)
    assert(response.status_code == 200)
