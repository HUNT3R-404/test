# Compiled By Mr Mafia | Muhammad Muzammil
# Github :  https://github.com/Muzammil-404

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))