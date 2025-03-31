import typer
import os
from rich.console import Console
from rich.table import Table
from rich.prompt import Confirm
import shutil
from importlib import resources

app = typer.Typer(help="Project Template CLI - Create new projects from templates")
console = Console()

def get_templates():
    """Return only the specific template directories we want to expose"""
    valid_templates = ["MonsterUI", "Tailwind"]
    with resources.path("project_templates_cli", "templates") as template_dir:
        return [d for d in valid_templates if os.path.isdir(os.path.join(template_dir, d))]

@app.command()
def list():
    """List all available project templates"""
    templates = get_templates()
    table = Table(title="Available Templates")
    table.add_column("Template Name", style="cyan")
    table.add_column("Description", style="green")
    
    descriptions = {
        "MonsterUI": "A modern UI template with Monster UI components",
        "Tailwind": "A template with Tailwind CSS setup"}
    
    for template in templates:
        description = descriptions.get(template, "A project template")
        table.add_row(template, description)
    
    console.print(table)

@app.command()
def create(
    template: str = typer.Argument(..., help="Name of the template to use"),
    project_name: str = typer.Argument(..., help="Name of your new project"),
):
    """Create a new project from a template"""
    templates = get_templates()
    
    if template not in templates:
        console.print(f"[red]Error: Template '{template}' not found.[/red]")
        console.print("\nAvailable templates:")
        for t in templates: console.print(f"  - {t}")
        raise typer.Exit(1)
    
    if os.path.exists(project_name):
        if not Confirm.ask(f"Directory '{project_name}' already exists. Overwrite?"):
            raise typer.Exit()
    
    with resources.path("project_templates_cli", "templates") as template_dir:
        source_path = os.path.join(template_dir, template)
        console.print(f"[green]Creating new project '{project_name}' from template '{template}'...[/green]")
        shutil.copytree(source_path, project_name, dirs_exist_ok=True)
        console.print(f"[green]✓ Project created successfully![/green]")

if __name__ == "__main__":
    app() 