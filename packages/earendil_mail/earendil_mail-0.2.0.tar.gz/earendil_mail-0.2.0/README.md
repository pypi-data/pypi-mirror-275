# Eärendil

> Eärendil was a mariner\
> that tarried in Arvernien;\
> he built a boat of timber felled\
> in Nimbrethil to journey in;

Eärendil is a Markdown-based HTML email API written in Python. It allows users to draft an email message in Markdown 
and send it as a rich email viewable as both HTML and plaintext.

My primary motivation for creating this library was the lack of good options for sending rich emails with an alternative
plaintext message for recipients who may be using a dated email service. I think that providing a faithful 
alternative message is important, and that simply using the Markdown used to generate the HTML message as the 
alternative is insufficient. Markdown, while fairly human-readable compared to most markup languages, still contains 
redundant or unhelpful syntax that is better expressed differently in plaintext. For example, escape characters 
should be removed, as should heading and emphasis symbols.

## Features

* Renders Common Markdown messages into HTML.
* Renders a subset of Markdown into plaintext.
* Sends Markdown emails from either strings or files.

### Planned Features

* Support for rendering a greater subset of Markdown as plaintext.
* Support for attachments.

## Usage

To send Markdown-formatted emails using Eärendil, use either the `send_markdown_email`or `send_markdown_email_from_file`
functions. Here is an example that uses each:

```python
from pathlib import Path
from smtplib import SMTP

from earendil import send_markdown_email, send_markdown_email_from_file

sender_email = "sender@gmail.com"
password = "password"
recipient = "receiver@example.com"

subject = "Example Subject"
message_path = Path("/path/to/markdown.md")
with message_path.open("r") as file:
    message = file.read()

with SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender_email, password)
    # Here, you can either use:
    send_markdown_email(server, sender_email, recipient, subject, message)
    # or, alternatively:
    send_markdown_email_from_file(server, sender_email, recipient, subject, message_path)
```

## Installation

### Requirements

Eärendil can run on any version of Python since `3.6.2` (inclusive). It also depends on the `markdown` library.

### From PyPI

The easiest way to install Eärendil is to simply run the command `pip3 install earendil-mail`.

### From Source

Alternatively, Eärendil can be installed from source by cloning this repository. To do so, run the following commands:
```commandline
git clone https://github.com/ADSteele916/earendil
cd earendil
pip3 install .
```

## Uninstallation

To uninstall, simply run the command `pip3 uninstall earendil-mail`
