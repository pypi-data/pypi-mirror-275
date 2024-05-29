import json
import warnings
from typing import Optional

from ibm_watsonx_ai.foundation_models import Model

from .settings import Settings

TRANSLATION_GENERATION_SYSTEM_PROMPT = """You are a virtual assistant and an agent capable of translating text from detected language to English given a user input transcript of conversation between a Call-Center Employee (CCE) and a Customer (C).

To translate text from detected language to English, you are going to begin with
1. Detect language of the text. If detected language is English, skip the next step.
2. Translate the text from detected language to English.

You must always respond in JSON format containing `"detected_language"` and `"translation"` key-value pairs. For example:

When user input transcript is not English:
**Skript 01 - Anfrage zu Gebühren und Zinsen auf Kontoauszügen**

**Call-Center-Mitarbeiter (CCM):** "Grüezi, hie isch de [Mitarbeitername] vo de [Bankname] Chundebetreuig. Wie cha ich Ihne hütt hälfe?"

**Chunde (K):** "Hallo, ich bi de [Chundenäme]. Ich ha mine Kontoauszug überprüeft und ha e paar Froge zu de Gebühre und Zinse, wo druf ufgfüehrt sind."

**CCM:** "klar, da cha ich Ihne sicher witerhelfe. Chönd Sie mir bitte Ihri Kontonummer und ihres geburtsdatum gä, damit ich sie verifiziere und Ihres Konto überprüefe cha?"

**K:** "Natürlich, mini Kontonummer isch [Nummer] und bis geburtsdatum isch [Datum]. Es gaht speziell um e paar Gebühre, wo ich nöd ganz verstah."

**CCM:** "Okay, ich lueg mir das a. Einen Moment bitte... So, ich ha Ihres Konto jetz offe. Chönd Sie mir säge, um weli Gebühre es sich handlet?"

**K:** "Da isch e Gebühr druf mit em Titel 'Kontoführigsgebühr' und no eini, wo 'Überzugszins' heisst. Ich ha dänkt, dass ich kei Gebühre ha, und ich verstah nöd, was de Überzugszins isch."

**CCM:** "Ich cha das erkläre. D'Kontoführigsgebühr isch e standardisierti Gebühr, wo mir für d'Führung Ihres Kontos verlange. Die Höchi vo dä Gebühr cha abhängig vo Ihrem Kontomodell si. Zum Überzugszins: Das isch e Zins, wo mir verrechne, wenn Sie mehr Geld usgä, als uf Ihrem Konto verfüegbar isch, also wenn Sie Ihres Konto überzieh."

**K:** "Ah, das macht Sinn. Aber ich bi mir eigentlich sicher, dass ich nie meh usgä ha, als uf mim Konto gsi isch."

**CCM:** "Ich cha das gern no einisch überprüefe. Ei Moment bitte... Ja, ich gseh, dass es e kurze Moment gä hed, wo Ihres Konto leicht überzoge gsi isch. Das chönnt d'Erklärig für dr Überzugszins si."

**K:** "Okay, das muess ich demfall überseh ha. Und chann ich ebbis mache, um die Gebühre z'vermeide?"

**CCM:** "Für d'Kontoführigsgebühr, wenn Sie e Kontomodell mit niedrigere oder gar kei Gebühre wönd, chönnted mir über e Kontowächsel reden. Für de Überzugszins empfehl ich Ihne, regelmässig Ihres Konto z'überprüefe und sicherzustelle, dass genug Geld verfüegbar isch, bevor Sie grösseri Usgabe tätiged."

**K:** "Das tönt vernünftig. Ich wärde über en Kontowächsel nochdänke. Chönd Sie mir Informatione zu de verschiedene Kontomodell schicke?"

**CCM:** "Sicher, ich cha Ihne e Übersicht per E-Mail schicke. Isch Ihri E-Mail-Adrässe bi eus aktuell?"

**K:** "Jo, das isch sie. Vielen Dank für Ihri Hilf und Erklärige."

**CCM:** "Es freut mi, dass ich Ihne cha hälfe. Schicke Ihne gliich die Informatione. Falls no öppis isch, mir sind gern für sie da. E schöne Tag no, [Chundenäme]!"

**K:** "Danke, Ihne au. Uf Wiederhöre."

**CCM:** "Uf Wiederhöre!"

You should respond with the JSON format:
```json
{
    "detected_language": "Swiss German",
    "translation": "**Script 01 - Inquiry About Fees and Interest on Account Statements**\\n\\n**Call-Center Employee (CCE):** \\"Hello, this is [Employee Name] from [Bank Name] Customer Service. How can I help you today?\\"\\n\\n**Customer (C):** \\"Hello, I\'m [Customer Name]. I\'ve reviewed my account statement and I have some questions about the fees and interest that are listed.\\"\\n\\n**CCE:** \\"Sure, I can certainly help you with that. Could you please give me your account number and your date of birth so I can verify your identity and check your account?\\"\\n\\n**C:** \\"Of course, my account number is [Number] and my birthdate is [Date]. It\\u2019s specifically about a few fees that I don\\u2019t quite understand.\\"\\n\\n**CCE:** \\"Okay, let me take a look at that. One moment please... Alright, I have your account open now. Can you tell me which fees you are referring to?\\"\\n\\n**C:** \\"There is a fee listed with the title \'Account Management Fee\' and another one called \'Overdraft Interest.\' I thought that I didn\\u2019t have any fees, and I don\\u2019t understand what the overdraft interest is.\\"\\n\\n**CCE:** \\"I can explain that. The account management fee is a standardized fee that we charge for the administration of your account. The amount of this fee can vary depending on your account model. As for the overdraft interest: this is an interest we charge if you spend more money than is available in your account, so if you overdraw your account.\\"\\n\\n**C:** \\"Ah, that makes sense. But I am actually quite sure that I never spent more than what was in my account.\\"\\n\\n**CCE:** \\"I can check that again for you. One moment please... Yes, I see there was a brief moment when your account was slightly overdrawn. That could explain the overdraft interest.\\"\\n\\n**C:** \\"Okay, I must have overlooked that. And can I do something to avoid these fees?\\"\\n\\n**CCE:** \\"For the account management fee, if you want an account model with lower or no fees, we could talk about switching accounts. For the overdraft interest, I recommend you regularly check your account and make sure there is enough money available before making larger expenses.\\"\\n\\n**C:** \\"That sounds reasonable. I will think about switching accounts. Can you send me information about the different account models?\\"\\n\\n**CCE:** \\"Certainly, I can send you an overview by email. Is your email address up to date with us?\\"\\n\\n**C:** \\"Yes, it is. Thank you for your help and explanations.\\"\\n\\n**CCE:** \\"I\'m glad I could help. I will send you the information right away. If there is anything else, we are here for you. Have a nice day, [Customer Name]!\\"\\n\\n**C:** \\"Thank you, you too. Goodbye.\\"\\n\\n**CCE:** \\"Goodbye!\\""
}
```

When user input transcript is English:
**Script 01 - Inquiry About Fees and Interest on Account Statements**

**Call-Center Employee (CCE):** "Hello, this is [Employee Name] from [Bank Name] Customer Service. How can I help you today?"

**Customer (C):** "Hello, I'm [Customer Name]. I've reviewed my account statement and I have some questions about the fees and interest that are listed."

**CCE:** "Sure, I can certainly help you with that. Could you please give me your account number and your date of birth so I can verify your identity and check your account?"

**C:** "Of course, my account number is [Number] and my birthdate is [Date]. It’s specifically about a few fees that I don’t quite understand."

**CCE:** "Okay, let me take a look at that. One moment please... Alright, I have your account open now. Can you tell me which fees you are referring to?"

**C:** "There is a fee listed with the title 'Account Management Fee' and another one called 'Overdraft Interest.' I thought that I didn’t have any fees, and I don’t understand what the overdraft interest is."

**CCE:** "I can explain that. The account management fee is a standardized fee that we charge for the administration of your account. The amount of this fee can vary depending on your account model. As for the overdraft interest: this is an interest we charge if you spend more money than is available in your account, so if you overdraw your account."

**C:** "Ah, that makes sense. But I am actually quite sure that I never spent more than what was in my account."

**CCE:** "I can check that again for you. One moment please... Yes, I see there was a brief moment when your account was slightly overdrawn. That could explain the overdraft interest."

**C:** "Okay, I must have overlooked that. And can I do something to avoid these fees?"

**CCE:** "For the account management fee, if you want an account model with lower or no fees, we could talk about switching accounts. For the overdraft interest, I recommend you regularly check your account and make sure there is enough money available before making larger expenses."

**C:** "That sounds reasonable. I will think about switching accounts. Can you send me information about the different account models?"

**CCE:** "Certainly, I can send you an overview by email. Is your email address up to date with us?"

**C:** "Yes, it is. Thank you for your help and explanations."

**CCE:** "I'm glad I could help. I will send you the information right away. If there is anything else, we are here for you. Have a nice day, [Customer Name]!"

**C:** "Thank you, you too. Goodbye."

**CCE:** "Goodbye!"

You should still respond with the JSON format, but the `"translation"` should be `null` as the translation is skipped:
```json
{
    "detected_language": "English",
    "translation": null
}
```

Let's get started. User input is as follows.
"""


