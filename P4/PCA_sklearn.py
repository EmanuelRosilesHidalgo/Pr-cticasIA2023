plt.figure(figsize=(8,6))
scatter = plt.scatter(df.culmen_length_mm, 
            df.culmen_depth_mm,
            s=150,
            c=df.species.astype('category').cat.codes)
plt.xlabel("Culmen Length", size=24)
plt.ylabel("Culmen Depth", size=24)
# add legend to the plot with names
plt.legend(handles=scatter.legend_elements()[0], 
           title="species")
plt.savefig("scatterplot_colored_by_variable_legend_first_try_matplotlib_Python.png",
                    format='png',dpi=150)