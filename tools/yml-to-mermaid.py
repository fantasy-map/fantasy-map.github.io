import yaml
from pathlib import Path

# This script converts the YAML data from data/graph.yml into a Mermaid flowchart.

# --- Configuration ---
# Use Path objects for robust file handling.
# This assumes the script is run from the repository's root directory.
REPO_ROOT = Path(__file__).parent.parent
YAML_FILE = REPO_ROOT / "data" / "books.yml"
OUTPUT_FILE = REPO_ROOT / "map.mmd"

def generate_mermaid_from_yaml():
    """Reads data from a YAML file and generates a Mermaid diagram string."""
    
    print(f"Reading data from: {YAML_FILE}")
    with open(YAML_FILE, 'r') as f:
        data = yaml.safe_load(f)

    # Start building the Mermaid string
    mermaid_lines = ["flowchart TD"]

    # Add node definitions (e.g., h["The Hobbit"])
    for node_id, node_label in data.get('nodes', {}).items():
        mermaid_lines.append(f'    {node_id}["{node_label}"]')

    # Add a blank line for readability
    mermaid_lines.append("")

    # Add edge definitions (e.g., h -- "World-building" --> d)
    for edge in data.get('edges', []):
        from_node = edge['from']
        to_node = edge['to']
        label = edge['label']
        mermaid_lines.append(f'    {from_node} -- "{label}" --> {to_node}')
    
    return "\n".join(mermaid_lines)

def main():
    """Main function to generate and write the Mermaid file."""
    mermaid_content = generate_mermaid_from_yaml()
    
    print(f"Writing Mermaid diagram to: {OUTPUT_FILE}")
    with open(OUTPUT_FILE, 'w') as f:
        f.write(mermaid_content)
    print("Successfully generated map.mmd")

if __name__ == "__main__":
    main()
