from jinja2 import Environment, select_autoescape, PackageLoader

from src.main.email.settings import settings

jinja2_env = Environment(
    loader=PackageLoader("src.main.email", "templates/"),
    autoescape=select_autoescape()
)


def construct_content(content_topic: str, recipients: list[str]):
    template = jinja2_env.get_template(f"{content_topic}.html")
    content = None
    match content_topic:
        case "user_registration":
            content = {
                "subject": "Welcome to not-reddit!",
                "plainText": "",
                "html": template.render(recipients=recipients)
            }

    return content


def construct_recipients(recipients: list[str]):
    to_list = []
    for recipient in recipients:
        to_list.append({"address": recipient})
    return {"to": to_list}


def construct_message(content_topic: str, recipients: list[str]):
    return {
        "content": construct_content(content_topic=content_topic, recipients=recipients),
        "recipients": construct_recipients(recipients=recipients),
        "senderAddress": settings.EMAIL_SENDER_ADDRESS
    }
