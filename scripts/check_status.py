import os

root = '.'
results = []

skip = {'.git', 'assets', 'scripts', 'templates', 'genel', '.github', '.vs'}

for name in sorted(os.listdir(root)):
    path = os.path.join(root, name)
    if os.path.isdir(path) and name not in skip:
        items = os.listdir(path)
        subdirs = [i for i in items if os.path.isdir(os.path.join(path, i))]
        files = [i for i in items if os.path.isfile(os.path.join(path, i))]
        empty_subdirs = []
        nonempty_subdirs = []
        for sd in subdirs:
            sdpath = os.path.join(path, sd)
            sd_items = os.listdir(sdpath)
            sd_files = [f for f in sd_items if os.path.isfile(os.path.join(sdpath, f))]
            sd_subdirs = [f for f in sd_items if os.path.isdir(os.path.join(sdpath, f))]
            if sd_files == [] or sd_files == ['README.md']:
                if sd_subdirs == []:
                    empty_subdirs.append(sd)
                else:
                    nonempty_subdirs.append(sd + '/ (has subdirs)')
            else:
                nonempty_subdirs.append(sd)
        results.append({
            'dir': name,
            'subdirs_total': len(subdirs),
            'empty': len(empty_subdirs),
            'nonempty': len(nonempty_subdirs),
            'files': files
        })

for r in results:
    status = 'DOLU' if r['nonempty'] > 0 else 'BOS'
    print(status + ' | ' + r['dir'] + ' | subdirs=' + str(r['subdirs_total']) + ' | bos=' + str(r['empty']) + ' dolu=' + str(r['nonempty']))
