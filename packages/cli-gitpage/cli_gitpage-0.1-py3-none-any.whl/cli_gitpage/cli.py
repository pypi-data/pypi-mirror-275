import click

about_text = """
Hi, I'm Debjit Mandal, currently pursuing B.Tech in Computer Science and Engineering at Kalinga Institute of
Industrial Technology, Bhubaneswar, Odisha, India. I have a passion for coding and I'm always looking to
improve my skills and knowledge. During my studies, I have gained experience in a variety of programming languages and
tools, including Java, Python, C/C++, HTML/CSS, JavaScript, Rust, and Go. I have also worked on various projects both
individually and as part of a team, which have helped me develop my skills in problem-solving, collaboration, and
project management. Aside from programming, I enjoy reading about new technologies and attending tech events
to learn from industry experts and network with like-minded Individuals.
"""

contact_info = """
GitHub: https://github.com/debjit-mandal
Facebook: https://www.facebook.com/iamdebjitmandal
LinkedIn: https://www.linkedin.com/in/debjit-mandal
X: https://www.x.com/imdebjitmandal
Fosstodon: https://fosstodon.org/@iamdebjitmandal
"""

skills_text = """
MY WORKS ARE BASED ON THE FOLLOWING:

- Java
- Python
- C
- C++
- GoLang
- Rust
- HTML
- CSS
- JavaScript
- SQL
- MongoDB
- Git/GitHub
- Flask
- Django
- Data Science
- Data Analytics
- AI & ML
"""

resume_link = "https://debjit-mandal.is-a.dev/assets/resume/Debjit's%20Resume.pdf"


@click.group()
def cli():
    pass


@cli.command()
def about():
    click.echo(about_text)


@cli.command()
def contact():
    click.echo(contact_info)


@cli.command()
def skills():
    click.echo(skills_text)


@cli.command()
def resume():
    click.echo(f"You can find my resume here: {resume_link}")


@cli.command()
@click.argument('page')
def navigate(page):
    pages = {
        'about': about_text,
        'contact': contact_info,
        'skills': skills_text,
        'resume': f"You can find my resume here: {resume_link}"
    }
    if page in pages:
        click.echo(pages[page])
    else:
        click.echo("Page not found")


@cli.command()
def list_pages():
    pages = ['about', 'contact', 'skills', 'resume']
    click.echo("Available pages:")
    for page in pages:
        click.echo(f"- {page}")


if __name__ == '__main__':
    cli()
