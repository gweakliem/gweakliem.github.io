# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "click",
# ]
# ///

import click
import datetime
import re
import subprocess
from pathlib import Path
from typing import Optional, List
from urllib.parse import urlparse


def slugify(text: str) -> str:
    """Convert text to URL-friendly slug."""
    # Convert to lowercase and replace spaces/special chars with dashes
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", text.lower())
    # Remove leading/trailing dashes
    slug = slug.strip("-")
    # Truncate to 60 chars
    return slug[:60]


def create_filename(title: str, date: datetime.date) -> str:
    """Generate Jekyll-compatible filename from title and date."""
    return f"{date.strftime('%Y-%m-%d')}-{slugify(title)}.md"


def format_categories(categories: Optional[str]) -> List[str]:
    """Format category string into list, replacing spaces with underscores."""
    if not categories:
        return []
    return [cat.replace(" ", "_").strip() for cat in categories.split(",")]


def create_front_matter(
    title: str, categories: List[str], tags: List[str], draft: bool
) -> str:
    """Generate Jekyll front matter."""
    draft_str = f"published: {not draft}"
    category_str = f"\ncategories: [{', '.join(categories)}]" if categories else ""
    tag_str = f"\ntags: [{'  -'.join(tags)}]" if tags else ""
    return f"""---
title: "{title}"{category_str}{tag_str}
date: {datetime.date.today().isoformat()}
{draft_str}
---
"""


def create_link_content(link: str, attrib: str, via: Optional[str] = None) -> str:
    """Generate link post content."""
    via_html = f' <small>(<a href="{via}">via</a>)</small>' if via else ""
    return f'<a href="{link}">{attrib}</a>{via_html}\n'


@click.command()
@click.argument("title")
@click.option("-d", "--draft", is_flag=True, help="Create a draft post")
@click.option("-y", "--yes", is_flag=True, help="Skip confirmation")
@click.option("-t", "--til", is_flag=True, help="Create a TIL post")
@click.option("-l", "--link", help="URL for link post")
@click.option("-a", "--attrib", help="name to attribute to link post")
@click.option("-v", "--via", help="Via link")
@click.option("-g", "--tags", help="Comma-separated tags")
def main(
    title: str,
    draft: bool,
    yes: bool,
    til: bool,
    link: str,
    attrib: str,
    via: str,
    tags: Optional[str],
) -> None:
    """Create a new Jekyll blog post."""
    # Process categories
    tags = format_categories(tags)
    cats = []
    if til:
        cats = ["til"] + cats
    if link:
        cats = ["links"] + cats

    # Generate filename and full path
    today = datetime.date.today()
    filename = create_filename(title, today)

    posts_dir = Path(__file__).parent / "_posts"
    posts_dir.mkdir(exist_ok=True)
    full_path = posts_dir / filename

    # Create content
    content = create_front_matter(title, cats, tags, draft)
    if link:
        if not attrib:
            # Try to get domain as author if not provided
            domain = urlparse(link).netloc
            attrib = domain.replace("www.", "")
        content += "\n" + create_link_content(link, attrib, via)

    # Show preview
    if not yes:
        click.echo("\nPost Preview:")
        click.echo(f"Filename: {filename}")
        click.echo("\nContent:")
        click.echo(content)
        if not click.confirm("\nCreate post?"):
            click.echo("Cancelled")
            return

    # Write file
    full_path.write_text(content)
    click.echo(f"\nCreated post: {full_path}")

    if not draft:
        try:
            subprocess.run(["git", "add", str(full_path)], check=True)
            click.echo("File staged in git")
        except subprocess.CalledProcessError:
            click.echo("Warning: Failed to stage file in git")
        except FileNotFoundError:
            click.echo("Warning: Git not found, file not staged")


if __name__ == "__main__":
    main()
