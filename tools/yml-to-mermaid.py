import yaml
from pathlib import Path

# --- Configuration ---
REPO_ROOT = Path(__file__).parent.parent
YAML_FILE = REPO_ROOT / "data" / "books.yml"
OUTPUT_FILE = REPO_ROOT / "map.mmd"

def generate_mermaid_from_yaml():
    """Reads data from a YAML file and generates a Mermaid diagram string for navigation."""
    
    print(f"Reading data from: {YAML_FILE}")
    with open(YAML_FILE, 'r') as f:
        data = yaml.safe_load(f)

    mermaid_lines = ["flowchart TD"]
    mermaid_lines.append("")
    all_node_ids = ""

    # # --- Add Node Definitions ---
    # for node_id, node_data in data.get('nodes', {}).items():
    #     label = node_data['label']
    #     mermaid_lines.append(f'    {node_id}["{label}"]')

    # --- Add Node Definitions ---
    for node in data.get('nodes', []):
        node_id = node['id']
        label = node['label']
        href = node['href']
        mermaid_lines.append(f'    {node_id}["{label}"]')
        mermaid_lines.append(f'    click {node_id} "{href}"')
        all_node_ids = all_node_ids + "," + str(node_id)
    
    mermaid_lines.append("\n\n")

    # --- Add Edge Definitions ---
    for edge in data.get('edges', []):
        from_node = edge['from']
        to_node = edge['to']
        label = edge['label']
        mermaid_lines.append(f'    {from_node} -- "{label}" --> {to_node}')
        
    mermaid_lines.append("")

    # --- Add Click Interactions for Navigation ---
    # e.g., click h "/books/the-hobbit.html"
    # for node_id, node_data in data.get('nodes', {}).items():
    #     if 'href' in node_data and node_data['href']:
    #         href = node_data['href']
    #         # This syntax tells mermaid to treat the click as a standard link
    #         mermaid_lines.append(f'    click {node_id} "{href}"')
            
    mermaid_lines.append("")
    mermaid_lines.append('    classDef bookNode text-align:center')
    # all_node_ids = ",".join(data.get('nodes', {}).keys())
    # all_node_ids = ",".join([node['id'] for node in data.get('nodes', [])])
    mermaid_lines.append(f'    class {all_node_ids} bookNode')

    return "\n".join(mermaid_lines)

def main():
    """Main function to generate and write the Mermaid file."""
    mermaid_content = generate_mermaid_from_yaml()
    print("--- Generated Mermaid Content ---")
    print(mermaid_content)
    print("---------------------------------")
    print(f"Writing Mermaid diagram to: {OUTPUT_FILE}")
    with open(OUTPUT_FILE, 'w') as f:
        f.write(mermaid_content)
    print("Successfully generated map.mmd")

if __name__ == "__main__":
    main()
