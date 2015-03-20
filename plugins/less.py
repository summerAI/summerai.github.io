import subprocess
from glob import glob


def postBuild(site):
    for filename in glob('%s/static/less/*less' % site.paths['build']):
        root_name = filename.rsplit('.', 1)[0]
        src = filename
        dest = "%s.css" % root_name.replace("/less/", "/css/")
        try:
            print "compiling", dest
            subprocess.check_call(['lessc', src, dest])
        except subprocess.CalledProcessError:
            print "lessc returned a non-zero exit status, please check your less syntax"
