## Set up

### Mirroring the website

#### Mirror the blog site
```
wget --mirror --convert-links --adjust-extension --page-requisites https://blog.zorin.com/
```

#### Mirror the main site
```
wget --mirror --convert-links --adjust-extension --page-requisites https://zorin.com/
```

#### Mirror the help site
```
wget --mirror --convert-links --adjust-extension --page-requisites https://help.zorin.com/
```

### Creating the Indexes
Execute the notebook `create_indexes.ipynb` to create the indexes for the blog, main and help sites.
This will also create a merged index for all three sites and saved in the `index` folder.
