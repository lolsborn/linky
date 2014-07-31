Turns text links, emails, and phone numbers into html links

## Example ##

```python
import cgi
from linky import linky

plain_text = """
Steven Osborn <osborn.steven@gmail.com>
phone: 918.513.1392
http://steven.bitsetters.com
"""
plain_text = cgi.escape(plain_text)
print linky(plain_text)
```

### Produces ###

```html
Steven Osborn &lt;<a href="mailto:osborn.steven@gmail.com" target="_blank">osborn.steven@gmail.com</a>&gt;
phone: <a href="tel:9185131392" target="_blank">9185131392</a>
<a href="http://steven.bitsetters.com" target="_blank">http://steven.bitsetters.com</a>
```

You can provide your own formatting functions by supplying callback functions to *url_callback*, *email_callback*, & *phone_callback*.  In addition if you don't wish to format email or phone strings you can set the appropriate callback to None
