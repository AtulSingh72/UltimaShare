from flask import Blueprint, render_template

share_page = Blueprint(
    "share_page", __name__, template_folder="./templates", url_prefix="/share_page", static_folder="./static"
)


@share_page.get("/")
def get_share_page_ui():
    return render_template("index.html")
