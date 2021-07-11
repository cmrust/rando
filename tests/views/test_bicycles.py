import uuid


def test_crud(client):
    # create
    # generate unique values for bicycle fields
    year = uuid.uuid1().int % 10000  # get the 4 digit remainder of division by 10000, to mock 4 digit year
    make = str(uuid.uuid4())
    model = str(uuid.uuid4())
    r = client.post("/bicycles", json=dict(year=year, make=make, model=model))
    r.raise_for_status()

    # read
    url = f"/bicycles/{r.json()['id']}"
    r = client.get(url).json()
    assert r["year"] == year
    assert r["make"] == make
    assert r["model"] == model

    # delete
    client.delete(url).raise_for_status()
    assert client.get(url).status_code == 404
