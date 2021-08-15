""" 
Function that translates English text to French
"""

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def englishtofrench(text):
    """
    Translates text argument (English) to French
    """
    url_lt='https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/487e0f55-a865-485d-9cea-8c7123dfe4af'
    apikey_lt='Beey-FgdyMLBEKQtweSR-8hQn5eVPmNUuDKzCP9_6QS_'
    version_lt='2018-05-01'

    # API data
    authenticator = IAMAuthenticator(apikey_lt)
    language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
    language_translator.set_service_url(url_lt)
    
    # Translation
    translation_response = language_translator.translate(
        text=text, model_id='en-fr')
    
    return translation_response.get_result()\
        ['translations'][0]['translation']

if __name__ == "__main__":
    example = "Mi dad has a hairy butt"
    print(example)

    translation = englishtofrench(example)
    print(translation)