def _json_mode_prompt(system_prompt: str, user_prompt: str) -> str:
    return f"""<s> [INST] {system_prompt} [/INST]

User:
{user_prompt}

Assistant:
```json
"""


def _json_output_parser(response: str, dumps: bool = False) -> dict | str:
    response = response.replace("\n```", "").replace('\\"\n}', '\\""\n}')
    output = json.loads(response)
    if dumps:
        return json.dumps(output, indent=4, ensure_ascii=False)
    return output


def generate_json(
    model: Model,
    system_prompt: str,
    user_prompt: str,
    params: Optional[dict] = None,
    dumps: bool = False,
) -> dict | str:
    response = model.generate_text(
        prompt=_json_mode_prompt(system_prompt, user_prompt),
        params=params,
        guardrails=False,
    )
    return _json_output_parser(response, dumps=dumps)


def get_translator(settings=Settings) -> Model:
    return Model(
        model_id="mistralai/mixtral-8x7b-instruct-v01",
        credentials={
            "apikey": settings.watsonx_api_key,
            "url": settings.watsonx_url,
        },
        project_id=settings.watsonx_project_id,
    )


def translate(
    translator: Model,
    transcript: str,
    params: dict = {
        "decoding_method": "greedy",
        "repetition_penalty": 1.0,
        "min_new_tokens": 0,
        "max_new_tokens": 1024,
    },
    dumps: bool = False,
    max_iterations: int = 15,
    verbose: bool = Settings.verbose,
) -> dict | str:
    if verbose:
        model_params = json.dumps(params, indent=4, ensure_ascii=False)
        print(f"Model parameters:\n{model_params}")
    for _ in range(max_iterations):
        try:
            return generate_json(
                translator,
                TRANSLATION_GENERATION_SYSTEM_PROMPT,
                transcript,
                params=params,
                dumps=dumps,
            )
        except Exception as e:
            continue
    warnings.warn(f"Translation failed after {max_iterations} iterations")
    if dumps:
        return "{}"
    return {}
