import collections
import concurrent.futures
import gzip
import hashlib
import math
import platform
import requests
import shutil
import time
from blake3 import blake3
from getblocks import __version__
from pathlib import Path, PurePath

def hasher(fname):

    try:
        md5_file = ''
        sha256_file = ''
        b3_file = ''
        BLOCKSIZE = 65536
        md5_hasher = hashlib.md5()
        sha256_hasher = hashlib.sha256()
        b3_hasher = blake3()
        with open(fname,'rb') as afile:
            buf = afile.read(BLOCKSIZE)
            while len(buf) > 0:
                md5_hasher.update(buf)
                sha256_hasher.update(buf)
                b3_hasher.update(buf)
                buf = afile.read(BLOCKSIZE)
        md5_file = md5_hasher.hexdigest().upper()
        sha256_file = sha256_hasher.hexdigest().upper()
        b3_file = b3_hasher.hexdigest().upper()
    except:
        md5_file = '-'
        sha256_file = '-'
        b3_file = '-'
        pass
    if md5_file == 'D41D8CD98F00B204E9800998ECF8427E':
        md5_file = 'EMPTY'
    if sha256_file == 'E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855':
        sha256_file = 'EMPTY'
    if b3_file == 'AF1349B9F5F9A1A6A0404DEA36DCC9499BCB25C9ADC112B7CC9A93CAE41F3262':
        b3_file = 'EMPTY'
    hashes = md5_file+'|'+sha256_file+'|'+b3_file
    return hashes

def matchmeta(meta):

    md5_hasher = hashlib.md5()
    sha256_hasher = hashlib.sha256()
    b3_hasher = blake3()
    md5_hasher.update(meta.encode())
    sha256_hasher.update(meta.encode())
    b3_hasher.update(meta.encode())
    md5_meta = md5_hasher.hexdigest().upper()
    sha256_meta = sha256_hasher.hexdigest().upper()
    b3_meta = b3_hasher.hexdigest().upper()
    meta = md5_meta+'|'+sha256_meta+'|'+b3_meta
    return meta

def normalizepath(path):

    if path[:1] == '/':
        out = path.split('/')
        try:
            if out[1] == 'home':            ### LINUX
                out[2] = 'user'
                path = '/'.join(out)
            elif out[1] == 'Users':         ### APPLE
                if out[2] != 'Shared':
                    out[2] = 'user'
                    path = '/'.join(out)
        except:
            pass
    elif path[1] == ':': 				    ### WINDOWS
        out = path.split('\\')
        try:
            if out[1] == 'Users' or out[1] == 'Documents and Settings':
                if out[2] != 'Default' and out[2] != 'Public' and out[2] != 'All Users' and out[2] != 'Default User':
                    out[0] = 'C:'
                    out[2] = 'Administrator'
                    path = '\\'.join(out)
        except:
            pass
    return path

def parsefilename(filename):

    if filename[:1] == '/':					### UNIX
        out = filename.split('/')
        count = len(out) - 1
    elif filename[1] == ':': 				### WINDOWS
        out = filename.split('\\')
        count = len(out) - 1
    return out[count]

def parseonlypath(onlypath):

    if onlypath[:1] == '/':					### UNIX
        out = onlypath.split('/')
        del out[-1]
        onlypath = '/'.join(out)
    elif onlypath[1] == ':': 				### WINDOWS
        out = onlypath.split('\\')
        del out[-1]
        onlypath = '\\'.join(out)
    return onlypath

def parser(p, amiid):

    try:
        size =  p.stat().st_size		
    except: 
        size = 0
        pass
    if size == 0:
        md5_file = 'EMPTY'
        sha256_file = 'EMPTY'
        b3_file = 'EMPTY'
    elif size > 104857599:
        md5_file = 'LARGE'
        sha256_file = 'LARGE'
        b3_file = 'LARGE'
    else:
        hashes = hasher(str(p))
        out = hashes.split('|')
        md5_file = out[0]
        sha256_file = out[1]
        b3_file = out[2]
    fullpath = normalizepath(str(p))
    meta = matchmeta(fullpath)
    out = meta.split('|')
    md5_path = out[0]
    sha256_path = out[1]
    b3_path = out[2]
    directory = parseonlypath(fullpath)
    meta = matchmeta(directory)
    out = meta.split('|')
    md5_dir = out[0]
    sha256_dir = out[1]
    b3_dir = out[2]
    filename = parsefilename(fullpath)
    meta = matchmeta(filename)
    out = meta.split('|')
    md5_name = out[0]
    sha256_name = out[1]
    b3_name = out[2]
    value = str(amiid)+'|'+ \
        str(fullpath)+'|'+ \
        str(filename)+'|'+ \
        str(size)+'|'+ \
        str(md5_file)+'|'+ \
        str(sha256_file)+'|'+ \
        str(b3_file)+'|'+ \
        str(md5_path)+'|'+ \
        str(sha256_path)+'|'+ \
        str(b3_path)+'|'+ \
        str(md5_dir)+'|'+ \
        str(sha256_dir)+'|'+ \
        str(b3_dir)+'|'+ \
        str(md5_name)+'|'+ \
        str(sha256_name)+'|'+ \
        str(b3_name)+'|FILE|-|-|-\n'
    return value

