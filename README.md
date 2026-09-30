# wordcut

Wrap a sentence on spaces. Words are not split. Blank input returns an empty list.

```python
from wordcut import wrap, wrap_text

wrap("one two three", 7)
wrap_text("one two three", 7)  # "one two\nthree"
```

```bash
python -m unittest test_wordcut.py
```

MIT
