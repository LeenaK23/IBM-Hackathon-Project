from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, KeywordsOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Authenticate
nlu = NaturalLanguageUnderstandingV1(
    version='2024-05-10',
    authenticator=IAMAuthenticator('pt1u11giScCw17q0HjEycBlwnLJVuUN9czJRdAtCSq6c')
)
nlu.set_service_url('https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/fd38e5b2-113d-4201-a754-5749a28f03f2')

# Analyze text
response = nlu.analyze(
    text="I have been sleeping only 4 hours a night and eating mostly fast food. I also feel bloated and fatigued.I have had chest pain and shortness of breath after minimal activity. I also feel dizzy sometimes.",
    features=Features(keywords=KeywordsOptions(limit=5))
).get_result()

print(response)
