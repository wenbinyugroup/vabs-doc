"""
Build One Markdown Document
---------------------------

This script combines multiple markdown files into a single document while maintaining
the proper heading hierarchy. It uses the toctree structure from Sphinx documentation
to determine which files to include and in what order.

The script ensures that headings in included files are properly incremented so that
they appear as sub-headings of the parent document (e.g., # becomes ##).

Usage:
    python build_one_md_doc.py

Output:
    A single file (combined_documentation.md) containing all documentation with
    properly adjusted heading levels.
"""
import os
import re

# Configuration paths
source_dir = './source'      # Directory containing the source markdown files
build_dir = './build/markdown'  # Directory containing the built markdown files
output_file = 'vabs_doc.md'  # Name of the combined output file

def ensure_dir_exists(file_path):
    """
    Create the directory structure for a file path if it doesn't exist.
    
    Args:
        file_path (str): Full path to the file
    """
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)


def parse_toctree(file_path):
    """
    Extract document entries from toctree directives in a markdown file.
    
    Args:
        file_path (str): Path to the markdown file containing toctree directives
    
    Returns:
        list: List of document entries referenced in the toctree directives
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all toctree blocks with the pattern ```{toctree}...```
    toctree_pattern = re.compile(r'```{toctree}.*?```', re.DOTALL)
    # Extract file entries (non-whitespace at start of line, excluding options that start with :)
    entries_pattern = re.compile(r'^\s*(?!:)([^\s][^\n]*)', re.MULTILINE)
    
    # Find all toctree blocks in the content
    toctree_blocks = toctree_pattern.findall(content)
    entries = []
    
    # Extract entries from each toctree block
    for block in toctree_blocks:
        entries += entries_pattern.findall(block)
    
    return entries


def remove_toctree_blocks(content):
    """
    Remove toctree blocks from markdown content.
    
    Args:
        content (str): The markdown content with toctree blocks
        
    Returns:
        str: The markdown content with toctree blocks removed
    """
    # Find and remove all toctree blocks with the pattern ```{toctree}...```
    toctree_pattern = re.compile(r'```{toctree}.*?```', re.DOTALL)
    return toctree_pattern.sub('', content)


def collect_documents(start_file, parent_dir="", visited=None, level=0):
    """
    Recursively collect all documents referenced in toctree directives,
    starting from a given file.
    
    Args:
        start_file (str): The starting markdown file to process
        parent_dir (str): The parent directory path relative to source_dir
        visited (set): Set of already visited documents to avoid cycles
    
    Returns:
        list: Ordered list of documents to include in the final output,
              with their full paths relative to source_dir
    """
    if visited is None:
        visited = set()
    
    docs = []
    # Form the full path of the current file
    current_file_path = os.path.join(source_dir, parent_dir, start_file)
    
    # Get all entries from the toctree directives in the start file
    entries = parse_toctree(current_file_path)
    
    # Get the directory of the current file for resolving relative paths
    current_dir = os.path.dirname(os.path.join(parent_dir, start_file))
    
    for entry in entries[1:-1]:
        level += 1

        normalized_entry = entry.strip()
        
        # Construct the full path relative to source_dir
        full_entry_path = os.path.normpath(os.path.join(current_dir, normalized_entry))
        
        # Skip files we've already processed to avoid cycles
        if full_entry_path not in visited:
            visited.add(full_entry_path)
            docs.append((full_entry_path, level))
            
            # Recursively process toctrees in child documents
            nested_file_path = os.path.join(source_dir, full_entry_path)
            if os.path.isfile(nested_file_path):
                # The parent directory for the recursive call is the directory part of full_entry_path
                docs += collect_documents(os.path.basename(full_entry_path), 
                                         os.path.dirname(full_entry_path), 
                                         visited, level)

        level -= 1
    
    return docs


def increment_headings(content, level=1):
    """
    Increment heading levels in markdown content by adding extra '#' characters.
    For example: '# Heading' becomes '## Heading' when level=1
    
    Args:
        content (str): The markdown content
        level (int): Number of levels to increment by
        
    Returns:
        str: Modified markdown with incremented heading levels
    """
    # Regex to match markdown headings (# to ######)
    # This matches the hash characters at the beginning of a line followed by whitespace and content
    heading_pattern = re.compile(r'^(#{1,6})(\s+.*)$', re.MULTILINE)
    
    def add_hashes(match):
        """Helper function to add hash marks to each heading match"""
        hashes = match.group(1)  # The existing hash marks (e.g., ###)
        if len(hashes) + level > 6:
            # Cap at 6 levels (######) as that's the maximum in markdown
            new_hashes = '#' * 6
        else:
            new_hashes = '#' * (len(hashes) + level)
        return new_hashes + match.group(2)  # Combine new hashes with the original heading text
    
    # Replace all headings with their incremented versions
    return heading_pattern.sub(add_hashes, content)


# Start document collection from index.md
documents = collect_documents('index.md')
for _doc in documents:
    print(_doc)

output_file_full = os.path.join(build_dir, output_file)
ensure_dir_exists(output_file_full)

# Create the combined output file
with open(output_file_full, 'w', encoding='utf-8') as outfile:
    # First, include the main index content without heading increment
    # This serves as the "root" document
    main_index_file = os.path.join(source_dir, 'index.md')
    if os.path.isfile(main_index_file):
        with open(main_index_file, 'r', encoding='utf-8') as infile:
            content = infile.read()
            # Remove toctree blocks from the content
            filtered_content = remove_toctree_blocks(content)
            outfile.write(filtered_content)
            outfile.write('\n\n')  # Add some spacing between documents

    # Then include all other documents with incremented heading levels
    for doc, level in documents:
        # Skip index.md if it appears in the list
        if doc == 'index.md':
            continue

        md_file = os.path.join(source_dir, doc)
        if os.path.isfile(md_file):
            with open(md_file, 'r', encoding='utf-8') as infile:
                content = infile.read()
                # Remove toctree blocks from the content
                filtered_content = remove_toctree_blocks(content)
                # Increment heading levels to maintain proper hierarchy
                modified_content = increment_headings(filtered_content, level=level)
                outfile.write(modified_content)
                outfile.write('\n\n')  # Add spacing between documents

# Script execution ends here
# The combined markdown document now exists at the path specified by 'output_file'



