# Copyright (c) 2016-2021 Martin Donath <martin.donath@squidfunk.com>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from collections import defaultdict
from markdown.extensions.toc import slugify
from mkdocs import utils
from mkdocs.config.config_options import Type
from mkdocs.plugins import BasePlugin

# -----------------------------------------------------------------------------
# Class
# -----------------------------------------------------------------------------

# Tags plugin
class TagsPlugin(BasePlugin):

    # Configuration scheme
    config_scheme = (
        ("tags_file", Type(str, required = False)),
    )

    # Initialize plugin
    def __init__(self):
        self.tags = defaultdict(list)
        self.tags_file = None
        self.slugify = None

    # Retrieve configuration for anchor generation
    def on_config(self, config):
        if "toc" in config["markdown_extensions"]:
            toc = { "slugify": slugify, "separator": "-" }
            if "toc" in config["mdx_configs"]:
                toc = { **toc, **config["mdx_configs"]["toc"] }

            # Partially apply slugify function
            self.slugify = lambda value: (
                toc["slugify"](value, toc["separator"])
            )

    # Hack: 2nd pass for tags index page
    def on_files(self, files, **kwargs):
        file = self.config.get("tags_file")
        if file:
            self.tags_file = files.get_file_from_path(file)
            files.append(self.tags_file)

    # Build and render tags index page
    def on_page_markdown(self, markdown, page, **kwargs):
        if page.file == self.tags_file:
            return self.__render_tag_index(markdown)

        # Add page to tags index
        for tag in page.meta.get("tags", []):
            self.tags[tag].append(page)

    # Inject tags into page (after search and before minification)
    def on_page_context(self, context, page, **kwargs):
        if "tags" in page.meta:
            context["tags"] = [
                self.__render_tag(tag)
                    for tag in page.meta["tags"]
            ]

    # -------------------------------------------------------------------------

    # Render tags index
    def __render_tag_index(self, markdown):
        if not "[TAGS]" in markdown:
            markdown += "\n[TAGS]"

        # Replace placeholder in Markdown with rendered tags index
        return markdown.replace("[TAGS]", "\n".join([
            self.__render_tag_links(*args)
                for args in sorted(self.tags.items())
        ]))

    # Render the given tag and links to all pages with occurrences
    def __render_tag_links(self, tag, pages):
        content = ["## <span class=\"md-tag\">{}</span>".format(tag), ""]
        for page in pages:
            url = utils.get_relative_url(
                page.file.src_path,
                self.tags_file.src_path
            )
            content.append("- [{}]({})".format(page.title, url))

        # Return rendered tag links
        return "\n".join(content)

    # Render the given tag, linking to the tags index (if enabled)
    def __render_tag(self, tag):
        if not self.tags_file or not self.slugify:
            return dict(name = tag)
        else:
            url = self.tags_file.url
            url += "#{}".format(self.slugify(tag))
            return dict(name = tag, url = url)
