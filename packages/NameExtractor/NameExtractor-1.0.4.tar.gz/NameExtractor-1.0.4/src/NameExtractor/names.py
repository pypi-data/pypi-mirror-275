import subprocess
from typing import List, Optional, Union
from dataclasses import dataclass
from downloaded import is_downloaded
import nltk
from nltk.corpus import names

import spacy
from spacy.tokens import Doc

nlp = spacy.load("en_core_web_sm")



@dataclass
class Name:
    text: str
    gender: Optional[str]
    firstname: str
    surname: str
    middlenames: Union[List[str], str]

class NameExtractor:
    def __init__(self, string: str):
        self.string = string

    @staticmethod
    def install():
        if not is_downloaded("names"):
            print("Downloading NLTK and spaCy resources...\n this will only happen the first time you run the script.")
            try:
                nltk.download("names")
                subprocess.run("p")
            except Exception as e:
                raise Exception("Failed to download NLTK resources\n"+str(e))
    def extract_names(self) -> List[Name]:
        doc: Doc = nlp(self.string)
        names = []
        for entity in doc.ents:
            if entity.label_ == "PERSON":
                name_parts = entity.text.split(" ")
                firstname = name_parts[0]
                surname = name_parts[-1]
                middlenames = name_parts[1:-1] if len(name_parts) > 2 else ""
                names.append(Name(entity.text, None, firstname, surname, middlenames))
        self.determine_genders(names)
        return names
    
    def determine_genders(self, names: List[Name]) -> None:
        male_names = set(nltk.corpus.names.words('male.txt'))
        female_names = set(nltk.corpus.names.words('female.txt'))

        for name in names:
            if any(name.firstname.lower() == male.lower() for male in male_names):
                name.gender = 'Male'
            elif any(name.firstname.lower() == female.lower() for female in female_names):
                name.gender = 'Female'
        return names

