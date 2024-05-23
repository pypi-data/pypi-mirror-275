from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks import AbsTaskClassification, MultilingualTask

_LANGUAGES = {
    "af": ["afr-Latn"],
    "am": ["amh-Ethi"],
    "ar": ["ara-Arab"],
    "az": ["aze-Latn"],
    "bn": ["ben-Beng"],
    "cy": ["cym-Latn"],
    "da": ["dan-Latn"],
    "de": ["deu-Latn"],
    "el": ["ell-Grek"],
    "en": ["eng-Latn"],
    "es": ["spa-Latn"],
    "fa": ["fas-Arab"],
    "fi": ["fin-Latn"],
    "fr": ["fra-Latn"],
    "he": ["heb-Hebr"],
    "hi": ["hin-Deva"],
    "hu": ["hun-Latn"],
    "hy": ["hye-Armn"],
    "id": ["ind-Latn"],
    "is": ["isl-Latn"],
    "it": ["ita-Latn"],
    "ja": ["jpn-Jpan"],
    "jv": ["jav-Latn"],
    "ka": ["kat-Geor"],
    "km": ["khm-Khmr"],
    "kn": ["kan-Knda"],
    "ko": ["kor-Kore"],
    "lv": ["lav-Latn"],
    "ml": ["mal-Mlym"],
    "mn": ["mon-Cyrl"],
    "ms": ["msa-Latn"],
    "my": ["mya-Mymr"],
    "nb": ["nob-Latn"],
    "nl": ["nld-Latn"],
    "pl": ["pol-Latn"],
    "pt": ["por-Latn"],
    "ro": ["ron-Latn"],
    "ru": ["rus-Cyrl"],
    "sl": ["slv-Latn"],
    "sq": ["sqi-Latn"],
    "sv": ["swe-Latn"],
    "sw": ["swa-Latn"],
    "ta": ["tam-Taml"],
    "te": ["tel-Telu"],
    "th": ["tha-Thai"],
    "tl": ["tgl-Latn"],
    "tr": ["tur-Latn"],
    "ur": ["urd-Arab"],
    "vi": ["vie-Latn"],
    "zh-CN": ["cmo-Hans"],
    "zh-TW": ["cmo-Hant"],
}


class MassiveIntentClassification(MultilingualTask, AbsTaskClassification):
    fast_loading = True
    metadata = TaskMetadata(
        name="MassiveIntentClassification",
        dataset={
            "path": "mteb/amazon_massive_intent",
            "revision": "4672e20407010da34463acc759c162ca9734bca6",
        },
        description="MASSIVE: A 1M-Example Multilingual Natural Language Understanding Dataset with 51 Typologically-Diverse Languages",
        reference="https://arxiv.org/abs/2204.08582#:~:text=MASSIVE%20contains%201M%20realistic%2C%20parallel,diverse%20languages%20from%2029%20genera.",
        category="s2s",
        type="Classification",
        eval_splits=["validation", "test"],
        eval_langs=_LANGUAGES,
        main_score="accuracy",
        date=None,
        form=None,
        domains=None,
        task_subtypes=None,
        license=None,
        socioeconomic_status=None,
        annotations_creators=None,
        dialect=None,
        text_creation=None,
        bibtex_citation=None,
        n_samples={"validation": 2033, "test": 2974},
        avg_character_length={"validation": 34.8, "test": 34.6},
    )
