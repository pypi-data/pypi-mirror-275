from setux.core import __version__
from setux.core.module import Module
from setux.logger import info


class Distro(Module):
    '''Show target infos
    '''

    def deploy(self, target, **kw):
        user = target.login.name
        kernel = target.kernel
        ret, out, err = target.run('python -V')
        python = out[0] if ret == 0 else '-'
        addr = target.net.addr or '!'

        infos =  f'''
        target : {target}
        distro : {target.distro.name}
        python : {python}
        os     : {kernel.name} {kernel.version} / {kernel.arch}
        user   : {user}
        host   : {target.system.hostname} : {addr}
        setux  : {__version__}
        '''

        info(infos)
        return True
