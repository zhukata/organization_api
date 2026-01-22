import httpx

base_url = "http://localhost:8000"
headers = {"X-API-KEY": "secret-key"}

def test_get_buildings():
    response = httpx.get(f"{base_url}/buildings/", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    print("✓ test_get_buildings passed")

def test_get_organizations_by_building():
    response = httpx.get(f"{base_url}/organizations/by_building/1", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    for org in data:
        assert org["building_id"] == 1
    print("✓ test_get_organizations_by_building passed")

def test_get_organizations_by_activity():
    response = httpx.get(f"{base_url}/organizations/by_activity/1", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    print("✓ test_get_organizations_by_activity passed")

def test_get_organizations_in_radius():
    response = httpx.get(f"{base_url}/organizations/in_radius/?latitude=55.7558&longitude=37.6173&radius_km=1", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    print("✓ test_get_organizations_in_radius passed")

def test_get_organization_by_id():
    response = httpx.get(f"{base_url}/organizations/1", headers=headers)
    assert response.status_code == 200
    org = response.json()
    assert org["id"] == 1
    assert "name" in org
    assert "building_id" in org
    assert "phone_numbers" in org
    assert "activities" in org
    print("✓ test_get_organization_by_id passed")

def test_search_organizations_by_name():
    response = httpx.get(f"{base_url}/organizations/by_name/Организация", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    for org in data:
        assert "Организация" in org["name"]
    print("✓ test_search_organizations_by_name passed")

if __name__ == "__main__":
    try:
        test_get_buildings()
        test_get_organizations_by_building()
        test_get_organizations_by_activity()
        test_get_organizations_in_radius()
        test_get_organization_by_id()
        test_search_organizations_by_name()
        print("\nВсе проверки пройдены успешно!")
    except AssertionError as e:
        print(f"Проверка не пройдена: {e}")
        exit(1)
    except Exception as e:
        print(f"Ошибка: {e}")
        exit(1)