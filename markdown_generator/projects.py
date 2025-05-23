# coding: utf-8

# # Projects markdown generator for academicpages
#
# Takes a TSV of projects with metadata and converts them for use with [academicpages.github.io](academicpages.github.io). This is an interactive Jupyter notebook, with the core python code in projects.py. Run either from the `markdown_generator` folder after replacing `projects.tsv` with one that fits your format.
#
# TODO: Make this work with BibTex and other databases of citations, rather than Stuart's non-standard TSV format and citation style.
#

# ## Data format
#
# The TSV needs to have the following columns: date, title, venue, excerpt, url_slug, with a header at the top.
#
# - `excerpt` and `paper_url` can be blank, but the others must have values.
# - `date` must be formatted as YYYY-MM-DD.
# - `url_slug` will be the descriptive part of the .md file and the permalink URL for the page about the paper. The .md file will be `YYYY-MM-[url_slug].md` and the permalink will be `https://[yourdomain]/projects/YYYY-MM-[url_slug]`


# ## Import pandas
#
# We are using the very handy pandas library for dataframes.

# In[2]:
import datetime
import os
import pandas as pd

# ## Import TSV
#
# Pandas makes this easy with the read_csv function. We are using a TSV, so we specify the separator as a tab, or `\t`.
#
# I found it important to put this data in a tab-separated values format, because there are a lot of commas in this kind of data and comma-separated values can get messed up. However, you can modify the import statement, as pandas also has read_excel(), read_json(), and others.

# In[3]:

projects = pd.read_csv("projects.tsv", sep="\t", header=0)
projects

# ## Escape special characters
#
# YAML is very picky about how it takes a valid string, so we are replacing single and double quotes (and ampersands) with their HTML encoded equivilents. This makes them look not so readable in raw format, but they are parsed and rendered nicely.

# In[4]:

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
}


def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c, c) for c in text)


# ## Creating the markdown files
#
# This is where the heavy lifting is done. This loops through all the rows in the TSV dataframe, then starts to concatentate a big string (```md```) that contains the markdown for each type. It does the YAML metadata first, then does the description for the individual page. If you don't want something to appear (like the "Recommended citation")

# In[5]:

for row, item in projects.iterrows():

    # create a string url slug from the title
    url_slug = str(item.title).replace(" ", "-").lower()
    url_slug = url_slug.replace("&", "and")
    url_slug = url_slug.replace("/", "-")
    url_slug = url_slug.replace("(", "")
    url_slug = url_slug.replace(")", "")
    url_slug = url_slug.replace(":", "")
    url_slug = url_slug.replace(";", "")
    url_slug = url_slug.replace("?", "")
    url_slug = url_slug.replace("!", "")
    url_slug = url_slug.replace(",", "")
    url_slug = url_slug.replace(".", "")
    url_slug = url_slug.replace("=", "")
    url_slug = url_slug.replace("+", "")

    date_no_day = item.date[:8]
    html_filename = str(item.date[:7]) + "-" + url_slug
    md_filename = html_filename + ".md"
    year = item.date[:4]

    # YAML variables

    md = "---"

    md += "\ndate: " + str(item.date)

    md += "\ntitle: \"" + item.title + '"\n'

    md += """collection: projects"""

    md += """\npermalink: /projects/""" + html_filename

    if len(str(item.excerpt)) > 5:
        md += "\nexcerpt: \"" + html_escape(item.excerpt) + "\""

    md += "\nvenue: \"" + html_escape(item.venue) + "\""

    md += "\nlast_modified_at: " + \
          str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    md += "\n---"

    # Markdown description for individual page

    md += "\n\n### Skills"
    md += "\n\n- skill 1"
    md += "\n- skill 2"
    md += "\n- skill 3"
    md += "\n\n## Links"
    md += "\n\n- [GitHub Repository](https://github.com/agopalareddy/<repository_name>)"

    md_filename = os.path.basename(md_filename)

    with open("../_projects/" + md_filename, 'w') as f:
        f.write(md)
