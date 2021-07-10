import uuid

def test_crud(client):
    # create
    # generate unique values for fields
    year = uuid.uuid1().int % 10000 # 4 digit remainder of dividing by 10000
    make = str(uuid.uuid4())
    model = str(uuid.uuid4())
    r = client.post("/bicycles", json=dict(year=year, make=make, model=model))
    r.raise_for_status()

    # retrieve
    url = f"/bicycles/{r.json()['id']}"
    r = client.get(url).json()
    assert r["year"] == year
    assert r["make"] == make
    assert r["model"] == model

    # delete
    client.delete(url).raise_for_status()
    assert client.get(url).status_code == 404
