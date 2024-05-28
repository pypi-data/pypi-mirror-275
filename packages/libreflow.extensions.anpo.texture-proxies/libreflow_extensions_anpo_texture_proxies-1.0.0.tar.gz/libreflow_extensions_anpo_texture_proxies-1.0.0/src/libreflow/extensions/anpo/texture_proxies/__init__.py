import os
import subprocess
from kabaret import flow
from kabaret.flow.object import _Manager
from libreflow.baseflow.site import WorkingSite
from libreflow.baseflow.file import TrackedFolder
from libreflow.utils.flow.values import MultiOSParam
from libreflow.utils.os import remove_folder_content

from . import _version
__version__ = _version.get_versions()['version']

def get_img_width(img_path):
    '''Return the width of the provided image.'''
    output = subprocess.check_output(
        ["identify", "-format", "%[w]", img_path])
    return int(output.decode())

def create_proxies(blender_path, src_path, new_width, dst_path):
    script_path = os.path.join(os.path.dirname(__file__), 'create_proxies.py')
    try:
        result = subprocess.run([
            blender_path, '-b',
            '--python', script_path, '--',
            src_path, dst_path, str(new_width)],
            stdout=open(os.devnull, 'wb'), stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(f"[TEXTURE PROXIES] Error while creating proxies:")
        print(e.stderr)
        return False

    if result.returncode > 0:
        print(f"[TEXTURE PROXIES] Error while creating proxies:")
        print(result.stderr.decode())
        return False

    return True

class RevisionNameChoiceValue(flow.values.SessionValue):
    DEFAULT_EDITOR = 'choice'
    STRICT_CHOICES = False
    _folder = flow.Parent(2)

    def __init__(self, parent, name):
        super(RevisionNameChoiceValue, self).__init__(parent, name)
        self._revision_names = None

    def choices(self):
        if self._revision_names is None:
            self._revision_names = self._folder.get_revision_names(
                sync_status='Available', published_only=True)
        
        return self._revision_names

    def reset(self):
        self._revision_names = None
        names = self.choices()
        if names:
            self.set(names[-1])

class CreateTextureProxies(flow.Action):
    _MANAGER_TYPE = _Manager
    revision = flow.SessionParam(value_type=RevisionNameChoiceValue)
    _folder = flow.Parent()
    _files = flow.Parent(2)
    _task = flow.Parent(3)

    def needs_dialog(self):
        self.revision.reset()
        return True

    def allow_context(self, context):
        return not self._folder.is_empty()

    def get_buttons(self):
        return ['Create proxies', 'Cancel']

    def get_proxies_path(self, suffix, revision_name):
        folder_name = f"textures_{suffix}"
        path_format = None
        if not self._files.has_mapped_name(folder_name):
            task_mng = self.root().project().get_task_manager()
            if task_mng.has_default_task(self._task.name()):
                default_task = task_mng.default_tasks[self._task.name()]
                if default_task.files.has_mapped_name(folder_name):
                    print(f"[TEXTURE PROXIES] Create {folder_name} from preset")
                    path_format = default_task.files[folder_name].path_format.get()

            tex_folder = self._files.add_folder(folder_name, \
                tracked=True, default_path_format=path_format)
            tex_folder.file_type.set('Works')
        else:
            tex_folder = self._files[folder_name]

        rev = tex_folder.get_revision(revision_name)
        if rev is None:
            print(f"[TEXTURE PROXIES] {folder_name}: add new revision {revision_name}")
            rev = tex_folder.add_revision(revision_name)
        tex_path = rev.get_path()
        if not os.path.isdir(tex_path):
            os.makedirs(tex_path, exist_ok=True)
        else:
            remove_folder_content(tex_path)
        return tex_path

    def get_blender_path(self):
        # Check environment
        path = os.environ.get('BLENDER_EXEC_PATH')
        if path is not None:
            return path

        # Check site runner executables
        site_env = self.root().project().get_current_site().site_environment
        if not site_env.has_mapped_name('BLENDER_EXEC_PATH'):
            return None

        value = site_env['BLENDER_EXEC_PATH'].value
        value.touch()
        return value.get()

    def run(self, button):
        if button == 'Cancel':
            return

        blender_path = self.get_blender_path()
        if blender_path is None or not os.path.isfile(blender_path):
            msg = ('<h3 style="font-weight: 400"><div style="color: red">Error: </div>'
                  f'Blender executable not set. Please define it in the site settings.</h3>')
            self.message.set(msg)
            return self.get_result(close=False)

        self.message.set("")
        rev = self._folder.get_revision(self.revision.get())
        rev_path = rev.get_path()
        img_paths = [os.path.join(rev_path, tex) \
            for tex in os.listdir(rev_path)]

        print(f"[TEXTURE PROXIES] checking texture sizes...")
        img_widths = [get_img_width(path) \
            for path in img_paths]
        max_width = max(img_widths)
        print(f"[TEXTURE PROXIES] found max size -> {max_width}")

        for suffix, res in (
            ("1k", 1024),
            ("2k", 2048)):
            if max_width <= res:
                print(f"[TEXTURE PROXIES] skip textures_{suffix}")
                continue

            proxy_dir = self.get_proxies_path(suffix, rev.name())
            print(f"[TEXTURE PROXIES] textures_{suffix}({rev.name()}): resizing...")
            created = create_proxies(blender_path, \
                rev_path, res, proxy_dir)
            if created:
                print(f"[TEXTURE PROXIES] textures_{suffix}({rev.name()}): proxies created -> {proxy_dir}")


def create_proxies_action(parent):
    if isinstance(parent, TrackedFolder) and parent.name() == 'textures':
        r = flow.Child(CreateTextureProxies)
        r.name = 'create_proxies'
        r.index = None
        return r

def install_extensions(session):
    return {
        "texture_proxies": [
            create_proxies_action,
        ]
    }
