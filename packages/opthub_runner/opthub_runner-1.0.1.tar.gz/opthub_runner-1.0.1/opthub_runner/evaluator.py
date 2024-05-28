"""This module implements the evaluator."""

import json

from opthub_runner.docker_executor import execute_in_docker


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

    def run(self, variable: object) -> dict[str, object]:
        """Run the evaluator.

        Args:
            variable (Any): The variable to evaluate.

        Returns:
            dict[str]: The result of the evaluation.
        """
        evaluation_result = execute_in_docker(
            {
                "image": self.docker_image,
                "environments": self.environment,
                "command": [],
                "timeout": self.timeout,
                "rm": self.rm,
            },
            [json.dumps(variable) + "\n"],
        )
        if "error" in evaluation_result:
            error = evaluation_result["error"]
            msg = f"Error occurred while evaluating solution:\n{error}"
            raise RuntimeError(msg)
        if "feasible" not in evaluation_result:
            evaluation_result["feasible"] = None
        if "constraint" not in evaluation_result:
            evaluation_result["constraint"] = None
        if "info" not in evaluation_result:
            evaluation_result["info"] = {}
        return evaluation_result
