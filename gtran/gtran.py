from urllib.parse import urlencode
import pycurl
import json
from io import BytesIO

class Gtran():
	URL = "https://translate.google.com/translate_a/single?client=at&dt=t&dt=ld&dt=qca&dt=rm&dt=bd&dj=1&hl=vi_VN&ie=UTF-8&oe=UTF-8&inputm=2&otf=2&iid=b488e6e1-31f6-44da-9d44-8d44d0b14c5d"
	USERAGENT = "AndroidTranslate/5.3.0.RC02.130475354-53000263 5.1 phone TRANSLATE_OPM5_TEST_1"
	SUCCESS_RESPONSE_CODE = 200
	SOURCE = "auto"
	VALID_TRANSLATE_KEY = "sentences"
	VALID_DETECT_KEY = "src"
	EXPECTED_TRANSLATION_KEY = "trans"
	ENCODE_ID = "UTF-8"
	language_ids = {
	    "af": "Afrikaans",
	    "am": "Amharic",
	    "ar": "Arabic",
	    "az": "Azerbaijani",
	    "be": "Belarusian",
	    "bg": "Bulgarian",
	    "bn": "Bengali",
	    "bs": "Bosnian",
	    "ca": "Catalan",
	    "ceb": "Cebuano",
	    "co": "Corsican",
	    "cs": "Czech",
	    "cy": "Welsh",
	    "da": "Danish",
	    "de": "German",
	    "el": "Greek",
	    "en": "English",
	    "en_US": "English",
	    "eo": "Esperanto",
	    "es": "Spanish",
	    "et": "Estonian",
	    "eu": "Basque",
	    "fa": "Persian",
	    "fi": "Finnish",
	    "fr": "French",
	    "fy": "Frisian",
	    "ga": "Irish",
	    "gd": "Scots Gaelic",
	    "gl": "Galician",
	    "gu": "Gujarati",
	    "ha": "Hausa",
	    "haw": "Hawaiian",
	    "he": "Hebrew",
	    "hi": "Hindi",
	    "hmn": "Hmong",
	    "hr": "Croatian",
	    "ht": "Haitian Creole",
	    "hu": "Hungarian",
	    "hy": "Armenian",
	    "id": "Indonesian",
	    "ig": "Igbo",
	    "is": "Icelandic",
	    "it": "Italian",
	    "ja": "Japanese",
	    "jv": "Javanese",
	    "ka": "Georgian",
	    "kk": "Kazakh",
	    "km": "Khmer",
	    "kn": "Kannada",
	    "ko": "Korean",
	    "ku": "Kurdish",
	    "ky": "Kyrgyz",
	    "la": "Latin",
	    "lb": "Luxembourgish",
	    "lo": "Lao",
	    "lt": "Lithuanian",
	    "lv": "Latvian",
	    "mg": "Malagasy",
	    "mi": "Maori",
	    "mk": "Macedonian",
	    "ml": "Malayalam",
	    "mn": "Mongolian",
	    "mr": "Marathi",
	    "ms": "Malay",
	    "mt": "Maltese",
	    "my": "Myanmar (Burmese)",
	    "ne": "Nepali",
	    "nl": "Dutch",
	    "no": "Norwegian",
	    "ny": "Nyanja (Chichewa)",
	    "or": "Odia (Oriya)",
	    "pa": "Punjabi",
	    "pl": "Polish",
	    "ps": "Pashto",
	    "pt": "Portuguese (Portugal, Brazil)",
	    "ro": "Romanian",
	    "ru": "Russian",
	    "rw": "Kinyarwanda",
	    "sd": "Sindhi",
	    "si": "Sinhala (Sinhalese)",
	    "sk": "Slovak",
	    "sl": "Slovenian",
	    "sm": "Samoan",
	    "sn": "Shona",
	    "so": "Somali",
	    "sq": "Albanian",
	    "sr": "Serbian",
	    "st": "Sesotho",
	    "su": "Sundanese",
	    "sv": "Swedish",
	    "sw": "Swahili",
	    "ta": "Tamil",
	    "te": "Telugu",
	    "tg": "Tajik",
	    "th": "Thai",
	    "tk": "Turkmen",
	    "tl": "Tagalog (Filipino)",
	    "tr": "Turkish",
	    "tt": "Tatar",
	    "ug": "Uyghur",
	    "uk": "Ukrainian",
	    "ur": "Urdu",
	    "uz": "Uzbek",
	    "vi": "Vietnamese",
	    "vi_VN": "Vietnamese",
	    "xh": "Xhosa",
	    "yi": "Yiddish",
	    "yo": "Yoruba",
	    "zh": "Chinese (Simplified)",
	    "zh-CN": "Chinese (Simplified)",
	    "zh-TW": "Chinese (Traditional)",
	    "zu": "Zulu"
	}
	
	def __init__(self):
		pass
		
	def call(self, to_lang="en", text=""):
		if(text is None): return ""
		length = len(text) 
		if length <= 0: return ""
		if length >= 5000:
			raise Exception("Maximum number of characters is: 5000")
		
		buffer = BytesIO() #Write down the results
		fields = {
			'sl' : self.SOURCE,
			'tl' : to_lang,
			'q' : text
		}
		field_string = urlencode(fields)
		
		crl = pycurl.Curl()
		crl.setopt(crl.URL, self.URL)
		crl.setopt(crl.POST, len(fields))
		#crl.setopt(crl.PROXY, address)#To-do
		#crl.setopt(crl.PROXYTYPE, 2)#To-do
		crl.setopt(crl.POSTFIELDS, field_string)
		#crl.setopt(crl.ENCODING, self.ENCODE_ID) #It feels like this is a useless step
		crl.setopt(crl.SSL_VERIFYPEER, 1)
		crl.setopt(crl.SSL_VERIFYHOST, 2)
		crl.setopt(crl.USERAGENT, self.USERAGENT)
		crl.setopt(crl.WRITEFUNCTION, buffer.write)
		
		crl.perform()
		response_code = crl.getinfo(crl.RESPONSE_CODE) #Get response code
		crl.close()
		
		if(response_code != self.SUCCESS_RESPONSE_CODE):
			raise Exception("There was an error: " + str(response_code))
		return json.loads(buffer.getvalue().decode(self.ENCODE_ID)) #Return processed results into dictionary
	
	def translate(self, to_lang="en", text=""):
		results = self.call(to_lang, text)
		if results == "": return ""
		if self.VALID_TRANSLATE_KEY not in results:
			raise Exception("Something's wrong! Invalid result")
		return results[self.VALID_TRANSLATE_KEY][0][self.EXPECTED_TRANSLATION_KEY] #Returns results from dictionary
		
	def detect(self, text=""):
		return self.language_ids[self.detectId(text)]
	
	def detectId(self, text=""):
		results = self.call(text=text)
		if results == "": return "en"
		if self.VALID_DETECT_KEY not in results:
			raise Exception("Something's wrong! Invalid result")
		return results[self.VALID_DETECT_KEY] #Returns results from dictionary