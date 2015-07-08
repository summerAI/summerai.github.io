# knot63.com

### Setup :hatching_chick: 
 
```bash
brew install npm
npm install less -g
pip install cactus
```

### Muddle :coffee: 

All development is done on the `summer` branch. 

```bash
git checkout summer
cactus serve  # starts local server, reloads on changes
# Fix cheesy copy on pages/index.html
# Add cat gifs to static/images/
# Cornify styles in less/landing.less
git commit --all -m "Sparkly stuff" 
git push
```

###  Ship :rocket:

```bash
git checkout master
make  # Goes to summer branch, builds, copies build to master and auto-pushes
```
