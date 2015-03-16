# knot63.com

### Setup :hatching_chick: 
 
```bash
pip install cactus
gem install less -g
```

### Muddle :coffee: 

All development is done on the `dev` branch. 

```bash
git checkout dev
cactus serve  # starts local server, reloads on changes
# Fix typo op pages/index.html
# Change images in static/images/
# Cornify style in less/landing.less
git add -a
git commit -m "Sparkly stuff" 
git push
```

###  Ship :rocket:

```bash
git checkout master
make  # Pulls from dev, builds and auto-pushes
```
