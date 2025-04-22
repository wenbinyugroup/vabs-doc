import os
import re

source_dir = './source'
build_dir = './build/markdown'
output_file = 'combined_documentation.md'

def parse_toctree(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    toctree_pattern = re.compile(r'```{toctree}.*?```', re.DOTALL)
    entries_pattern = re.compile(r'^\s*(?!:)([^\s][^\n]*)', re.MULTILINE)
    toctree_blocks = toctree_pattern.findall(content)
    entries = []
    for block in toctree_blocks:
        entries += entries_pattern.findall(block)
    return entries

def collect_documents(start_file, visited=None):
    if visited is None:
        visited = set()
    docs = []
    entries = parse_toctree(os.path.join(source_dir, start_file))
    for entry in entries:
        normalized_entry = entry.strip()
        if normalized_entry not in visited:
            visited.add(normalized_entry)
            docs.append(normalized_entry)
            # Recursively collect documents from nested toctrees
            nested_file = os.path.join(source_dir, normalized_entry)
            if os.path.isfile(nested_file):
                docs += collect_documents(normalized_entry, visited)
    return docs

documents = collect_documents('index.md')

with open(output_file, 'w', encoding='utf-8') as outfile:
    for doc in documents:
        md_file = os.path.join(build_dir, doc)
        if os.path.isfile(md_file):
            with open(md_file, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
                outfile.write('\n\n')



