![main-documentation](https://github.com/aws-quickstart/quickstart-documentation-base/workflows/main-documentation/badge.svg)

**This folder contains the base structure for AWS QuickStarts (New Repos will be auto populated with this structure**

## Docs 
```
├── docs
│   ├── README.md
│   ├── common
│   ├── css
│   ├── generated
│   ├── images
│   └── index.adoc
```
Root folder Main Documentation (docroot)

### README.md 
 Render only when in github and serves as a description when browsing github
### common 
```
├── common
│   ├── about_this_guide.adoc
│   ├── cost.adoc
│   ├── overview.adoc
│   └── troubleshoot.adoc
```
 Generic content that will be liked from this repo to other docs via github

 **Example:** To embed overview.adoc file from __common__ 
 ```
 # add to this to index.adoc
 include::https://raw.githubusercontent.com/aws-quickstart/quickstart-documentation-base/master/docs/common/overview.adoc
 ```
### css 
 ```
├── css
    └── quickstart.css
```
 Hold documentation styles sheets

### generated
```
├── generated
    └── parameter_table.adoc
```
 Content in this folder will auto generated upon commits to master for example parameter tables

### images 
 Used to store images referenced in documentation

## Quick Start Reference Folders 
**(scripts templates)**

###  scripts
```
├── scripts
│   └── ngnix.conf
```
Hold scripts and config files used in cfn bootstrapping
   
### submodules
```
├── submodules
    └── quickstart-aws-vpc

```
 QuickStart submodules example: quickstart-aws-vpc

### templates
```
├── templates
    ├── master.template.yaml
    └── workload.template.yaml

```
 Cloudformation templates example: ( master.template.yaml)

### Workshops 
```
├── workshops
    ├── awsworkshop.io
    └── immersionday
```
 **awsworkshop** (If this folder existing awsworkshop.io content will be updated in ghpages branch upon commits to master)
 **immersionday** (If this folder existing immersionday modules will be updated in ghpages upon on commits to master)
