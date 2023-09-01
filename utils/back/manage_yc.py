import requests
import os
from subprocess import PIPE, run
import json
from .bearer import BearerAuth


def structuring_list(list_item):
    dictionary_of_items = [
        list_item["id"],
        list_item["name"],
        list_item["status"]]
    return dictionary_of_items


def start_instance(instance, token):
    requests.post("https://compute.api.cloud.yandex.net/compute/v1/instances/" + instance('id') + ":start")


def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout


def generate_iam_token():
    get_token = out("yc iam create-token")
    get_token = get_token[:-1]
    return get_token


def main_function(listAnswers):
    myToken = listAnswers[1]
    folderId = listAnswers[0]
    headers = {"Authorization": "Bearer " + str(myToken) + ""}
    # Get all Cloud Instances
    instanceRequest = requests.get("https://compute.api.cloud.yandex.net/compute/v1/instances?folderId=" + folderId,
                                   auth=BearerAuth(str(myToken)))
    list_all_instances = []

    # Преобразование словаря в JSON-строку
    x = json.dumps(instanceRequest.json())
    # Преобразовываем JSON-строку в сам JSON, чтобы можно было к нему обращаться
    data = json.loads(x)
    # x = json.dumps(instanceRequest.json())
    for line in data.get('instances'):
        list_all_instances.append(structuring_list(line))
        # print(line['name'])
        # print("========")
    # print(data.get('instances'))

    return list_all_instances

    # for instance in list_all_instances:
    #     print(instance)

# for instance in instanceRequest:
#     listAllInstances.append(structuring_list(instance))

# for instance in listAllInstances:
#     print(instance)
