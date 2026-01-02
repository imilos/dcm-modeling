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

## Deploy
By employing GitHub Actions, the site is directly deployed to the server, whether 
[https://dcm-modeling.kg.ac.rs](https://dcm-modeling.kg.ac.rs) or 
[https://dcmodeling.kg.ac.rs](https://dcmodeling.kg.ac.rs).
