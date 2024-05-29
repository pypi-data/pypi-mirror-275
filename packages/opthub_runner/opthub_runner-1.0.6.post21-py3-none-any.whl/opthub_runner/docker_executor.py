"""Docker Execution Module."""

import json
from typing import TypedDict, cast

import docker

from opthub_runner.converter import float_to_json_float


class DockerConfig(TypedDict):
    """A type for docker execution configuration."""

    image: str
    environments: dict[str, str]
    command: list[str]
    timeout: float
    rm: bool


def execute_in_docker(
    config: DockerConfig,
    std_in: list[str],
) -> dict[str, object]:
    """Execute command in docker container.

    Args:
        config (DockerConfig): docker image name
        std_in (list[str]): standard input

    Returns:
        dict[str, Any]: parsed standard output
    """
    client = docker.from_env()

    client.images.pull(config["image"])  # pull image

    container = client.containers.run(
        image=config["image"],
        command=config["command"],
        environment=config["environments"],
        stdin_open=True,
        detach=True,
    )

    socket = container.attach_socket(params={"stdin": 1, "stream": 1, "stdout": 1, "stderr": 1})

    for line in std_in:
        socket._sock.sendall(line.encode("utf-8"))  # noqa: SLF001

    container.wait(timeout=config["timeout"])

    stdout = container.logs(stdout=True, stderr=False).decode("utf-8")

    if config["rm"]:
        container.remove()

    out: dict[str, object] | None = parse_stdout(stdout)

    if out is None:
        msg = "Failed to parse stdout."
        raise RuntimeError(msg)

    return cast(dict[str, object], float_to_json_float(out))


def parse_stdout(stdout: str) -> dict[str, object] | None:
    """Parse stdout.

    Args:
        stdout (str): stdout

    Returns:
        dict[str, Any] | None: parsed stdout
    """
    lines = stdout.split("\n")
    lines.reverse()
    for line in lines:
        if line:
            line_dict: dict[str, object] = json.loads(line)
            return line_dict
    return None
