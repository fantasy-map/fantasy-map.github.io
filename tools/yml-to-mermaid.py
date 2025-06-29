import yaml
import json
from pathlib import Path

# --- Configuration ---
REPO_ROOT = Path(__file__).parent.parent
YAML_FILE = REPO_ROOT / "data" / "books.yml"
OUTPUT_FILE = REPO_ROOT / "map.mmd"

def generate_mermaid_from_yaml():
    """Reads data from a YAML file and generates a Mermaid diagram string."""
    
    print(f"Reading data from: {YAML_FILE}")
    with open(YAML_FILE, 'r') as f:
        data = yaml.safe_load(f)

    mermaid_lines = ["flowchart TD"]
    mermaid_lines.append("")

    # --- Add Node Definitions ---
    # This is the section with the fix.
    for node_id, node_data in data.get('nodes', {}).items():
        # THE FIX IS HERE: We explicitly pull out the 'label' from the node_data dictionary.
        label = node_data['label']
        # Now we use *only* the label variable to create the node text.
        mermaid_lines.append(f'    {node_id}["{label}"]')

    mermaid_lines.append("")

    # --- Add Edge Definitions (This part was already correct) ---
    for edge in data.get('edges', []):
        from_node = edge['from']
        to_node = edge['to']
        label = edge['label']
        mermaid_lines.append(f'    {from_node} -- "{label}" --> {to_node}')
        
    mermaid_lines.append("")

    # --- Add Click Interactions (This part was also already correct) ---
    for node_id, node_data in data.get('nodes', {}).items():
        if 'details' in node_data and node_data['details']:
            details_text = json.dumps(node_data['details'])
            mermaid_lines.append(f'    click {node_id} call showDialog({details_text})')
            
    mermaid_lines.append("")
    mermaid_lines.append('    classDef bookNode text-align:center')
    all_node_ids = ",".join(data.get('nodes', {}).keys())
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
