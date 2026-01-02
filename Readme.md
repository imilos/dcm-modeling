# DCM Modeling site
We are using Pelican Python static site generator.

## Install instructions

```
pip install pelican[markdown]
git clone https://github.com/getpelican/pelican-plugins.git pelican-plugins
pip install git+https://github.com/arulrajnet/attila.git@master
```

## Build and serve
```
pelican content
pelican --listen
```
