import os
from typing import Optional, Text

import click


@click.group()
def app():
    pass


@click.group()
def agent():
    pass


@click.group()
def llm():
    pass


@click.command("version")
@click.option("--short", "-s", default=False, help="Action to run", is_flag=True)
def pkg_version(short: bool = False):
    from languru.version import VERSION

    if short is True:
        click.echo(VERSION)
    else:
        click.echo(f"languru {VERSION}")


@click.command("run")
@click.option("--port", "-p", default=None, help="Port to run the server")
def agent_run(port: Optional[int]):
    from languru.server.config import AgentSettings, AppType
    from languru.server.main import run_app

    settings = AgentSettings()
    settings.APP_TYPE = os.environ["APP_TYPE"] = AppType.agent

    # Parse port parameter
    if port is None and settings.PORT is not None:
        port = settings.PORT
    elif port is None:
        port = settings.DEFAULT_PORT
    port = int(port)
    if port == settings.DEFAULT_PORT:
        click.echo(f"Using default port {settings.DEFAULT_PORT}")
    else:
        click.echo(f"Using port {port} instead of default port {settings.DEFAULT_PORT}")
    settings.PORT, os.environ["PORT"] = port, str(port)

    click.echo("Running agent server")
    run_app(settings)


@click.command("run")
@click.option("--action", default=None, help="Action to run")
@click.option("--port", "-p", default=None, help="Port to run the server")
@click.option("--auto-port", default=True, help="Port to run the server")
@click.option("--agent-base-url", default=None, help="Agent base URL")
def llm_run(
    action: Optional[Text],
    port: Optional[int],
    auto_port: bool = True,
    agent_base_url: Optional[Text] = None,
):
    from languru.server.config import AppType, LlmSettings
    from languru.server.main import run_app
    from languru.utils.socket import check_port, get_available_port

    settings = LlmSettings()
    settings.APP_TYPE = os.environ["APP_TYPE"] = AppType.llm

    # Parse action parameter
    if action is not None and action.strip() != "":
        os.environ["ACTION"] = settings.action = action.strip()

    # Parse port parameter
    if port is None and settings.PORT is not None:
        port = settings.PORT
    elif port is None and auto_port is True:
        port = get_available_port(settings.DEFAULT_PORT)  # Search for available port
    elif port is None:
        port = settings.DEFAULT_PORT
    int(port)  # Check if port is a valid integer
    if check_port(port) is False:
        raise ValueError(f"The port '{settings.PORT}' is already in use")
    if port == settings.DEFAULT_PORT:
        click.echo(f"Using default port {settings.DEFAULT_PORT}")
    else:
        click.echo(f"Using port {port} instead of default port {settings.DEFAULT_PORT}")
    settings.PORT, os.environ["PORT"] = port, str(port)

    # Parse agent base URL parameter
    if agent_base_url is not None and agent_base_url.strip() != "":
        os.environ["AGENT_BASE_URL"] = settings.AGENT_BASE_URL = agent_base_url.strip()

    # Run the app
    click.echo("Running llm server")
    run_app(settings=settings)


agent.add_command(agent_run)

llm.add_command(llm_run)

app.add_command(agent)
app.add_command(llm)
app.add_command(pkg_version)


if __name__ == "__main__":
    app()
