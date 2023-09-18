[![SVG Banners](https://svg-banners.vercel.app/api?type=typeWriter&text1=Machine%20Learning%20👨‍💻&width=800&height=100)](https://github.com/Akshay090/svg-banners)

## ML w/ Python -  ScikitLearn

# :exclamation: Disclaimer 

All gathered data has already been discarded and is only used for educational purposes. After creating the report, all data were removed and deleted immediately.

---

### Used pip packages

| Package  | Version  |    
|---|---|
| joblib  | 1.3.2  |
| numpy  | 1.26.0  | 
| pip  | 22.0.4  |
| scikit-learn  | 1.3.0  | 
| scipy  | 1.11.2  |
| setuptools  | 58.1.0  |
| threadpoolctl  | 3.2.0  | 

## Data gathering and capture
Raw data was captured during a live stream of a well-known German streamer using the stream platform's own API. For more information, read [here](https://dev.twitch.tv): 

See [here]() how **I** did it very simply with just a few lines of code.

## Output

You can see here the report that was created from the data input and my assignments for the cluster keywords:

|   Class   | Precision |  Recall  | F1-Score | Support |
|:---------:|:---------:|:--------:|:--------:|:-------:|
|     -1    |    0.92   |   1.00   |   0.96   |  10234  |
|     0     |    0.94   |   0.20   |   0.33   |   867   |
|     1     |    0.00   |   0.00   |   0.00   |    42   |
|     2     |    0.00   |   0.00   |   0.00   |    8    |
|     3     |    0.00   |   0.00   |   0.00   |    17   |
|     4     |    0.95   |   0.72   |   0.81   |   387   |
|     5     |    0.98   |   0.85   |   0.91   |   169   |
|     6     |    1.00   |   0.58   |   0.74   |    43   |
|     7     |    0.00   |   0.00   |   0.00   |    15   |
|  Accuracy |    0.92   |          |          |  11782  |
| Macro Avg |    0.53   |   0.37   |   0.42   |  11782  |
|Weighted Avg|   0.92   |   0.92   |   0.90   |  11782  |

## Conclusion

I will gather some more data from the platform and its chat to achieve higher scores with the model. After reaching a specific point, the model should be able to make more specific predictions than it does today.
