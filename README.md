# summer.ai

### Setup :hatching_chick: 
 
```bash
brew install npm
npm install less -g
pip install cactus
```

### Muddle :coffee: 

All development is done on the `dev` branch. 

```bash
git checkout dev
cactus serve  # starts local server, reloads on changes
# Fix typos on pages/index.html
# Change images in static/images/
# Cornify style in less/landing.less
git add --all
git commit -m "Sparkly stuff" 
git push
```

###  Ship :rocket:

```bash
git checkout master
make  # Goes to dev branch, builds, copies build to master and auto-pushes
```
