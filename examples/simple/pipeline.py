import pandas as pd
from conduits import Pipeline

##########################
## Pipeline Declaration ##
##########################

pipeline = Pipeline()


@pipeline.step(dependencies=["first_step"])
def second_step(data):
    return data + 1


@pipeline.step()
def first_step(data):
    return data ** 2


###############
## Execution ##
###############

df = pd.DataFrame({"X": [1, 2, 3], "Y": [10, 20, 30]})

output = pipeline.fit_transform(df)
assert output.X.sum() != 29  # Addition before square => False!
assert output.X.sum() == 17  # Square before addition => True!
