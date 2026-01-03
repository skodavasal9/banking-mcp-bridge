from mcp.server.fastmcp import FastMCP
import subprocess
import json
import os

# Initialize the MCP Server
mcp = FastMCP("BankingSystem")

# Configuration for your Java Environment
# The list of all your required JARs and classes

JAVA_CP = "target/classes:target/dependency/*"

MAIN_CLASS = "BankingSystem.BankCLI"
APP_ROOT = "/Users/snigdhakodavasal/CodingFun/APITesting/src/main/java/BankingSystem"

@mcp.tool()
def get_balance(account_id: str) -> str:
    """
    Get the current balance and status for a specific bank account.
    """
    try:
        # Spawning the Java process exactly like you did in the terminal
        result = subprocess.run(
            ["java", "-cp", JAVA_CP, MAIN_CLASS, "get_balance", account_id],
            cwd=APP_ROOT,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error from Java core: {e.stdout or e.stderr}"

@mcp.tool()
def create_account(name: str, initial_deposit: float) -> str:
    """
    Create a new bank account for a customer with an initial deposit.
    """
    try:
        result = subprocess.run(
            ["java", "-cp", JAVA_CP, MAIN_CLASS, "create_account", name, str(initial_deposit)],
            cwd=APP_ROOT,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error from Java core: {e.stdout or e.stderr}"

if __name__ == "__main__":
    mcp.run()