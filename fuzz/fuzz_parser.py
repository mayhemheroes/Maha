#!/usr/local/bin/python3
import atheris
import sys

with atheris.instrument_imports():
    from maha.parsers.functions import parse
    from maha.cleaners.functions import normalize_small_alef

@atheris.instrument_func
def TestOneInput(data):
    if len(data) < 1:
        return
    fdp = atheris.FuzzedDataProvider(data)
    option = fdp.ConsumeBytes(1)[0]
    input = fdp.ConsumeString(len(data) - 1)
    if option % 10 == 0:
        parse(input, arabic=True)
    if option % 10 == 1:
        parse(input, english=True)
    if option % 10 == 2:
        parse(input, harakat=True)
    if option % 10 == 3:
        parse(input, all_harakat=True)
    if option % 10 == 4:
        parse(input, punctuations=True)
    if option % 10 == 5:
        parse(input, arabic_numbers=True)
    if option % 10 == 6:
        parse(input, english_numbers=True)
    if option % 10 == 7:
        parse(input, arabic_punctuations=True)
    if option % 10 == 8:
        parse(input, arabic_ligatures=True)
    if option % 10 == 9:
        parse(input, arabic_letters=True)

# atheris.instrument_all()
atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()