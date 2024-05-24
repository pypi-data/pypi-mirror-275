# zh_RSM

推荐系统常用模型实现

## Match
> 推荐系统中的召回，之前一直以为是Recall，但论文中常称作match或者candidate generate


## Publish
```shell
# packing
python setup.py sdist bdist_wheel
# upload
twine upload --repository pypi dist/*
```