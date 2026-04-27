import urllib.request
import re
import gzip

url = "https://pieach.com/project/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        if response.info().get('Content-Encoding') == 'gzip':
            html = gzip.decompress(response.read()).decode('utf-8')
        else:
            try:
                html = response.read().decode('utf-8')
            except UnicodeDecodeError:
                # sometimes read() is already consumed or it's gzip but missing header
                pass
        
        imgs = re.findall(r'<img[^>]+src="([^">]+)"', html)
        valid_imgs = set([img for img in imgs if 'uploads' in img and ('jpg' in img or 'png' in img)])
        for img in valid_imgs:
            print(img)
except Exception as e:
    print(f"Error: {e}")
