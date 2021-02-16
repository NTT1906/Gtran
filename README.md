<div align="center">
	<h2>Gtran</h2>
</div>
<div align=center>
	<a href="https://github.com/NTT1906/Gtran">
		<img src="https://raw.githubusercontent.com/NTT1906/Gtran/main/logo.png">
	</a>
	<div align=left>
		<a href="https://discord.gg/emSrPFn">
		        <img src="https://img.shields.io/discord/598415377478844442?color=blue&label=discord&style=plastic" alt="discord">
		</a>
	<br><br>
	</div>
</div>

- A free and unlimited Google translator.

<div align="center">
	<h2>Installation</h2>
</div>

 ```
pip install translate
```
 
 or you can download the source and run
 
```python
python setup.py install
```

<div align="center">
	<h2>How to use as a python module?</h2>
</div>

```python
from gtrans.gtrans import Gtran
translator = Gtran()
```

<div align="center">
	<h2>How to translate?</h2>
</div>

#### Default translate:
> Every language to English
 
```python
text = "こんにちは"
out = translator.translate(text=text)
print(out)
```
```
Hello
```

#### Custom translate:
> Every language to target language

```python 
to_lang = "en"
text = "こんにちは"
out = translator.translate(to_lang=target, text = text)
print(out)
```
```
Hello
```

<div align="center">
	<h2>How to detect language?</h2>
</div>

#### Return Id:

```python
text = "Hello"
translator.detectId(text=text)
```
```
en
```

#### Return name:

```python
text = "Hello"
translator.detect(text=text)
```
```
English
```

<div align="center">
	<h2>Dependant</h2>
	<a href="https://pypi.org/project/pycurl/">
		Pycurl
	</a>
	<br>
	<a href="https://pypi.org/project/urllib3/">
		Urllib3
	</a>
</div>

<div align="center">
	<h2>Language ids</h2>

|`Language` | `Id` |
| :---: | :---: |
|Afrikaans | af|
|Albanian | sq|
|Amharic | am|
|Arabic | ar|
|Armenian | hy|
|Azerbaijani | az|
|Basque | eu|
|Belarusian | be|
|Bengali | bn|
|Bosnian | bs|
|Bulgarian | bg|
|Catalan | ca|
|Cebuano | ceb (ISO-639-2)|
|Chinese (Simplified) | zh-CN or zh|
|Chinese (Traditional) | zh-TW|
|Corsican | co|
|Croatian | hr|
|Czech | cs|
|Danish | da|
|Dutch | nl|
|English | en|
|Esperanto | eo|
|Estonian | et|
|Finnish | fi|
|French | fr|
|Frisian | fy|
|Galician | gl|
|Georgian | ka|
|German | de|
|Greek | el|
|Gujarati | gu|
|Haitian Creole | ht|
|Hausa | ha|
|Hawaiian | haw (ISO-639-|
|Hebrew | he or iw|
|Hindi | hi|
|Hmong | hmn (ISO-639-2)|
|Hungarian | hu|
|Icelandic | is|
|Igbo | ig|
|Indonesian | id|
|Irish | ga|
|Italian | it|
|Japanese | ja|
|Javanese | jv|
|Kannada | kn|
|Kazakh | kk|
|Khmer | km|
|Kinyarwanda | rw|
|Korean | ko|
|Kurdish | ku|
|Kyrgyz | ky|
|Lao | lo|
|Latin | la|
|Latvian | lv|
|Lithuanian | lt|
|Luxembourgish | lb|
|Macedonian | mk|
|Malagasy | mg|
|Malay | ms|
|Malayalam | ml|
|Maltese | mt|
|Maori | mi|
|Marathi | mr|
|Mongolian | mn|
|Myanmar (Burmese) | my|
|Nepali | ne|
|Norwegian | no|
|Nyanja (Chichewa) | ny|
|Odia (Oriya) | or|
|Pashto | ps|
|Persian | fa|
|Polish | pl|
|Portuguese (Portugal Brazil) | pt|
|Punjabi | pa|
|Romanian | ro|
|Russian | ru|
|Samoan | sm|
|Scots Gaelic | gd|
|Serbian | sr|
|Sesotho | st|
|Shona | sn|
|Sindhi | sd|
|Sinhala (Sinhalese) | si|
|Slovak | sk|
|Slovenian | sl|
|Somali | so|
|Spanish | es|
|Sundanese | su|
|Swahili | sw|
|Swedish | sv|
|Tagalog (Filipino) | tl|
|Tajik | tg|
|Tamil | ta|
|Tatar | tt|
|Telugu | te|
|Thai | th|
|Turkish | tr|
|Turkmen | tk|
|Ukrainian | uk|
|Urdu | ur|
|Uyghur | ug|
|Uzbek | uz|
|Vietnamese | vi|
|Welsh | cy|
|Xhosa | xh|
|Yiddish | yi|
|Yoruba | yo|
|Zulu | zu|

</div>
<div align=center>
	<a href="https://github.com/NTT1906/Gtran">
		<img src="https://raw.githubusercontent.com/NTT1906/Gtran/main/banner.jpg">
	</a>
</div>