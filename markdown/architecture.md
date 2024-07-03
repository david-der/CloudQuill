File 2: `markdown/cloudquill-architecture.md`

```markdown
# CloudQuill Architecture

This page describes the architecture of CloudQuill, our static site generator. If you haven't seen our main page yet, check out the [Welcome to CloudQuill](welcome-to-cloudquill.md) page first.

## Components

CloudQuill consists of several key components:

1. Markdown Parser
2. HTML Generator
3. CSS Styler
4. Media Manager
5. AWS Deployer

### 1. Markdown Parser

The Markdown parser uses the Python `markdown` library to convert `.md` files into HTML. It supports various extensions for enhanced functionality.

Example usage:

```python
import markdown

with open('input.md', 'r') as f:
    md_content = f.read()

html_content = markdown.markdown(md_content, extensions=['extra', 'codehilite'])
```

### 2. HTML Generator

The HTML generator takes the parsed Markdown and wraps it in a complete HTML structure, including:

- Proper DOCTYPE and HTML tags
- Meta tags for SEO
- Links to CSS stylesheets
- Any necessary JavaScript

### 3. CSS Styler

CloudQuill uses a custom CSS file to style the generated HTML. Here's a sample of our CSS:

```css
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.6;
    color: #333;
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
}

h1, h2, h3 {
    color: #2c3e50;
}

code {
    background-color: #f4f4f4;
    padding: 2px 4px;
    border-radius: 4px;
}
```

### 4. Media Manager

The Media Manager handles all images and other media files. It ensures that media is properly referenced and uploaded to the correct S3 bucket.

![CloudQuill Media Flow](https://media.yourdomain.com/cloudquill-media-flow.png)

### 5. AWS Deployer

The AWS Deployer uses the AWS CLI to sync the generated HTML and media files to their respective S3 buckets. It also handles CloudFront invalidation for immediate updates.

## Workflow

1. Write content in Markdown
2. Run CloudQuill build process
3. Review generated HTML locally
4. Deploy to AWS with a single command

Ready to create your first post? Head back to our [Welcome Page](welcome-to-cloudquill.md) to get started!