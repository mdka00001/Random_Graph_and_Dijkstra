import pandas as pd
import csv
import forcelayout as fl
import matplotlib.pyplot as plt
import matplotlib.animation as plt2

iris0=pd.read_excel(r"D:\BIII\Assignmentt_4\iris.xlsx")
iris=pd.DataFrame(iris0)
iris.columns=['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'variety']

iris_dt = iris[['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid']]

iris_class=[]
for i in iris['variety']:
    if i == "Setosa":
        iris_class.append(1)
    if i == "Versicolor":
        iris_class.append(2)
iris_class_df = pd.DataFrame(iris_class)
iris_class_df.columns =["variety"]

iris_dt_concat = pd.concat([iris_dt, iris_class_df], axis=1)


iris_np = iris_dt_concat.to_numpy()


colors = dict()
ind = 0
col = 0

color = ["blue","yellow"]

color_map=dict()


for i in iris["variety"]:
    if i == "Sesota":
         color_map[i] = color[0]
    if i == "Versicolor":
        color_map[i] = color[1]


def classed_iris(iris):
    global ind, col
    if iris_class[ind] not in colors:
        colors[iris_class[ind]] = col
        col += 1
    class_col = colors[iris_class[ind]]
    ind += 1
    return class_col

layout = fl.draw_spring_layout_animated(dataset=iris_np, algorithm=fl.NeighbourSampling, alpha=0.5,
                                     algorithm_highlights=True, color_by=classed_iris)

plt.savefig('iris.png')
plt.show()


