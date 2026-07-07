# AGENTS.md

## Project Setup

- **Virtual Environment**: Always activate the virtual environment before working.
  ```bash
  source mcp_ai_env/Scripts/activate  # For Windows
  ```

- **Install Dependencies**: Use the following command to install required libraries.
  ```bash
  pip install -r requirements.txt
  ```

## Testing

- Run tests using the following command to ensure the integrity of the code.
  ```bash
  # Assuming there is a test framework set up
  pytest  # or the specific test command configured
  ```

## Development Conventions

- **Commands Order**: Follow this order when making changes:
  1. **Linting**: `lint`
  2. **Type Check**: `typecheck`
  3. **Run Tests**: `test`

- **Style Guide**: Follow PEP 8 for Python code style, unless otherwise specified.

## Environment Variables

- Define environment variables in the `.env` file as needed for API keys or configurations used in development.

## Important Notes

- If running into issues, review logs and configurations to catch any environment-specific details.
- Always verify that libraries are up to date via the `requirements.txt` file.
