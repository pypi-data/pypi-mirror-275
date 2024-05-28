# Name Extractor
## Name Extractor is a small AI program that analyzes text for characters and retrieves their full names and genders

### How to use

#### Install NameExtractor: 
```bash
pip install NameExtractor
```

#### Use Name Extractor in your code:

```python
import NameExtractor
extractor = NameExtractor.NameExtractor("John Robert Smith and Mary Anne Johnson went to the park.")

#install NLTK resources
extractor.install()

#extract names
extracted_names = extractor.extract_names()

#determine genders
names_with_genders = extractor.determine_genders(extracted_names)

for name in names_with_genders:
    middlenames_str = ', '.join(name.middlenames) + ', ' if name.middlenames else ''
    print(f"Name: {name.text}, Gender: {name.gender}, Last Name: {name.surname}, Middle Names: {middlenames_str}")

```

### More features coming soon!
