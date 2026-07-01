import json


def generate_json(report):

    return json.dumps(
        report,
        indent=4
    )