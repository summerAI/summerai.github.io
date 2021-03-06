# summer.ai

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
# Fix typos on pages/index.html
# Change images in static/images/
# Cornify style in less/landing.less
git commit --all -m "Sparkly stuff" 
git push
```

###  Ship :rocket:

```bash
git checkout master
make  # Goes to dev branch, builds, copies build to master and auto-pushes
```

###  Adding Books :books:

1. Find book on Amazon.
2. Copy the 10-digit product ID from the URL (e.g. 'B00C0ALZ0W')
3. Insert into `bookshelf.yaml` in the appropriate shelf (The part after the colon is just a comment and won't be displayed)
4. run `python build_shelf.py` to scrape Amazon.

This requires a file `~/.amazon-product-api` to be present with the following contents:

```
[Credentials]
access_key = <YOUR_ACCESS_KEY>
secret_key = <YOUR_SECRET_KEY>
associate_tag = summerai-20
```

Not that these have to be root credentials, IAM identities won't work (amazon's fault).
