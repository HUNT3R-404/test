# Compiled By Mr Mafia | Muhammad Muzammil
# Github :  https://github.com/Muzammil-404

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))