import typer
import requests

app = typer.Typer()

@app.command()
def my_cli_app(
    git_url: str = typer.Option(..., help="The Git URL"),
    git_branch: str = typer.Option(..., help="The Git branch"),
    app_name: str = typer.Option(..., help="The application name"),
    explain: bool = typer.Option(False, "--explain", "-e", help="This command clones your repository, processes the files against Watsonx, and provides output with code summaries, comments, and unit test cases.")
):
    """
    A CLI app that calls an API with given Git details and prints the CLI command.
    """
    if explain:
        typer.echo("This command calls an API with the provided Git details and prints the CLI command.")
        return

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    body = {
        "git_req": {
            "git_url": git_url,
            "git_branch": git_branch,
            "app_name": app_name
        }
    }
    url = "https://code-explorer-pre-prod.dal2a.ciocloud.nonprod.intranet.ibm.com/api/github"
    response = requests.post(url, json=body, headers=headers)
    if response.status_code == 201:
        typer.echo("Your request has been submitted. Please check your repository later. You will receive a new pull request from WCA Code Explorer.")
    else:
        typer.echo(f"Request failed. Please contact DX-WX-4code Team.")

    # Print the command
    command = f"my_cli_app --git-url {git_url} --git-branch {git_branch} --app-name {app_name}"
    #typer.echo(f"Command: {command}")

if __name__ == "__main__":
    app()
