# Compiled By Mr Mafia | Muhammad Muzammil
# Github :  https://github.com/Muzammil-404

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))