import json
from datetime import datetime
from confing import dir_json


def open_json(dir_file=dir_json):
    with open(dir_file, encoding='UTF8') as f:
        parsed_data = json.load(f)
        return parsed_data


def operation_limit_sort(limited, operation=open_json()):
    json_data = []

    for parsed in operation:
        if parsed and parsed["state"] == "EXECUTED":
            json_data.append({"date": datetime.strptime(parsed.get("date"), "%Y-%m-%dT%H:%M:%S.%f"),
                              "operationAmount_amount": parsed.get("operationAmount").get("amount"),
                              "operationAmount_currency_name": parsed.get("operationAmount").get("currency").get(
                                  "name"),
                              "description": parsed.get("description"),
                              "from": parsed.get("from"),
                              "to": parsed.get("to")})

    json_data.sort(key=lambda x: x.get("date"), reverse=True)
    print(json_data)
    return json_data[:limited]


def hiding_account(operation):
    if operation:
        letters_from_account = "".join(c for c in operation if c.isalpha())
        igits_from_account = "".join(c for c in operation if c.isdigit())
        if "счет" in operation.lower():
            return letters_from_account + ' ' + f"**{igits_from_account[2:6]}"

        elif len(igits_from_account) == 16:
            formatted_account = " ".join([igits_from_account[i:i + 4] for i in range(0, 16, 4)])
            formatted_account = (formatted_account[:7] + f"** ****{formatted_account[-5:]}")
            return letters_from_account + " " + formatted_account

        else:
            return operation
    else:
        return ""


def print_operation(operation):
    for data in operation:
        indicator = ""
        if data.get("from"):
            indicator = " -> "
        print(f"{data.get("date").strftime('%d.%m.%Y')} {data.get("description")}"
              f"\n{hiding_account(data.get("from"))}{indicator}{hiding_account(data.get("to"))}"
              f"\n{data.get("operationAmount_amount")} {data.get("operationAmount_currency_name")}"
              f"\n")



