from pathlib import Path
from subprocess import run, PIPE
from bs4 import BeautifulSoup as bs
import pytest
import os

path_tests = Path(__file__).parent.resolve()
path_book = path_tests.joinpath("book")
path_html = path_book.joinpath("build", "html")
path_algo = path_html.joinpath("algorithm")


def test_build(tmpdir):
	"""Test building the book template and a few test configs."""
	os.chdir(path_book)

	# Clean build
	run(f"make clean".split())
	assert path_book.joinpath("conf.py").exists()

	# Build the book
	run(f"make html".split(), check=True)

	assert path_book.joinpath("build").exists()
	assert path_html.joinpath("index.html").exists()
	assert path_algo.exists()
	assert path_algo.joinpath("content_rst.html").exists()

@pytest.mark.usefixtures("file_regression")
def test_algorithm(tmpdir, file_regression):
	"""Test algorithm directive markup."""

	algo_list = [
		"_algo_options.html",
		"_algo_nonumber.html",
	]

	# for ialgo in algo_list:
	# 	soup = bs(path_algo.joinpath("content_rst.html").read_text(encoding="utf8"), "html.parser")
	# 	algo = soup.find_all("div", class_="algorithm")[0]

	# 	file_regression.check(str(algo), basename=ialgo.split(".")[0], extension=".html")
