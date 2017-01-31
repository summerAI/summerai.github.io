import subprocess

OUTPUT = ("error", "landing", "bookshelf", "marketing")


def postBuild(site):
    for output in OUTPUT:
        filename = '{}/static/less/{}.less'.format(site.paths['build'], output)
        root_name = filename.rsplit('.', 1)[0]
        src = filename
        dest = "%s.css" % root_name.replace("/less/", "/css/")
        try:
            print("compiling", dest)
            subprocess.check_call(['lessc', src, dest])
        except subprocess.CalledProcessError:
            print("lessc returned a non-zero exit status, please check your less syntax")
