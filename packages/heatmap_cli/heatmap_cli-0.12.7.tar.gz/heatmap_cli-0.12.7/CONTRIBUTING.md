# Contributing

## Setting up local development

Clone repository from GitHub:

```console
git clone https://github.com/kianmeng/heatmap_cli
cd heatmap_cli
```

To set up different Python environments, we need to install all supported
Python version using <https://github.com/pyenv/pyenv>. Once you've installed
`pyenv`, install these additional `pyenv` plugins:

```console
git clone https://github.com/pyenv/pyenv-doctor.git "$(pyenv root)/plugins/pyenv-doctor"
pyenv doctor

git clone https://github.com/pyenv/pyenv-update.git $(pyenv root)/plugins/pyenv-update
pyenv update
```

Run the command below to install all Python versions:

```console
pyenv install $(cat .python-version)
```

Install and upgrade required Python packages:

```console
python -m pip install --upgrade pip pipenv
pipenv install --dev
```

Spawn a shell in virtual environment for your development:

```console
pipenv shell
```

Show all available `tox` tasks:

```console
tox -av
```

```console
...
default environments:
py38  -> testing against python3.8
py39  -> testing against python3.9
py310 -> testing against python3.10
py311 -> testing against python3.11
py312 -> testing against python3.12

additional environments:
cov   -> generate code coverage report in html
doc   -> generate sphinx documentation in html
```

For code linting, we're using `pre-commit`:

```console
pre-commit install # run once
pre-commit clean
pre-commit run --all-files
```

Or specific hook:

```console
pre-commit run pylint -a
```

## Create a Pull Request

Fork it at GitHub, <https://github.com/kianmeng/heatmap_cli/fork>

Create your feature branch:

```console
git checkout -b my-new-feature
```

Commit your changes:

```console
git commit -am 'Add some feature'
```

Push to the branch:

```console
git push origin my-new-feature
```

Create new Pull Request in GitHub.

## License

## Developer's Certificate of Origin

By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I have the right
to submit it under the open source license indicated in the file; or

(b) The contribution is based upon previous work that, to the best of my
knowledge, is covered under an appropriate open source license and I have the
right under that license to submit that work with modifications, whether
created in whole or in part by me, under the same open source license (unless I
am permitted to submit under a different license), as indicated in the file; or

(c) The contribution was provided directly to me by some other person who
certified (a), (b) or (c) and I have not modified it.

(d) I understand and agree that this project and the contribution are public
and that a record of the contribution (including all personal information I
submit with it, including my sign-off) is maintained indefinitely and may be
redistributed consistent with this project or the open source license(s)
involved.
