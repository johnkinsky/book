# PyPi Package Data Graph

While I was a data analyst, I created a simple version of this script to help some development teams and product managers, who didn't own the pypi.org packages, visualize pip package usage they helped to maintain. (I know that sounds odd, but that's modern corporate life.)

I've modified the script a little to automatically generate a line chart of the data. It also adds the values to the highest and lowest download numbers. 

This is a draft of the modified version; however, it's relatively harmless and should not blow up your system in it's current state. It will evolve with some planned improvements as time and energy allow.

I used [pypistats](https://pypistats.org/api/) to retrieve the data. (As far as I can tell pypistats is the only way to get the data now that other APIs are not supported now.) I used a [matplotlib](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot) line chart to visualize the data.

> **Note**: I started with a mermaid.js xychart version of the chart, but mathplotlib is much easier to implement and format and much clearer to read. 

## Run the PyPi Package Data Graph Script

1. Install the requirements. (This is necessary only if you do not have the packages installed arlready.)

   ```
   pip install -r requirements.txt
   ```

2. Run the script.
   ```
   python pypi_downloads.py
   ```

3. When prompted, enter a valid package name (without version numbers). For example, you might enter something like:
   ```
   openseries
   ```
4. Once the script completes, open the HTML file, in the same directory as the script, to see the charted data. You should see something similar to the following image.

![htmlcontainer.png](htmlcontainer.png "HMTL version")

## Script Output

The script generates an HTML page containing a PNG chart and a CSV file containing the data.

The script prepends the package name to the output file name specified in the file. So if you entered "openseries" as the package name, the script will show the following messages once the outputs are generated.

```
Full data saved to openseries_download_data.csv.
HTML container saved to openseries_download_data.html.
```

Here are some suggested packages to use for testing:

- `matplotlib` - Relatively large activity
- `breathe` - Moderate activity
- `openseries` - Relatively light activity



## Clean Up

When you are done, you can remove the packages installed for this example by entering the following command:
```
pip uninstall -y -r requirements.txt
```
Enjoy!