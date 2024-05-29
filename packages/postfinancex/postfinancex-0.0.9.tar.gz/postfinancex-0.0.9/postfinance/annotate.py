import json
import warnings
from typing import Optional

from ibm_watsonx_ai.foundation_models import Model

from .settings import Settings

ANNOTATION_GENERATION_SYSTEM_PROMPT = """You are a virtual assistant that only outputs JSON and an agent capable of annotating text given a user input transcript of conversation between a Call-Center Employee (CCE) and a Customer (C).

To annotate the transcript, you are going to begin with:
1. Summarize the transcript in one sentence.
2. Extract the Customer's requests, questions or problems as well as the Call-Center Employee's corresponding response given the transcript.
3. Cite the related content in the transcript for each extraction.
4. Extraction from the Customer's messages should be classified into one of three classes: `"request"`, `"question"`, `"problem"`. 

Definitions of these three classes `"request"`, `"question"`, `"problem"` are as follows:
Class name: `"request"`
Description: The customer is requesting something. They might say they are needing information about something to be sent to their email address or mail address.

Class name: `"question"`
Description: The customer is asking a technical question or a how-to question about the products or services.

Class name: `"problem"`
Description: The customer is describing a problem they are having. They might say they are trying something, but it's not working. They might say they are getting an error or unexpected results.

You must always respond in JSON format containing `"summarization"` and `"extraction"` key-value pairs. For example:

When user input transcript is:
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

You should respond with the JSON format:
```json
{
    "summary": "The customer called to inquire about unexpected fees and interest charges on their bank account statement, and the call-center employee explained the charges and discussed potential ways to avoid them in the future.",
    "details": [
        {
            "type": "question",
            "role": "customer",
            "content": "The customer questioned the \'Account Management Fee\' and \'Overdraft Interest\' listed on their account statement, expressing confusion over their existence since they believed their account should not have any fees and they had not overspent their account balance.",
            "citation": "\\"There is a fee listed with the title \'Account Management Fee\' and another one called \'Overdraft Interest.\' I thought that I didn’t have any fees, and I don’t understand what the overdraft interest is.\\"",
            "has_response": {
                "type": "response",
                "role": "call-center employee",
                "content": "The call-center employee clarified that the \'Account Management Fee\' is a standard fee for account administration, dependent on the account model, and 'Overdraft Interest' is charged when the account balance goes negative, even briefly.",
                "citation": "\\"The account management fee is a standardized fee that we charge for the administration of your account. The amount of this fee can vary depending on your account model. As for the overdraft interest: this is an interest we charge if you spend more money than is available in your account, so if you overdraw your account.\\""
            }
        },
        {
            "type": "problem",
            "role": "customer",
            "content": "The customer was certain they never exceeded their account balance and needed clarification on the recorded overdraft.",
            "citation": "\\"Ah, that makes sense. But I am actually quite sure that I never spent more than what was in my account.\\"",
            "has_response": {
                "type": "response",
                "role": "call-center employee",
                "content": "Upon further review, the employee confirmed that the customer's account was indeed briefly overdrawn, which led to the overdraft charge.",
                "citation": "\\"I can check that again for you. One moment please... Yes, I see there was a brief moment when your account was slightly overdrawn. That could explain the overdraft interest.\\""
            }
        },
        {
            "type": "question",
            "role": "customer",
            "content": "The customer asked for ways to avoid these fees in the future.",
            "citation": "\\"Okay, I must have overlooked that. And can I do something to avoid these fees?\\"",
            "has_response": {
                "type": "response",
                "role": "call-center employee",
                "content": "The employee suggested regularly monitoring the account to avoid overdrafts and discussed the possibility of switching to a different account model to reduce or eliminate the management fee.",
                "citation": "\\"For the account management fee, if you want an account model with lower or no fees, we could talk about switching accounts. For the overdraft interest, I recommend you regularly check your account and make sure there is enough money available before making larger expenses.\\""
            }
        },
        {
            "type": "request",
            "role": "customer",
            "content": "The customer requested information about different account models that might not carry the same fees.",
            "citation": "\\"That sounds reasonable. I will think about switching accounts. Can you send me information about the different account models?\\"",
            "has_response": {
                "type": "response",
                "role": "call-center employee",
                "content": "The employee agreed to send information on different account models via email and confirmed that they had the correct email address on file.",
                "citation": "\\"Certainly, I can send you an overview by email. Is your email address up to date with us?\\""
            }
        }
    ]
}
```

Let's get started. User input is as follows.
"""


def _json_mode_prompt(system_prompt: str, user_prompt: str) -> str:
    return f"""<|begin_of_text|><|start_header_id|>system<|end_header_id|>

{system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>

{user_prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>```json"""


def _json_output_parser(response: str, dumps: bool = False) -> dict | str:
    response = response.replace("\n```", "")
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


def get_annotator(settings=Settings) -> Model:
    return Model(
        model_id="meta-llama/llama-3-70b-instruct",
        credentials={
            "apikey": settings.watsonx_api_key,
            "url": settings.watsonx_url,
        },
        project_id=settings.watsonx_project_id,
    )


def annotate(
    annotator: Model,
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
                annotator,
                ANNOTATION_GENERATION_SYSTEM_PROMPT,
                transcript,
                params=params,
                dumps=dumps,
            )
        except Exception as e:
            continue
    warnings.warn(f"Annotation failed after {max_iterations} iterations")
    if dumps:
        return "{}"
    return {}
