import requests

ENDPOINT = "https://todo.pixegami.io"

def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200


def test_can_create_task():
    payload = {
        "content": "my test content",
        "user_id": "test_user",
        "is_done": False
    }
    create_task_response = requests.put(ENDPOINT + "/create-task", json=payload)
    assert create_task_response.status_code == 200

    data = create_task_response.json()
    print(data)

    task_id = data["task"]["task_id"]
    get_task_response = requests.get(ENDPOINT + f"/get-task/{task_id}")

    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    print(get_task_data)
    assert get_task_data["content"] == payload["content"]
    assert get_task_data["user_id"] == payload["user_id"]


    def test_can_update_task():
        #create a task
        #update the task
        #get and validate the changes
        pass

    def create_task(payload):
         return requests.put(ENDPOINT + "/create-task", json=payload)

    def get_task(task_id):
        return requests.get(ENDPOINT + f"/get-task/{task_id}")
