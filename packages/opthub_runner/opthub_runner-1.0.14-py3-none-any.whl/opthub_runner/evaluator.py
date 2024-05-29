"""This module implements the evaluator."""

import json
from typing import TypedDict

from opthub_runner.docker_executor import execute_in_docker


class EvaluationResult(TypedDict):
    """A type for evaluation result."""

    objective: object
    feasible: bool | None
    constraint: object | None
    info: object


class Evaluator:
    """The Evaluator class."""

    def __init__(
        self,
        docker_image: str,
        environment: dict[str, str],
        *,
        rm: bool = True,
        timeout: float = 43200,
    ) -> None:
        """Initialize the Evaluator class.

        Args:
            docker_image (str): The docker image URL.
            environment (dict[str, str]): The environments.
            rm (bool, optional): Remove the container after execution. Defaults to True.
            timeout (float, optional): The timeout for the execution. Defaults to 43200 .

        """
        self.docker_image = docker_image
        self.environment = environment
        self.timeout = timeout
        self.rm = rm

    def run(self, variable: object) -> EvaluationResult:
        """Run the evaluator.

        Args:
            variable (object): The variable to evaluate.

        Returns:
            EvaluationResult: The evaluation result.
        """
        docker_output = execute_in_docker(
            {
                "image": self.docker_image,
                "environments": self.environment,
                "command": [],
                "timeout": self.timeout,
                "rm": self.rm,
            },
            [json.dumps(variable) + "\n"],
        )
        if "error" in docker_output:
            error = docker_output["error"]
            msg = f"Error occurred while evaluating solution:\n{error}"
            raise RuntimeError(msg)

        feasible = docker_output.get("feasible", None)

        if feasible is not None and not isinstance(feasible, bool):
            msg = f"Feasible value is not boolean: {feasible}"
            raise TypeError(msg)

        evaluation_result: EvaluationResult = {
            "objective": docker_output["objective"],
            "feasible": feasible,
            "constraint": docker_output.get("constraint", None),
            "info": docker_output.get("info", None),
        }
        return evaluation_result
