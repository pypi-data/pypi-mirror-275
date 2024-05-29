# Jabroni

Convert between journal abbreviated and full titles.

```shell
pip install jabroni
```

```python
>>> import jabroni

>>> jabroni.get_abbr("Journal of Neuroscience")
'J Neurosci'

>>> jabroni.get_full("J Neurosci")
'Journal of Neuroscience'

>>> jabroni.get_full("J Neuroscissss")
KeyError: 'J Neuroscissss'

>>> jabroni.get_full("J Neuroscissss", errors="preserve")
'Journal Neuroscissss'
```
