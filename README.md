# Banking MCP Bridge

A high-performance **Model Context Protocol (MCP)** server that enables Large Language Models (like Claude) to securely interact with a robust Java-based banking core.

## Architecture
This project acts as a specialized "translation layer." It decouples the AI interface (Python) from the enterprise business logic (Java), allowing for independent scaling and maintenance.

* **Host:** Claude Desktop (JSON-RPC)
* **Bridge Server:** Python 3.11+ (FastMCP)
* **Execution Core:** Java 17 (Maven)
* **Storage:** SQLite (JDBC)



## Key Technical Challenges & Solutions
Developing this bridge required solving several low-level integration hurdles:
* **Process Isolation:** Used Python's `subprocess` to manage a short-lived Java runtime for each tool call, ensuring no memory leaks in the long-running Python server.
* **Strict Pathing:** Overcame path resolution issues by implementing absolute path resolution for the SQLite database and Java binaries, a necessity for MCP servers running as background processes.
* **Dependency Wildcards:** Simplified the Java classpath by automating dependency collection with Maven (`copy-dependencies`), allowing a single wildcard to load all required JDBC drivers.

## Getting Started

### Prerequisites
1.  **Banking Core:** Ensure you have the [Banking Core Logic](https://github.com/skodavasal9/concurrent-banking-system) repository cloned and compiled (`mvn clean install`).
2.  **Java 17:** Must be installed and available on your system path.
3.  **Python 3.11+:** Recommended for FastMCP compatibility.

### Installation
1.  Clone this repository into your workspace.
2.  Create and activate a virtual environment:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Claude Desktop Integration
Add the following to your `claude_desktop_config.json` (usually found in `~/Library/Application Support/Claude/` on macOS):

```json
{
  "mcpServers": {
    "banking-system": {
      "command": "/Users/YOUR_USER/path/to/banking-mcp-bridge/.venv/bin/python3",
      "args": ["/Users/YOUR_USER/path/to/banking-mcp-bridge/server.py"],
      "env": {
        "PYTHONPATH": "/Users/YOUR_USER/path/to/banking-mcp-bridge"
      }
    }
  }
}

## Claude Desktop Integration Demo
<img width="1469" height="856" alt="Screenshot 2026-01-02 at 7 32 00 PM" src="https://github.com/user-attachments/assets/9aa8da63-9042-4009-a3cb-6f9eacf7389c" />


