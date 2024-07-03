import argparse
import markdown
import os
import logging
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.tables import TableExtension

def convert_md_to_html(md_content):
    extensions = [
        'extra',
        CodeHiliteExtension(css_class='highlight'),
        FencedCodeExtension(),
        TableExtension(),
        'toc',
        'nl2br',
    ]
    
    html = markdown.markdown(md_content, extensions=extensions)
    return html

def main():
    parser = argparse.ArgumentParser(description="Convert Markdown files to HTML")
    parser.add_argument("--source_dir", help="Path to the markdown files", required=True)
    parser.add_argument("--target_dir", help="Output path for the rendered HTML", required=True)
    args = parser.parse_args()

    logging.basicConfig(format='%(levelname)s: [%(asctime)s] %(message)s', level=logging.INFO)

    source_dir = os.path.abspath(args.source_dir)
    target_dir = os.path.abspath(args.target_dir)

    logging.info(f"Source directory: {source_dir}")
    logging.info(f"Target directory: {target_dir}")

    # Ensure target directory exists
    os.makedirs(target_dir, exist_ok=True)

    # Read prefix and suffix HTML
    try:
        with open(os.path.join(source_dir, "prefix.html"), "r") as f:
            prefix_html = f.read()
        with open(os.path.join(source_dir, "suffix.html"), "r") as f:
            suffix_html = f.read()
    except FileNotFoundError as e:
        logging.error(f"Error reading prefix or suffix file: {e}")
        return

    # Copy CSS file to target directory
    css_source = os.path.join(source_dir, "..", "css", "styles.css")
    css_target = os.path.join(target_dir, "css")
    os.makedirs(css_target, exist_ok=True)
    try:
        with open(css_source, "r") as source_file, open(os.path.join(css_target, "styles.css"), "w") as target_file:
            target_file.write(source_file.read())
        logging.info(f"Copied CSS file to {css_target}")
    except FileNotFoundError:
        logging.error(f"CSS file not found: {css_source}")

    for filename in os.listdir(source_dir):
        if filename.endswith(".md"):
            md_file = os.path.join(source_dir, filename)
            html_file = os.path.join(target_dir, filename.replace(".md", ".html"))
            
            try:
                with open(md_file, 'r', encoding='utf-8') as file:
                    md_content = file.read()
                    html_content = convert_md_to_html(md_content)
                
                with open(html_file, 'w', encoding='utf-8') as writer:
                    writer.write(prefix_html + "\n")
                    writer.write(html_content)
                    writer.write("\n" + suffix_html)
                
                logging.info(f"Converted {filename} to HTML")
            except Exception as e:
                logging.error(f"Error processing {filename}: {e}")

    logging.info("Conversion completed")

if __name__ == "__main__":
    main()