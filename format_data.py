from datasets import load_dataset
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
import re

def to_roman(text):
    """Convert Devanagari text to casual Romanized Nepali."""
    if not text:
        return text
    roman = transliterate(text, sanscript.DEVANAGARI, sanscript.ITRANS)
    roman = roman.lower()
    roman = roman.replace('||', '.').replace('|', '.')
    roman = re.sub(r'\.{2,}', '.', roman)  # collapse repeated periods
    return roman.strip()

def format_example(example):
    instruction = to_roman(example['instruction'].strip())
    input_text = to_roman(example['input'].strip())
    output = to_roman(example['output'].strip())

    user_content = f"{instruction}\n\n{input_text}" if input_text else instruction

    return {
        "conversations": [
            {"role": "user", "content": user_content},
            {"role": "model", "content": output},
        ]
    }

if __name__ == "__main__":
    ds = load_dataset('saillab/alpaca-nepali-cleaned', split='train')
    subset = ds.shuffle(seed=42).select(range(3000))

    formatted = subset.map(format_example, remove_columns=subset.column_names)

    print("Example 0:")
    print(formatted[0])
    print("\nExample 1:")
    print(formatted[1])

    formatted.save_to_disk("nepali_roman_formatted")
    print("\nSaved to nepali_roman_formatted/")