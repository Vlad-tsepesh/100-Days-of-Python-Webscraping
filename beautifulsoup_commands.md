# BeautifulSoup Top Commands Cheat Sheet

A concise list of the most used **BeautifulSoup** commands and properties, formatted for quick lookup and practical usage.

---

## 🌳 Core Object & Initialization

1. `BeautifulSoup(html, parser)` – create a soup object from HTML/XML
2. `.prettify()` – format the parse tree with indentation
3. `.encode(...)` / `.decode(...)` – encode/decode with formatting options

---

## 🔍 Searching & Filtering

4. `.find(name, attrs, ...)` – returns the first matching tag
5. `.find_all(name, attrs, limit=…)` – returns all matching tags
6. `.select(selector)` – use CSS selectors (e.g. `.content p#intro`)
7. `.find_parent(...)` / `.find_parents(...)` – find ancestor tags
8. `.find_next_sibling(...)` / `.find_previous_sibling(...)` – get adjacent sibling
9. `.find_next_siblings(...)` / `.find_previous_siblings(...)` – all adjacent siblings
10. `.find_next(...)` / `.find_previous(...)` – next/prev in document order
11. `.find_all_next(...)` / `.find_all_previous(...)` – all following/preceding elements
12. Use `text=` in `.find_all(...)` – filter by inner text
13. Use `attrs={...}` – filter by attributes dict
14. Use regex, list, function, or `True` in tag search filters

---

## 🚶 Traversal: Tree Navigation

15. `.contents` – list of direct children
16. `.children` – iterator over direct children
17. `.descendants` – iterator over all descendants
18. `.string` – if the tag has one direct string child
19. `.strings` – all descendant strings (including whitespace)
20. `.stripped_strings` – all descendant strings (no whitespace)
21. `.parent` – direct parent
22. `.parents` – generator of all ancestors
23. `.next_sibling` / `.previous_sibling` – adjacent elements
24. `.next_siblings` / `.previous_siblings` – all siblings after/before
25. `.next_element` / `.previous_element` – next/prev in doc order
26. `.next_elements` / `.previous_elements` – all following/preceding nodes

---

## 💬 Accessing Text & Attributes

27. `.get_text(separator, strip)` – combined text with options
28. `.text` – shorthand for `.get_text()`
29. Attribute access – `tag['href']`, `tag.get('class')`, etc.

---

## ✏️ Modifying the Tree

30. `.append(new)` – add child tag
31. `.extend([...])` – add multiple children
32. `.new_tag(name, **attrs)` – create a new tag
33. `.insert(position, new_tag)` – insert child at index
34. `.insert_before(...)` / `.insert_after(...)` – insert near current
35. `.clear()` – remove all children
36. `.extract()` – remove this tag and return it
37. `.decompose()` – completely destroy tag and contents
38. `.replace_with(new)` – replace tag with another
39. `.wrap(new_tag)` – wrap element in another tag
40. `.unwrap()` – remove current tag, preserve children
41. `.smooth()` – normalize whitespace and formatting
42. `.replace_with()` – same tag replacement shortcut
43. Create and insert tag together: `.insert_*` and `.new_tag`

---

## 🧰 Diagnostics & Utilities

44. `diagnose(data)` – inspect HTML to detect parser issues
45. `.get_text(strip=True)` – get cleaned text from element
46. `.prettify()` – format output (useful for inspection)

---

## 📜 Real‑World Usage Example

```python
from bs4 import BeautifulSoup
import requests

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
main = soup.find('div', class_='main')
links = main.find_all('a')

for a in links:
    print(a.get_text(strip=True), a['href'])
```

---

## ✅ Recap Summary

| Group        | Commands Count |
| ------------ | -------------- |
| Core & init  | \~3            |
| Searching    | \~11           |
| Traversal    | \~12           |
| Text & attrs | \~3            |
| Modify tree  | \~13           |
| Diagnostics  | \~3            |
| **Total**    | **\~45+**      |

---

> 📌 Use these commands in real-world scraping, cleaning, and parsing workflows. Focus on `find`, `select`, `get_text`, and traversal for 90% of your use cases.

---

*Updated August 2025 – compiled by ChatGPT based on BeautifulSoup documentation and usage in the field.*

