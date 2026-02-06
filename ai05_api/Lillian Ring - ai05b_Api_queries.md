# API Query Building Assignment
---

## USGS Earthquake Queries

### Query 1: [Describe what you're searching for]
**URL:**
```
https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&minmagnitude=4.0&maxmagnitude=6.0&orderby=magnitude&limit=10
```

**Parameters used:**
- `format`: [geojson makes it readable]
- `minmagnitude=4.0`: [range min between 4.0-6.0]
- `maxmagnitude=6.0`: [range max between 4.0-6.0]
- `orderby=magnitude`: [order by magnitude]
- `limit=10`: [max resuts of 10]

**Result:** [gave 10 results of earthquakes ranging from 5.7-6 (no 4.0 earthquakes.)]

---

### Query 2: [Describe what you're searching for]
**URL:**
```
https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2020-02-05&orderby=time&limit=8
```

**Parameters used:**
- `format`: [explanation]
- `starttime=2020-02-05`: [starttime showing from 2020 feb. 5]
- `orderby`: [ordered by time]

**Result:** [shows most magnitudes being <5]

---

### Query 3: Earthquakes between 2023 & 2025
**URL:**
```
https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2023-01-01&endtime=2025-01-01&limit=4
```

**Parameters used:**
- `format`: geojson
- `parameter2`: [starttime from 2023]
- `parameter3`: [endtime to 2025]

**Result:** the magnitude of the earthquakes were all below 2.0

---

## Open Library Queries

### Query 4: Looking for the book/graphic novel titled 'amulet'
**URL:**
```
https://openlibrary.org/search.json?title=amulet&limit=5&language=eng
```

**Parameters used:**
- `title=amulet`: looking for a book titled 'Amulet'
- `language=eng`: putting it in english.

**Result:** 650 results (numfound). I found 3 volumes of the book I was trying to find. Gives author, edition, published year, and more.


### Query 5: looking for the book I'm currently reading in ELA, 'Frankenstein' by Mary Shelly
**URL:**
```
https://openlibrary.org/search.json?title=frankenstein&limit=5&language=eng&author=mary+shelly
```

**Parameters used:**
- `title=frankenstein`: looking for book titled 'Frankenstein'
- `author=mary+shelly`: author of the book 'Mary Shelly'

**Result:** Found the book, also came up with results that were similar.

### Query 6: Looking for a manga I have, 'Fairy Tail'
**URL:**
```
https://openlibrary.org/search.json?title=fairy+tail&limit=5&language=eng
```

**Parameters used:**
- `title=fairy+tail`: looking for the manga 'Fariy Tail'
- `language=eng`: language in english

**Result:** numfound = 287, Found the one I was looking for, also found a coloring book.