import json
import os
import uuid
from datetime import datetime
from pathlib import Path

from allure_commons.model2 import Parameter, TestStepResult
from allure_commons.model2 import TestResult
from allure_commons.utils import now


def parse_json_to_allure(json_data):
    with open(json_data) as file:
        data = json.load(file)

    for feature in data['features']:
        for scenario in feature['scenarios']:
            test_case = TestResult(uuid=scenario['id_feature'], start=now())
            test_case.name = scenario['name']
            test_case.fullName = scenario['name']

            for tag in scenario['tags']:
                if "epic" in tag:
                    test_case.labels.append({"name": "epic", "value": tag.split("=")[-1]}),
                elif "author" in tag:
                    test_case.labels.append({"name": "author", "value": tag.split(":")[-1]}),
                elif "allure.tms" in tag:
                    test_case.links.append(
                        {"type": "tms", "url": tag.split("tms:")[-1], "name": tag.split("tms:")[-1]}),
                elif "allure.issue" in tag:
                    test_case.links.append(
                        {"type": "issue", "url": tag.split("issue:")[-1], "name": tag.split("issue:")[-1]}),
                elif tag in ("normal", "trivial", "minor", "critical", "blocker"):
                    test_case.labels.append({"name": "severity", "value": tag}),
                else:
                    test_case.labels.append({"name": "tag", "value": tag})

            for step in scenario['steps']:
                allure_step = TestStepResult(name=step["step_type"].capitalize() + " " + step["name"], start=now())
                allure_step.status = step["status"]
                allure_step.start = datetime.now().timestamp()
                allure_step.stop = step["duration"]
                if step["status"] in ("failed", "broken"):
                    allure_step.statusDetails = {"message": step['error_msg'],
                                                 "trace": step['error_lines']}
                test_case.steps.append(allure_step)

            if scenario.get('parameters'):
                for param in scenario['parameters']:
                    test_case.parameters.append(Parameter(name=param['name'], value=param['value']))

            test_case.stop = datetime.now().timestamp()
            test_case.status = scenario['status']

            test_case_dict = {
                "name": test_case.name,
                "status": test_case.status,
                "parameters": [(param.name, param.value) for param in test_case.parameters],
                "steps": [{
                    "name": step.name,
                    "start": step.start,
                    "stop": step.stop,
                    "status": step.status,
                    "statusDetails": step.statusDetails if step.status in ("failed", "broken") else {}
                } for step in test_case.steps],
                "start": test_case.start,
                "stop": test_case.stop,
                "uuid": str(test_case.uuid),
                "fullName": test_case.fullName,
                "labels": [item for item in test_case.labels],
                "links": [item for item in test_case.links],

            }

            output_dir = Path(__file__).resolve().parent / "allure-report"
            output_dir.mkdir(parents=True, exist_ok=True)
            path = output_dir / f"{uuid.uuid4()}.json"
            json_object = json.dumps(test_case_dict)
            with open(path, "w") as outfile:
                outfile.write(json_object)


if __name__ == "__main__":
    path = os.path.join(Path(__file__).resolve().parent, "output", "report.json")
    parse_json_to_allure(path)
