# wordcut

Wrap a sentence on spaces. Words are not split. Blank input returns an empty list.

```python
from wordcut import wrap, wrap_text, line_count

wrap("one two three", 7)
wrap_text("one two three", 7)  # "one two\nthree"
line_count("one two three", 7)  # 2
```

```bash
python -m unittest test_wordcut.py
```

MIT
