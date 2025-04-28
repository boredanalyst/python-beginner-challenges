## This is sample glossary made using Python dictionaries


python_terms = {
    "list" : "An ordered collection of items that allows duplication.",
    "set" : "An unordered collection of items that does not allow duplication.",
    "variable" :"An element that stores data using a label.",
    "string" : "A data type composed of alphanumeric characters."
}

for term in python_terms.keys():
    print(f'{term.upper()} : {python_terms[term]}')