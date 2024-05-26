import typer
import requests

app = typer.Typer()

@app.command()
def my_cli_app(
    git_url: str = typer.Option(..., help="The Git URL"),
    git_branch: str = typer.Option(..., help="The Git branch"),
    app_name: str = typer.Option(..., help="The application name")
):
    """
    A CLI app that calls an API with given Git details and prints the CLI command.
    """
    # Call the API
    print("git url", git_url)
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
    #print("url", url)
    response = requests.post(url, json=body, headers=headers)
    #print("response", response)
    if response.status_code == 201:
        typer.echo("Request Submitted!")
        #typer.echo("Response:")
        #typer.echo(response.json())
    else:
        typer.echo(f"Request failed. Please contact DX-WX-4code Team.")
        #typer.echo("Response:")
        #typer.echo(response.text)

    # Print the command
    command = f"my_cli_app --git-url {git_url} --git-branch {git_branch} --app-name {app_name}"
    #print(command)

if __name__ == "__main__":
    app()
