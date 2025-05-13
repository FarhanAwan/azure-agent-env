import typer
from agent_runtime import agent_loop

app = typer.Typer()

# Accept a query argument and run the agent loop
@app.command()
def ask(query: str):
    """Accept a query and run the agent loop to process it."""
    print(f"Debug: Received query '{query}'")  # Debug print to check how Typer is parsing the argument
    response = agent_loop(query)
    print(response)

if __name__ == "__main__":
    print("Debug: Running the Typer app...")  # Added debug print to confirm app() is being invoked correctly
    app()  # This is where Typer processes the command
