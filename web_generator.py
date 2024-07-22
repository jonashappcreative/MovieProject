import os


def serialize_movie(title, year, link):

    output_html = ''

    output_html += f'<li>\n'
    output_html += f'<div class="movie">\n'
    output_html += f'<img class="movie-poster"\nsrc="{link}"/>\n'
    output_html += f'<div class="movie-title">{title}</div>\n'
    output_html += f'<div class="movie-year">{year}</div>\n'
    output_html += f'</div>'
    output_html += f'</li>\n'

    return output_html


def process_data(movies):

    replace_html = ""

    for movie in movies.keys():
        title = movie

        try:
            year = movies[movie]["year"]
        except KeyError:
            year = 0000

        try:
            link = movies[movie]["poster image url"]
        except KeyError:
            link = "N/A"

        replace_html += serialize_movie(title, year, link)
        # DEBUG print(title, year, link)

    return replace_html


def write_html(movies):

    with open("_static/index_template.html", "r") as html_file:
        template_content = html_file.read()

    replace_html = process_data(movies)

    # Replace the placeholder with the generated animal information
    updated_html_content = template_content.replace("__TEMPLATE_MOVIE_GRID__", replace_html)
    output_folder = "/Users/jonashapp/Documents/GitHub/Pycharm/2403056_Codio_MovieProject/"

    # Write the updated HTML content into a new HTML file
    new_html_doc = os.path.join(output_folder, "MoviesApp.html")

    with open(new_html_doc, "w") as output_file:
        output_file.write(updated_html_content)
