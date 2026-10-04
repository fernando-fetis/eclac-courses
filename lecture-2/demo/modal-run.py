'''Run notebook.ipynb on a Modal GPU, or open JupyterLab served from one.

    modal run modal-run.py::corpus     scrape the ECLAC repository into assets/corpus.txt
    modal run modal-run.py::execute    run every cell on the GPU and bring the notebook back
    modal run modal-run.py::jupyter    serve JupyterLab from the GPU, and print its URL

Set GPU to ask for a different one, for instance GPU=H100 modal run modal-run.py::jupyter.

Stop any of them with Ctrl+C: the container lives as long as the local command does.

The Hugging Face cache lives in the `hf-cache` volume, so a model is downloaded once and every later run starts from it. The notebook and `assets/` live in the `eclac-lecture-2` volume, which is what JupyterLab edits during a talk.
'''

import os
import pathlib
import secrets
import subprocess

import modal

GPU = os.environ.get('GPU', 'L40S')
DEMO = pathlib.Path(__file__).parent

image = (
    modal.Image.debian_slim(python_version='3.12')
    .pip_install('torch', 'transformers>=5.0', 'accelerate', 'datasets', 'numpy', 'matplotlib', 'jupyterlab', 'nbclient', 'nbformat', 'ipykernel', 'ipywidgets')
    .env({'HF_HOME': '/cache/huggingface'})
)

hf_cache = modal.Volume.from_name('hf-cache', create_if_missing=True)
workspace = modal.Volume.from_name('eclac-lecture-2', create_if_missing=True)

app = modal.App('eclac-lecture-2')

VOLUMES = {'/cache': hf_cache, '/workspace': workspace}


def upload() -> None:
    '''The notebook and its assets; assets/.temp holds the source PDFs and stays local.'''
    with workspace.batch_upload(force=True) as batch:
        batch.put_file(DEMO / 'notebook.ipynb', 'notebook.ipynb')
        for name in ('build-corpus.py', 'corpus.txt', 'gpt.pt'):
            if (DEMO / 'assets' / name).exists():
                batch.put_file(DEMO / 'assets' / name, f'assets/{name}')


@app.function(image=image, volumes=VOLUMES, timeout=3600)
def build_corpus(listing: bool) -> str:
    subprocess.run(['python', '-u', 'assets/build-corpus.py', *(['--list'] if listing else [])], cwd='/workspace')
    workspace.commit()
    return 'corpus built'


@app.function(image=image, gpu=GPU, volumes=VOLUMES, timeout=3 * 3600)
def run_notebook() -> str:
    import nbformat
    from nbclient import NotebookClient

    print(subprocess.run(['nvidia-smi', '--query-gpu=name,memory.total', '--format=csv,noheader'], capture_output=True, text=True).stdout.strip())

    path = pathlib.Path('/workspace/notebook.ipynb')
    notebook = nbformat.read(path, as_version=4)
    NotebookClient(notebook, timeout=3000, kernel_name='python3', resources={'metadata': {'path': '/workspace'}}, allow_errors=True).execute()
    nbformat.write(notebook, path)
    workspace.commit()

    failures = [f"cell {index}: {output['ename']}: {output['evalue'][:160]}" for index, cell in enumerate(notebook.cells) for output in cell.get('outputs', []) if output.get('output_type') == 'error']
    return '\n'.join(failures) if failures else 'every cell ran'


@app.function(image=image, gpu=GPU, volumes=VOLUMES, timeout=4 * 3600)
def serve_jupyter(token: str) -> None:
    environment = os.environ | {'SHELL': '/bin/bash'}
    subprocess.run(['jupyter', 'trust', '/workspace/notebook.ipynb'], env=environment)

    with modal.forward(8888) as tunnel:
        print(f'\n  JupyterLab: {tunnel.url}/lab?token={token}\n')
        subprocess.run(['jupyter', 'lab', '--ip=0.0.0.0', '--port=8888', '--no-browser', '--allow-root', '--ServerApp.root_dir=/workspace', f'--IdentityProvider.token={token}', '--ServerApp.allow_origin=*', '--ServerApp.allow_remote_access=True'], env=environment)


@app.local_entrypoint()
def corpus(listing: bool = False) -> None:
    upload()
    print(build_corpus.remote(listing))
    if listing:
        return

    text = b''.join(workspace.read_file('assets/corpus.txt'))
    (DEMO / 'assets' / 'corpus.txt').write_bytes(text)
    print(f'assets/corpus.txt written back, {len(text) / 1e6:.2f} MB')


@app.local_entrypoint()
def execute() -> None:
    upload()
    print(run_notebook.remote())

    executed = b''.join(workspace.read_file('notebook.ipynb'))
    (DEMO / 'notebook.ipynb').write_bytes(executed)
    print(f'notebook.ipynb written back, {len(executed) / 1e6:.1f} MB')


@app.local_entrypoint()
def jupyter() -> None:
    upload()
    serve_jupyter.remote(secrets.token_urlsafe(12))