def sector(p,count):

    block = 512
    ifile = open(p,'rb')
    ifile.seek(count)
    entropy_value = 0
    bases = collections.Counter([tmp_base for tmp_base in ifile.read(block)])
    for base in bases:
        n_i = bases[base]
        p_i = n_i / float(block)
        entropy_i = p_i * (math.log(p_i, 2))
        entropy_value += entropy_i
    entropy = entropy_value * -1
    ifile.seek(count)
    b3block =  blake3(ifile.read(block)).hexdigest().upper()
    if b3block == 'AF1349B9F5F9A1A6A0404DEA36DCC9499BCB25C9ADC112B7CC9A93CAE41F3262':
        b3block = 'EMPTY'
    return str(entropy)+'|'+b3block

def start(amiid):

    with open(amiid+'.txt', 'w+') as f:
        f.write('ami|path|file|size|md5|sha256|b3|md5path|sha256path|b3path|md5dir|sha256dir|b3dir|md5name|sha256name|b3name|type|entropy|block|location\n')
        root = PurePath(Path.cwd()).anchor
        path = Path(root)
        for p in Path(path).glob('*'):
            if str(p) != '/proc':
                if p.is_file() == True and not str(p).endswith(amiid+'.txt'):
                    value = parser(p, amiid)
                    if value != None:
                        f.write(value)
                        out = value.split('|')
                        if out[6] != 'LARGE' and out[6] != 'EMPTY' and out[6] != '-':
                            count = 0
                            location = 1
                            while count <= int(out[3]):
                                try:
                                    block = sector(p,count)
                                    parse = block.split('|')
                                    f.write(str(out[0])+'|-|-|'+str(out[3])+'|-|-|'+str(out[6])+'|-|-|-|-|-|-|-|-|-|SECTOR|'+str(parse[0])+'|'+str(parse[1])+'|'+str(location)+'\n')
                                except:
                                    pass
                                count = count + 512
                                location = location + 1
                else:
                    for s in Path(p).rglob('*'):
                        if s.is_file() == True and not str(s).endswith(amiid+'.txt'):
                            value = parser(s, amiid)
                            if value != None:
                                f.write(value)
                                out = value.split('|')
                                if out[6] != 'LARGE' and out[6] != 'EMPTY' and out[6] != '-':
                                    count = 0
                                    location = 1
                                    while count <= int(out[3]):
                                        try:
                                            block = sector(s,count)
                                            parse = block.split('|')
                                            f.write(str(out[0])+'|-|-|'+str(out[3])+'|-|-|'+str(out[6])+'|-|-|-|-|-|-|-|-|-|SECTOR|'+str(parse[0])+'|'+str(parse[1])+'|'+str(location)+'\n')
                                        except:
                                            pass
                                        count = count + 512
                                        location = location + 1
    f.close()

def main():

    print('GETBLOCKS v'+__version__)

    ### Instance Metadata Service Version 2 (IMDSv2) ###

    try:

        headers = {'X-aws-ec2-metadata-token-ttl-seconds': '30'}
        token = requests.put('http://169.254.169.254/latest/api/token', headers=headers)

        headers = {'X-aws-ec2-metadata-token': token.text}
        r = requests.get('http://169.254.169.254/latest/meta-data/ami-id', headers=headers)
        amiid = r.text

    except:

        host = platform.node()
        amiid = 'ami-'+str(host.lower())

        pass

    print('  '+amiid)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(start, amiid)

    time.sleep(30)

    with open(amiid+'.txt', 'rb') as f_in:
        with gzip.open(amiid+'.txt.gz', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    print('    Done!!')