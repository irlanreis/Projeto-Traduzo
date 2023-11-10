from flask import Blueprint, render_template, request

from deep_translator import GoogleTranslator
from models.language_model import LanguageModel
from models.history_model import HistoryModel


translate_controller = Blueprint("translate_controller", __name__)


# Reqs. 4 e 5
@translate_controller.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template(
            "index.html",
            languages=LanguageModel.list_dicts(),
            text_to_translate="O que deseja traduzir?",
            translate_from="pt",
            translate_to="en",
            translated="What do you want to translate?",
        )
    elif request.method == "POST":
        languages = LanguageModel.list_dicts()

        text_to_translate = request.form.get("text-to-translate")
        translate_from = request.form.get("translate-from")
        translate_to = request.form.get("translate-to")

        translator_google = GoogleTranslator(
            source="auto", target=translate_to
        ).translate(text_to_translate)

        translated = translator_google

        history_dict = {
            "text_to_translate": text_to_translate,
            "translate_from": translate_from,
            "translate_to": translate_to,
        }
        HistoryModel(history_dict).save()

        return render_template(
            "index.html",
            languages=languages,
            text_to_translate=text_to_translate,
            translate_from=translate_from,
            translate_to=translate_to,
            translated=translated,
        )


# Req. 6
@translate_controller.route("/reverse", methods=["POST"])
def reverse():
    languages = LanguageModel.list_dicts()
    translate_from = request.form.get("translate-to")
    translate_to = request.form.get("translate-from")
    translated = request.form.get("text-to-translate")
    translator_google = GoogleTranslator(
        source="auto", target=translate_from
    ).translate(translated)
    text_to_translate = translator_google or ""
    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated,
    )
